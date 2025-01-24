import json
import os
from pathlib import Path

from helpers.logs.logs_handler import logger as logging
from redis import StrictRedis

from .cache_interface import CacheInterface
from .cache_redis import RedisCache


class LocalCache(CacheInterface):

  def __init__(self,
               config: dict = {},
               with_redis_client: RedisCache | None = None):
    self.base_dir = config.get("local_base_dir", "./.cache_local_data")
    self.redis_client = with_redis_client

  def _local_cache_path(self, key: str, suffix: str = ".json"):
    return Path(self.base_dir) / Path(key).with_suffix(suffix=suffix)

  def get_raw_redis_client(self):
    return (self.redis_client and
            self.redis_client.get_raw_redis_client()) or None

  def json_get(self, key: str):
    if self.redis_client and self.get_raw_redis_client():
      try:
        value = self.redis_client.json_get(key=key)
        if value:
          return value
      except Exception as e:
        logging.warning("GOT THE ISSUE IN REDIS", e)
        return None
    path = self._local_cache_path(key.replace(":", "/"))
    if path.exists():
      with open(path, "r") as file:
        value = json.load(file)
        if self.redis_client and self.get_raw_redis_client():
          self.redis_client.json_set(key, value)
        return value
    return None

  def json_set(self, key, value):
    if self.redis_client and self.get_raw_redis_client():
      try:
        self.redis_client.json_set(key=key, value=value)
      except Exception as e:
        logging.warning("GOT THE ISSUE IN REDIS", e)
    path = self._local_cache_path(key.replace(":", "/"))
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w") as file:
      json.dump(value, file)

  def json_list_keys(self, prefix: str) -> list[str]:
    if self.redis_client and self.get_raw_redis_client():
      try:
        return self.redis_client.json_list_keys(prefix=prefix)
      except Exception as e:
        logging.warning("GOT THE ISSUE IN REDIS", e)
    prefix = prefix.replace(':', '/')
    whole_prefix = self._local_cache_path(key=prefix, suffix='')
    if not whole_prefix.exists():
      return []
    return [
        str(file.relative_to(self.base_dir)).replace('/',
                                                     ':').replace('.json', '')
        for file in whole_prefix.rglob('*.json')
    ]
