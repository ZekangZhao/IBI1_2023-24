import numpy as np
import matplotlib.pyplot as plt

class SpatialSIRModel:
    def __init__(self, size, beta, gamma):
        self.size = size
        self.beta = beta
        self.gamma = gamma
        self.population = np.zeros((size, size), dtype=int)
        self.infect_random()

    def infect_random(self):
        x, y = np.random.randint(0, self.size, size=2)
        self.population[x, y] = 1

    def infect_neighbors(self):
        for i in range(self.size):
            for j in range(self.size):
                if self.population[i, j] == 1:  # Infected individual
                    for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:  # 4 neighbors
                        ni, nj = i + di, j + dj
                        if 0 <= ni < self.size and 0 <= nj < self.size and self.population[ni, nj] == 0:
                            # Infection probability for a susceptible neighbor
                            if np.random.rand() < self.beta:
                                self.population[ni, nj] = 1

    def recover(self):
        # Simple recovery without immunity for simplicity
        self.population[self.population == 1] = (self.population[self.population == 1] > 0) * np.random.rand(self.population[self.population == 1].size) < self.gamma

    def run(self, days):
        for day in range(days):
            self.infect_neighbors()
            self.recover()
            plt.figure(figsize=(6, 6))
            plt.imshow(self.population, cmap='viridis', interpolation='nearest')
            plt.title(f'Day {day}')
            plt.show()

# Parameters
size = 100
beta = 0.3
gamma = 0.05
days = 100

# Run the spatial SIR model
model = SpatialSIRModel(size, beta, gamma)
model.run(days)