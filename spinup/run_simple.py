
from spinup.utils.run_utils import ExperimentGrid
from spinup import ddpg, ppo, vpg

import gym
import tensorflow as tf

def run_experiment(args):
    def env_fn():
        import gym_flexibility  # register gym_flexibility to gym env registry
        return gym.make(args.env_name)

    eg = ExperimentGrid(name=args.exp_name)
    eg.add('env_fn', env_fn)
    eg.add('seed', [10*i for i in range(args.num_runs)])
    eg.add('epochs', args.epochs)
    eg.add('steps_per_epoch', args.steps_per_epoch)
    eg.add('save_freq', args.save_freq)
    eg.add('max_ep_len', 200)
    eg.add('ac_kwargs:activation', tf.tanh, '')
    if args.algo == "ppo":
        eg.run(ppo)
    elif args.algo == "vpg":
        eg.run(vpg)

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--algo", type=str, default="ppo")
    parser.add_argument("--cpu", type=int, default=1)
    parser.add_argument("--epochs", type=int, default=5)
    parser.add_argument("--num_runs", type=int, default=2)
    parser.add_argument('--steps_per_epoch', type=int, default=5000)
    parser.add_argument('--save_freq', type=int, default=2000)
    parser.add_argument('--env_name', type=str, default="Flexibility-v0")
    parser.add_argument('--exp_name', type=str, default='Flexibility-PPO')

    args = parser.parse_args()

    run_experiment(args)