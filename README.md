## Pycon-India-2023-Learn-and-Adapt

This repository contains code for Pycon India 2023 talk titled "Learn and Adapt: Shaping AI with Reinforcement Learning using the [Gymnasium Framework](https://gymnasium.farama.org/)". It contains two examples of **custom reinforcement learning agent** created using the Gymnasium Framework in a Stock Market environment where the Agent has to either Buy, Sell, or Hold the stock:

1. [01_custom_agent](01_custom_agent): Custom Gymnasium Agent that samples through the action space randomly.
2. [02_dqnetwork_agent](02_dqnetwork_agent): Custom Gymnasium Agent that trains on a **Deep-Q-Network** with a **LSTM model**.

## Libraries Used

- [Gymnasium](https://github.com/Farama-Foundation/Gymnasium)
- [Tensorflow](https://github.com/tensorflow/tensorflow)
- [Pandas](https://github.com/pandas-dev/pandas)
- [Numpy](https://github.com/numpy/numpy)
- [Matplotlib](https://github.com/matplotlib/matplotlib)

## Setup on Local

1. Create a Virtual Environment using [Anacond](https://www.anaconda.com/download):

Although Anaconda is not a hard requirement, it's recommended, specially for MacOS Silicon users.

```sh
conda create --name pycon python=3.8
```

2. Activate the Virtual Environment:

```sh
conda activate pycon
```

3. Install the Libraries through requirement.txt file:

```sh
pip install -r requirements.txt
```

4. Run the custom stock market trading agent:

```sh
python main.py
```

Note: In order to deactivate the environment once you are done using, you can use the following command: `conda deactivate`.

### MacOS Silicon Users

1. Install `tensorflow-deps` for conda:

```sh
conda install -c apple tensorflow-deps
```

2. Change `tensorflow` in `requirements.txt` file to `tensorflow-macos`.

3. Install using `requirements.txt`:

```sh
pip install -r requirements.txt
```
