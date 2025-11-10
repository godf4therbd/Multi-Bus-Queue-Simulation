"""
Multi-Bus Queue Simulation for University Shuttle Service
Author: Biswajit (2025)
Description:
    A discrete-event simulation that models students arriving
    at a bus stop and buses serving them at fixed intervals with limited capacity.
"""

import random
import math
from pprint import pprint

def exp_interarrival(mean):
    """Generate exponential inter-arrival time with given mean."""
    return random.expovariate(1.0 / mean)

def simulate_bus_system(
    sim_time=120,          
    mean_interarrival=1.5, 
    bus_interval=10,       
    bus_capacity=30,       
    seed=42                
):
    random.seed(seed)

    time = 0.0
    queue = []
    next_student_arrival = exp_interarrival(mean_interarrival)
    next_bus_arrival = bus_interval

    total_waiting_time = 0.0
    total_served = 0
    max_queue_len = 0
    total_arrivals = 0
    total_seats_offered = 0

    while time < sim_time:
        if next_student_arrival < next_bus_arrival and next_student_arrival <= sim_time:
            time = next_student_arrival
            queue.append(time)
            total_arrivals += 1
            if len(queue) > max_queue_len:
                max_queue_len = len(queue)
            next_student_arrival = time + exp_interarrival(mean_interarrival)
        else:
            if next_bus_arrival > sim_time:
                break
            time = next_bus_arrival
            seats_left = bus_capacity
            total_seats_offered += bus_capacity
            while seats_left > 0 and len(queue) > 0:
                student_arrival_time = queue.pop(0)
                waiting = time - student_arrival_time
                total_waiting_time += waiting
                total_served += 1
                seats_left -= 1
            next_bus_arrival = time + bus_interval

    leftover_students = len(queue)
    avg_wait = total_waiting_time / total_served if total_served > 0 else 0
    bus_utilization = (total_served / total_seats_offered) if total_seats_offered > 0 else 0

    return {
        "Simulation time": sim_time,
        "Mean inter-arrival": mean_interarrival,
        "Bus interval": bus_interval,
        "Bus capacity": bus_capacity,
        "Total arrivals": total_arrivals,
        "Total served": total_served,
        "Leftover students": leftover_students,
        "Average waiting time (min)": round(avg_wait, 3),
        "Max queue length": max_queue_len,
        "Bus seat utilization": round(bus_utilization, 3)
    }

def run_scenarios():
    scenarios = [
        {"sim_time": 120, "mean_interarrival": 1.5, "bus_interval": 10, "bus_capacity": 30},
        {"sim_time": 120, "mean_interarrival": 1.5, "bus_interval": 8,  "bus_capacity": 30},
        {"sim_time": 120, "mean_interarrival": 1.5, "bus_interval": 10, "bus_capacity": 40},
    ]

    print("🚌 Multi-Bus Queue Simulation Results\n")
    results = []
    for i, sc in enumerate(scenarios, start=1):
        res = simulate_bus_system(**sc, seed=42)
        res["Scenario"] = i
        results.append(res)
        print(f"\n--- Scenario {i} ---")
        pprint(res)
    
    return results

if __name__ == "__main__":
    run_scenarios()
