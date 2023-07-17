## Pycon-India-2023-Learn-and-Adapt

This repository contains code for Pycon India 2023 talk titled "Learn and Adapt: Shaping AI with Reinforcement Learning using the [Gymnasium Framework](https://gymnasium.farama.org/)". It contains two examples of **custom reinforcement learning agent** created using the Gymnasium Framework in a Stock Market environment where the Agent can either Buy, Sell, or Hold the stock at any given step:

1. [01_custom_agent](01_custom_agent): Samples through the action space randomly.
2. [02_dqnetwork_agent](02_dqnetwork_agent): Trains on a **Deep-Q-Network** with a **LSTM model** to predict the action.

## Libraries Used

- [Gymnasium](https://github.com/Farama-Foundation/Gymnasium)
- [Tensorflow](https://github.com/tensorflow/tensorflow)
- [Pandas](https://github.com/pandas-dev/pandas)
- [Numpy](https://github.com/numpy/numpy)
- [Matplotlib](https://github.com/matplotlib/matplotlib)

## Setup on Local

[Anaconda](https://www.anaconda.com/download) is recommended for creating a virtual environment, specially for MacOS Silicon users. `venv` can also be used.

#### Using Anaconda

1. Create a Virtual Environment using Anaconda:

```sh
conda create --name pycon python=3.8
```

2. Activate the Virtual Environment:

```sh
conda activate pycon
```

#### Using venv

1. Create a Virtual Environment using `venv`:

```sh
python -m venv venv
```

2. Active the Virtual Environment:

```sh
source venv/bin/activate
```

#### Common Steps

3. Install the Libraries through requirement.txt file:

```sh
pip install -r requirements.txt
```

4. Run any of the custom stock market trading agent:

```sh
python main.py
```

Note: In order to deactivate the environment once you are done, you can use the following command: `conda deactivate`.

### MacOS Silicon Users

1. Install `tensorflow-deps` for Anaconda:

```sh
conda install -c apple tensorflow-deps
```

2. Change `tensorflow` in [requirements.txt](requirements.txt) file to `tensorflow-macos`.

3. Install using `requirements.txt`:

```sh
pip install -r requirements.txt
```
