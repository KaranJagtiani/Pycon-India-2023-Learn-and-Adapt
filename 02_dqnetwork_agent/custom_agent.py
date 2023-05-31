import gymnasium as gym
from gymnasium import spaces
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class StockTradingEnv(gym.Env):
    def __init__(self, csv_file):
        super(StockTradingEnv, self).__init__()

        # Load data from a csv file
        self.df = pd.read_csv(csv_file)
        self.reward_range = (0, np.inf)
        self.action_space = spaces.Discrete(3)  # Sell, Hold, Buy
        self.observation_space = spaces.Box(
            low=0, high=float('inf'), shape=(2,), dtype=np.float16)  # Balance, Stock Price

        self.init_balance = 10000  # Initial balance
        self.balance = self.init_balance
        self.n_stocks = 0  # Number of stocks held
        self.current_step = 0

        # Added to count number of trades
        self.trade_count = 0

        # Store transactions for rendering
        self.transactions = []  # Each element is a tuple (step, price, action)

    def step(self, action):
        self.current_step += 1

        action_penalty = 0  # Penalty depending on the action chosen
        hold_reward = 0  # Reward for holding

        if action == 0:  # Sell
            self.balance += self.n_stocks * self.df.loc[self.current_step, 'Close']
            self.transactions.append((self.current_step, self.df.loc[self.current_step, 'Close'], 'Sell'))
            self.n_stocks = 0
            action_penalty = 50  # Arbitrary penalty value
            self.trade_count += 1
        elif action == 2:  # Buy
            self.n_stocks += self.balance / self.df.loc[self.current_step, 'Close']
            self.transactions.append((self.current_step, self.df.loc[self.current_step, 'Close'], 'Buy'))
            self.balance = 0
            action_penalty = 50  # Arbitrary penalty value
            self.trade_count += 1
        else:  # Hold
            # Reward for holding action
            hold_reward = 0.01 * (self.balance + self.n_stocks * self.df.loc[self.current_step, 'Close'])

        # Update balance to include held stocks
        total_balance = self.balance + self.n_stocks * self.df.loc[self.current_step, 'Close']

        reward = total_balance - self.init_balance - action_penalty + hold_reward  # Updated reward
        done = self.current_step >= len(self.df.loc[:, 'Close']) - 1

        # Increase penalty with trade_count
        action_penalty *= self.trade_count

        return np.array([self.balance, self.df.loc[self.current_step, 'Close']]), reward, done, {}

    def reset(self):
        # Reset the state of the environment to an initial state
        self.balance = self.init_balance
        self.n_stocks = 0
        self.current_step = 0
        self.transactions = []

        return np.array([self.balance, self.df.loc[self.current_step, 'Close']])

    def render(self, mode='human'):
        # Render the environment to the screen
        if mode == 'human':
            print(f'Step: {self.current_step}, Balance: {self.balance}, Stocks held: {self.n_stocks}, '
                  f'Stock Price: {self.df.loc[self.current_step, "Close"]}, Total Balance: '
                  f'{self.balance + self.n_stocks * self.df.loc[self.current_step, "Close"]}')
        elif mode == 'system':
            buy_steps = [item[0] for item in self.transactions if item[2] == 'Buy']
            sell_steps = [item[0] for item in self.transactions if item[2] == 'Sell']
            buy_prices = [item[1] for item in self.transactions if item[2] == 'Buy']
            sell_prices = [item[1] for item in self.transactions if item[2] == 'Sell']

            plt.figure(figsize=(10,5))
            plt.plot(self.df.loc[:, 'Close'], label='Close Price')
            plt.scatter(buy_steps, buy_prices, color='green', label='Buy')
            plt.scatter(sell_steps, sell_prices, color='red', label='Sell')
            plt.title('Stock Price and Transactions')
            plt.xlabel('Steps')
            plt.ylabel('Price')
            plt.legend(loc='upper left')
            plt.grid(True)
            plt.show()

