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
    # Simplified throughput calculation
    return np.random.rand() * 100  # Mbps


def calculate_energy_consumption():
    # Simplified energy consumption calculation
    return np.random.rand() * 10  # Watt-hours


def calculate_latency():
    # Simplified latency calculation
    return np.random.rand() * 10  # ms


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
    num_upfs = 3  # Number of UPFs
    num_users = 5  # Number of users

    simulator = NetworkSimulator(num_upfs, num_users)
    simulator.run_simulation()
