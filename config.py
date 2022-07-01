import json

EVAL_EPISODES = 11  # 10 for evaluation + 1 leaderboard video
EVAL_MAX_STEPS = float('inf')

settings = json.load(open('aicrowd.json'))
if settings['debug']:  # if debug flag is set to true, evaluation will only run a single episode for 100 steps
    EVAL_EPISODES = 1
    EVAL_MAX_STEPS = 100
