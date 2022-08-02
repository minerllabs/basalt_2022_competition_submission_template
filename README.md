# NeurIPS 2022: MineRL BASALT Competition Starter Kit

[![Discord](https://img.shields.io/discord/565639094860775436.svg)](https://discord.gg/BT9uegr)

This repository is the main MineRL BASALT 2022 Competition **submission template** (only for the "basalt" track")!

You can find the "intro" track submission kit [here](https://github.com/minerllabs/basalt_intro_track_2022_competition_submission_template).

MineRL BASALT is a competition on solving human-judged tasks. The tasks in this competition do not have a pre-defined reward function: the goal is to produce trajectories that are judged by real humans to be effective at solving a given task.

See [the AICrowd competition page](https://www.aicrowd.com/challenges/neurips-2022-minerl-basalt-competition) for further information.

**This repository contains**:
*  **Documentation** on how to submit your agent to the leaderboard
*  **Starter code** for you to base your submission (an agent that takes random actions)!

**Other Resources**:
- [AICrowd competition page](https://www.aicrowd.com/challenges/neurips-2022-minerl-basalt-competition) - Main registration page & leaderboard.
- [MineRL Documentation](http://minerl.io/docs) - Documentation for the `minerl` package!

# How to Submit a Model on AICrowd.

In brief: you define your Python environment using Anaconda environment files, and AICrowd system will use the `run.py` file to train and evaluate your agents.

You submit pretrained models, the evaluation code and the training code. Training code should produce the same models you upload as part of your submission. You **must** upload the training code; which will be used to retrain and validate finalist submissions.

Your evaluation code (`test_<env_name>.py`) only needs to control the agent and accomplish the environment's task. The evaluation server will handle recording of videos. Do not change the number of episodes played or maximum number of steps executed: the submissions will fail otherwise.

## Setup

1.  **Clone the github repository** or press the "Use this Template" button on GitHub!

    ```
    git clone https://github.com/minerllabs/basalt_2022_competition_submission_template.git
    ```

2. **Install** MineRL specific dependencies! Mainly, make sure you have Java JDK 8! See more details [here](https://minerl.readthedocs.io/en/v1.0.0/tutorials/index.html)

3. **Specify** your specific submission dependencies (PyTorch, Tensorflow, kittens, puppies, etc.)

    * **Anaconda Environment**. To make a submission you need to specify the environment using Anaconda environment files. It is also recommended you recreate the environment on your local machine. Make sure at least version `4.5.11` is required to correctly populate `environment.yml` (By following instructions [here](https://www.anaconda.com/download)). Then:
       * **Create your new conda environment**

            ```sh
            cd basalt_2022_competition_submission_template
            conda env create -f environment.yml
            conda activate minerl
            ```

      * **Your code specific dependencies**
        Add your own dependencies to the `environment.yml` file. **Remember to add any additional channels**. PyTorch requires the channel `pytorch`, for example.
        You can also install them locally using
        ```sh
        conda install <your-package>
        ```

    * **Pip Packages** If you need pip packages (not on conda), you can add them to the `environment.yml` file (see the currently populated version):

    * **Apt Packages** If your training procedure or agent depends on specific Debian (Ubuntu, etc.) packages, add them to `apt.txt`.

If above are too restrictive for defining your environment, see [this Discourse topic for more information](https://discourse.aicrowd.com/t/how-to-specify-runtime-environment-for-your-submission/2274).

## What should my code structure be like ?

Please follow the example structure shared in the starter kit for the code structure.
The different files and directories have the following meaning:

```
.
├── aicrowd.json                     # Submission meta information like your username
├── apt.txt                          # Packages to be installed inside docker image
├── config.py                        # Config for debugging submissions
├── data                             # DO NOT UPLOAD THE DATASET. This data will be available on the training instance.
│   ├── MineRLBasaltBuildVillageHouse-v0
│   │   ├── Player139-40dd711bfe2e-20220626-202049.jsonl
│   │   ├── Player139-40dd711bfe2e-20220626-202049.mp4
│   │   ├── Player139-62ae2702e774-20220626-201655.jsonl
│   │   ├── Player139-62ae2702e774-20220626-201655.mp4
│   │   └── ... rest of the files
│   ├── MineRLBasaltCreateVillageAnimalPen-v0
│   │   └── ... files as above
│   ├── MineRLBasaltFindCave-v0
│   │   └── ... files as above
│   ├── MineRLBasaltMakeWaterfall-v0
│   │   └── ... files as above
│   └── VPT-models
│       ├── foundation-model-1x.model
│       ├── foundation-model-1x.weights
│       ├── foundation-model-3x.model
│       ├── foundation-model-3x.weights
│       └── ... rest of the models
├── environment.yml                  # Conda environment description
├── LICENCE                          # Licence
├── run.py                           # The file that runs training and evaluation
├── test_BuildVillageHouse.py        # IMPORTANT: Your testing/inference phase code.
├── test_CreateVillageAnimalPen.py   # IMPORTANT: Your testing/inference phase code.
├── test_FindCave.py                 # IMPORTANT: Your testing/inference phase code.
├── test_MakeWaterfall.py            # IMPORTANT: Your testing/inference phase code.
├── train                            # IMPORTANT: Your trained models MUST be saved inside this directory
└── train.py                         # IMPORTANT: Your training code. Running this should produce the same agent as you upload as part of the agent.
```

Finally, **you must specify an AIcrowd submission JSON in `aicrowd.json` to be scored!**

The `aicrowd.json` of each submission should contain the following content:

```json
{
  "challenge_id": "neurips-2022-minerl-basalt-competition",
  "authors": ["your-aicrowd-username"],
  "description": "sample description about your awesome agent",
  "license": "MIT",
  "gpu": true,
  "debug": true,
  "track": "basalt"
}
```

This JSON is used to map your submission to the said challenge, so please remember to use the correct `challenge_id` as specified above.

By default, the `debug` flag is set to `true`. This makes evaluations run a single short episode. Please submit this way first to see if everything works fine on the AICrowd side. If it does, go ahead and submit with `debug` set to `false`.

Please specify if your code will use a GPU or not for the evaluation of your model.

### Dataset and pretrained model location for training

You **don't** need to upload the provided BASALT dataset or pretrained models for the training stage, and it will be provided in online submissions at `MINERL_DATA_ROOT` path (points to the `data` directory), should you need them for training. Note that `data` directory is not filled with data during initial evaluation phase.

**Please** only add files needed for the submission; too large submissions may fail randomly. Having large git history is fine.

See instructions [here](https://github.com/minerllabs/basalt-2022-behavioural-cloning-baseline#downloading-basalt-dataset) on how to download the BASALT dataset.

## How to submit!

To make a submission, you will have to create a private repository on [https://gitlab.aicrowd.com/](https://gitlab.aicrowd.com/).

You will have to add your SSH Keys to your GitLab account by following the instructions [here](https://docs.gitlab.com/ee/user/ssh.html).
If you do not have SSH Keys, you will first need to [generate one](https://docs.gitlab.com/ee/user/ssh.html#generate-an-ssh-key-pair).

Then you can create a submission by making a _tag push_ to your repository on [https://gitlab.aicrowd.com/](https://gitlab.aicrowd.com/).
**Any tag push (where the tag name begins with "submission-") to your private repository is considered as a submission**
Then you can add the correct git remote, and finally submit by doing:

```
cd basalt_2022_competition_submission_template
# Add AIcrowd git remote endpoint
git remote add aicrowd git@gitlab.aicrowd.com:<YOUR_AICROWD_USER_NAME>/basalt_2022_competition_submission_template.git
git push aicrowd main

# Create a tag for your submission and push
git tag -am "submission-v0.1" submission-v0.1
git push aicrowd main
git push aicrowd submission-v0.1

# Note : If the contents of your repository (latest commit hash) do not change,
# then pushing a new tag will **not** trigger a new evaluation.
```

You now should be able to see the details of your submission at: `https://gitlab.aicrowd.com/<YOUR_AICROWD_USER_NAME>/basalt_2022_competition_submission_template/issues/`

**Best of Luck** :tada: :tada:

## Large model files

To upload large model files (e.g., your fine-tuned versions of the OpenAI VPT models, which can reach gigabytes), use git LFS. See instructions [here](https://discourse.aicrowd.com/t/how-to-upload-large-files-size-to-your-submission/2304).

# Ensuring that your code works.

You can perform local training and evaluation by simply running `python run.py`, which then runs `train.py` and all four `test_<env_name>.py` scripts.

**Note** that you do not need to record videos in your code! AICrowd server will handle this. Your code only needs to play the games.

# Team

The quick-start kit was authored by
[Anssi Kanervisto](https://www.microsoft.com/en-us/research/people/t-anssik/), [Karolis Ramanauskas](https://ka.rol.is/) and [Shivam Khandelwal](https://twitter.com/skbly7) with help from [William H. Guss](http://wguss.ml)

The BASALT competition is organized by the following team:

* [Anssi Kanervisto](https://www.microsoft.com/en-us/research/people/t-anssik/) (Microsoft Research)
* [Stephanie Milani](https://stephmilani.github.io/) (Carnegie Mellon University)
* [Karolis Ramanauskas](https://ka.rol.is/) (Independent)
* [Byron V. Galbraith](https://github.com/bgalbraith) (Seva Inc.)
* Steven H. Wang (ETH Zürich)
* [Sander Schulhoff](https://trigaten.github.io/) (University of Maryland)
* Brandon Houghton (OpenAI)
* Sharada Mohanty (AIcrowd)
* [Rohin Shah](https://rohinshah.com) (DeepMind)

Advisors:

* Andrew Critch (Encultured.ai)
* Fei Fang (Carnegie Mellon University)
* Kianté Brantley (Cornell University)
* Sam Devlin (Microsoft Research)
* Oriol Vinyals (DeepMind)
