# n users and n UPFs (n=10 here) (stationary users)

import numpy as np


class UPF:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class User:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def calculate_throughput():
    return np.random.rand() * 100


def calculate_energy_consumption():
    return np.random.rand() * 10


def calculate_latency():
    return np.random.rand() * 10


class NetworkSimulator:
    def __init__(self, num_upfs, num_users):
        self.upfs = [UPF(np.random.rand(), np.random.rand()) for _ in range(num_upfs)]
        self.users = [User(np.random.rand(), np.random.rand()) for _ in range(num_users)]

    def run_simulation(self):
        for user in self.users:
            for upf in self.upfs:
                throughput = calculate_throughput()
                latency = calculate_latency()
                energy_consumption = calculate_energy_consumption()
                print(f"User at ({user.x:.2f}, {user.y:.2f}) connected to UPF at ({upf.x:.2f}, {upf.y:.2f}):")
                print(f"Throughput: {throughput:.2f} Mbps")
                print(f"Latency: {latency:.2f} ms")
                print(f"Energy Consumption: {energy_consumption:.2f} Watt-hours")
                print("=" * 50)


if __name__ == "__main__":
    num_upfs = 10
    num_users = 10

    simulator = NetworkSimulator(num_upfs, num_users)
    simulator.run_simulation()
