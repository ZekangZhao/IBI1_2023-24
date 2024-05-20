import numpy as np
import matplotlib.pyplot as plt

class SIRModelVaccination:
    def __init__(self, population, initial_infected, vaccination_rate, beta, gamma):
        self.S = population - initial_infected  # Susceptible individuals
        self.I = initial_infected  # Infected individuals
        self.R = 0  # Recovered individuals
        self.V = vaccination_rate * population  # Vaccinated individuals
        self.N = population  # Total population
        self.beta = beta  # Infection rate
        self.gamma = gamma  # Recovery rate
        self.I_values = [self.I]  # Track infected individuals over time
        self.S_values = [self.S]
        self.R_values = [self.R]

    def run(self, days):
        for day in range(days):
            # Calculate the effective contact rate, accounting for vaccination
            effective_contact_rate = self.beta * (self.S + self.I) / (self.N - self.V)

            # Calculate the number of new infections and recoveries
            new_infections = self.S * effective_contact_rate
            new_recoveries = self.I * self.gamma

            # Update the number of susceptible, infected, and recovered individuals
            self.S -= new_infections
            self.I -= new_infections + new_recoveries
            self.R += new_recoveries

            # Append the new values to their respective lists
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
        plt.title('SIR Model with Vaccination')
        plt.legend()
        plt.show()

# Parameters
population = 10000
initial_infected = 1
vaccination_rate = 0.1  # 10% of the population is vaccinated
beta = 0.3
gamma = 0.05
days = 1000

# Run the model with vaccination
model_vaccination = SIRModelVaccination(population, initial_infected, vaccination_rate, beta, gamma)
model_vaccination.run(days)
model_vaccination.plot()