import simpy
import random

NUM_UPFS = 3
NUM_USERS = 1
SIMULATION_TIME = 1000


class User:
    def __init__(self, env):
        self.env = env
        self.position = (random.uniform(0, 100), random.uniform(0, 100))
        self.throughput = 0
        self.latency = 0
        self.energy_consumption = 0
        self.upf = None

    def move(self):
        while True:
            yield self.env.timeout(1)
            self.position = (random.uniform(0, 100), random.uniform(0, 100))


class UPF:
    def __init__(self, env):
        self.env = env

    def serve_user(self, user):
        while True:
            yield self.env.timeout(1)
            user.throughput = random.uniform(1, 100)
            user.latency = random.uniform(1, 10)
            user.energy_consumption = random.uniform(1, 10)


def simulate(env, users):
    upfs = [UPF(env) for _ in range(NUM_UPFS)]

    for user in users:
        user.upf = random.choice(upfs)
        env.process(user.move())

    for upf in upfs:
        for user in users:
            env.process(upf.serve_user(user))

    yield env.timeout(SIMULATION_TIME)


env = simpy.Environment()
users = [User(env) for _ in range(NUM_USERS)]
env.process(simulate(env, users))
env.run(until=SIMULATION_TIME)

user = users[0]
print("Simulation results for a single user:")
print(f"Final position: {user.position}")
print(f"Throughput: {user.throughput:.2f} Mbps")
print(f"Latency: {user.latency:.2f} ms")
print(f"Energy Consumption: {user.energy_consumption:.2f} Watt-hours")
