from custom_agent import StockTradingEnv
from dqnetwork import DQNAgent
import numpy as np

env = StockTradingEnv('../stock.csv')

state_size = env.observation_space.shape[0]
action_size = env.action_space.n
agent = DQNAgent(state_size, action_size)

n_episodes = 5  # Number of episodes
batch_size = 32

for episode in range(n_episodes):
    state = env.reset()
    state = np.reshape(state, [1, 1, state_size])
    done = False
    while not done:
        action = agent.act(state)
        next_state, reward, done, _ = env.step(action)
        next_state = np.reshape(next_state, [1, 1, state_size])
        agent.remember(state, action, reward, next_state, done)
        state = next_state
        if done:
            print("episode: {}/{}, score: {}, e: {:.2}".format(episode, n_episodes, time, agent.epsilon))
            break
        if len(agent.memory) > batch_size:
            agent.replay(batch_size)

env.render(mode="system")