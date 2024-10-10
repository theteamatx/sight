# Copyright 2023 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Setting up configuration for DQN Experiment."""

from absl import flags
from acme import specs
from acme import wrappers
from acme.agents.jax import dqn
from acme.agents.jax.dqn import losses
from acme.jax import experiments
from acme.jax import networks as networks_lib
from acme.jax import utils
import haiku as hk
import jax.numpy as jnp

NUM_QUANTILES = flags.DEFINE_integer('num_quantiles', 20,
                                     'Number of bins to use.')


def build_qrdqn_config():
  """Builds QR-DQN experiment config which can be executed in different ways."""

  def env_factory(seed):
    # del seed
    # return helpers.make_atari_environment(
    #     level=env_name, sticky_actions=True, zero_discount_on_life_loss=False)
    return None

  def net_factory(environment_spec: specs.EnvironmentSpec) -> dqn.DQNNetworks:
    """Creates networks for training DQN on Gym Env."""
    num_quantiles = 20

    def network(inputs):
      model = hk.Sequential([
          hk.nets.MLP(
              [512, 128, environment_spec.actions.num_values * num_quantiles]),
      ])
      q_dist = model(inputs).reshape(-1, environment_spec.actions.num_values,
                                     num_quantiles)
      q_values = jnp.mean(q_dist, axis=-1)
      return q_values, q_dist

    network_hk = hk.without_apply_rng(hk.transform(network))
    obs = utils.add_batch_dim(utils.zeros_like(environment_spec.observations))
    network = networks_lib.FeedForwardNetwork(
        init=lambda rng: network_hk.init(rng, obs), apply=network_hk.apply)
    typed_network = networks_lib.non_stochastic_network_to_typed(network)
    return dqn.DQNNetworks(policy_network=typed_network)

  # Construct the agent.
  config = dqn.DQNConfig(discount=0.99, n_step=1, epsilon=0.1)

  loss_fn = losses.QrDqn(num_atoms=2, huber_param=1.)
  dqn_builder = dqn.DistributionalDQNBuilder(config, loss_fn=loss_fn)

  return experiments.ExperimentConfig(builder=dqn_builder,
                                      environment_factory=env_factory,
                                      network_factory=net_factory,
                                      seed=0,
                                      max_num_actor_steps=100)
