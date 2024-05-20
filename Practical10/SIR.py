import numpy as np
import matplotlib.pyplot as plt

class SIRModel:
    def __init__(self, population, initial_infected, beta, gamma):
        self.S = population - initial_infected
        self.I = initial_infected
        self.R = 0
        self.N = population
        self.beta = beta
        self.gamma = gamma
        self.I_values = [self.I]
        self.S_values = [self.S]
        self.R_values = [self.R]

    def run(self, days):
        for day in range(days):
            new_infections = self.beta * self.S * self.I / self.N
            new_recoveries = self.gamma * self.I
            self.S -= new_infections
            self.I -= new_infections + new_recoveries
            self.R += new_recoveries
            self.I_values.append(self.I)
            self.S_values.append(self.S)
            self.R_values.append(self.R)

    def plot(self):
        plt.figure(figsize=(6, 4), dpi=150)
        plt.plot(self.S_values, label='Susceptible')
        plt.plot(self.I_values, label='Infected')
        plt.plot(self.R_values, label='Recovered')
        plt.xlabel('Days')
        plt.ylabel('Number of People')
        plt.title('SIR Model')
        plt.legend()
        plt.show()

# Parameters
population = 10000
initial_infected = 1
beta = 0.3
gamma = 0.05
days = 1000

# Run the model
model = SIRModel(population, initial_infected, beta, gamma)
model.run(days)
model.plot()