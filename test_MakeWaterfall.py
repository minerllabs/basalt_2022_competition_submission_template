import logging

import gym
import minerl

from config import EVAL_EPISODES, EVAL_MAX_STEPS

import coloredlogs
coloredlogs.install(logging.DEBUG)

MINERL_GYM_ENV = 'MineRLBasaltMakeWaterfall-v0'


def main():
    env = gym.make(MINERL_GYM_ENV)
    max_steps = min(EVAL_MAX_STEPS, env._max_episode_steps)

    # Load your model here
    # model = None

    for i in range(EVAL_EPISODES):
        obs = env.reset()
        for _ in range(max_steps):

            # Step your model here. Currently, it's using random actions:
            random_act = env.action_space.sample()
            obs, reward, done, info = env.step(random_act)

            if done:
                break
        print(f"[{i}] Episode complete")

    env.close()


if __name__ == "__main__":
    main()
