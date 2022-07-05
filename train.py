import logging
import os

import numpy as np
import gym
import minerl

import coloredlogs
coloredlogs.install(logging.DEBUG)

# The dataset and trained models are available in data/ directory from repository root.
MINERL_DATA_ROOT = os.getenv('MINERL_DATA_ROOT', 'data/')


def main():
    """
    This function will be called for training phase.
    This should produce and save same files you upload during your submission.
    All trained models should be placed under "train" directory!
    """
    # Sample code for illustration, add your training code below
    env = gym.make('MineRLBasaltFindCave-v0')

    # For an example, lets just run 100 steps of the environment for training
    obs = env.reset()
    for _ in range(100):
        obs, reward, done, info = env.step(env.action_space.sample())
        # Do your training here
        if done:
            break

    # Save trained model to train/ directory
    # For a demonstration, we save some dummy data.
    # NOTE: All trained models should be placed under train directory!
    np.save("./train/parameters.npy", np.random.random((10,)))

    # Close environment and clean up any bigger memory hogs.
    # Otherwise, you might start running into memory issues.
    env.close()


if __name__ == "__main__":
    main()
