import random
import numpy as np
from sklearn.linear_model import LinearRegression

NUM_UPF_INSTANCES = 5
NUM_TIME_STEPS = 100
MAX_DISTANCE = 100

user_positions = [random.uniform(0, MAX_DISTANCE) for _ in range(NUM_TIME_STEPS)]

throughput_data = []
latency_data = []
energy_consumption_data = []

for step in range(NUM_TIME_STEPS):
    upf_throughput = [random.uniform(1, 10) for _ in range(NUM_UPF_INSTANCES)]
    upf_latency = [random.uniform(1, 5) for _ in range(NUM_UPF_INSTANCES)]
    upf_energy_consumption = [random.uniform(50, 200) for _ in range(NUM_UPF_INSTANCES)]

    user_position = user_positions[step]
    X = np.array(upf_throughput).reshape(-1, 1)

    throughput_model = LinearRegression()
    throughput_model.fit(X, upf_throughput)
    predicted_throughput = throughput_model.predict([[user_position]])

    latency_model = LinearRegression()
    latency_model.fit(X, upf_latency)
    predicted_latency = latency_model.predict([[user_position]])

    energy_model = LinearRegression()
    energy_model.fit(X, upf_energy_consumption)
    predicted_energy_consumption = energy_model.predict([[user_position]])

    throughput_data.append(predicted_throughput[0])
    latency_data.append(predicted_latency[0])
    energy_consumption_data.append(predicted_energy_consumption[0])

print("User Positions:", user_positions)
print("Predicted Throughput:", throughput_data)
print("Predicted Latency:", latency_data)
print("Predicted Energy Consumption:", energy_consumption_data)