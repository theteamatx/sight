from abc import ABC
from abc import abstractmethod


class CacheInterface(ABC):

  @abstractmethod
  def json_get(self, key):
    pass

  @abstractmethod
  def json_set(self, key, value):
    pass
