import json
import logging
import os
import atexit

import aicrowd_helper
import gym
import minerl
from minerl.herobraine.wrappers import downscale_wrapper

from test_submission_code import MineRLAgent, Episode, EpisodeDone

import coloredlogs
coloredlogs.install(logging.DEBUG)

MINERL_GYM_ENV = os.getenv('MINERL_GYM_ENV', 'MineRLBasaltFindCaveHighRes-v0')
MINERL_MAX_EVALUATION_EPISODES = int(os.getenv('MINERL_MAX_EVALUATION_EPISODES', 5))
# We only use one evaluation thread
EVALUATION_THREAD_COUNT = 1

####################
# EVALUATION CODE  #
####################


def main():
    agent = MineRLAgent()
    agent.load_agent()

    assert MINERL_MAX_EVALUATION_EPISODES > 0
    assert EVALUATION_THREAD_COUNT > 0

    env = gym.make(MINERL_GYM_ENV)
    # Bit of sanity check
    if env.observation_space['pov'].shape[0] != 1024:
        raise RuntimeError('The MineRL environment should be a "HighRes" variant.')
    # Apply downscale wrapper to turn (1024, 1024) observations into (64, 64)
    env = downscale_wrapper.DownscaleWrapper(env)

    # Ensure that videos are closed properly
    @atexit.register
    def cleanup_env():
        env.close()

    for i in range(MINERL_MAX_EVALUATION_EPISODES):
        try:
            agent.run_agent_on_episode(Episode(env))
        except EpisodeDone:
            print("[{}] Episode complete".format(i))


if __name__ == "__main__":
    main()
