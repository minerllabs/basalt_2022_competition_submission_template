import logging
import coloredlogs

import aicrowd_gym
import minerl

from config import EVAL_EPISODES, EVAL_MAX_STEPS

coloredlogs.install(logging.DEBUG)

MINERL_GYM_ENV = 'MineRLBasaltCreateVillageAnimalPen-v0'


def main():
    # NOTE: It is important that you use "aicrowd_gym" instead of regular "gym"!
    #       Otherwise, your submission will fail.
    env = aicrowd_gym.make(MINERL_GYM_ENV)

    # Load your model here
    # NOTE: The trained parameters must be inside "train" directory!
    # model = None

    for i in range(EVAL_EPISODES):
        obs = env.reset()
        done = False
        for step_counter in range(EVAL_MAX_STEPS):

            # Step your model here.
            # Currently, it's doing random actions
            # for 200 steps before quitting the episode
            random_act = env.action_space.sample()

            if step_counter < 200:
                random_act["ESC"] = 0
            else:
                random_act["ESC"] = 1

            obs, reward, done, info = env.step(random_act)

            if done:
                break
        print(f"[{i}] Episode complete")

    # Close environment and clean up any bigger memory hogs.
    # Otherwise, you might start running into memory issues
    # on the evaluation server.
    env.close()


if __name__ == "__main__":
    main()
