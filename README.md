# 🚌 Multi-Bus Queue Simulation

### 👤 Author
**Biswajit (2025)**

---

### 🎯 Overview
This project simulates a **university shuttle system** using **discrete-event simulation**.  
Students arrive randomly, buses come at fixed intervals, and each bus has limited capacity.

It calculates:
- Average waiting time per student
- Maximum queue length
- Leftover students
- Bus seat utilization

---

### ⚙️ Features
✅ Event-driven simulation  
✅ Adjustable parameters  
✅ Multiple scenario comparison  
✅ Simple Python implementation (works on Google Colab)

---

### 🧮 Example Parameters

| Parameter | Description | Example |
|------------|--------------|----------|
| `sim_time` | Total run time (minutes) | 120 |
| `mean_interarrival` | Avg time between student arrivals | 1.5 |
| `bus_interval` | Time between bus arrivals | 10 |
| `bus_capacity` | Number of seats per bus | 30 |

---

### 📊 Sample Output
```
--- Scenario 1 ---
Simulation time: 120
Bus interval: 10
Bus capacity: 30
Total arrivals: 85
Total served: 80
Leftover: 5
Average waiting time: 4.2 min
Bus utilization: 0.89
```

---

### 🧰 How to Run
#### 🔹 Option 1: Google Colab
1. Open [Google Colab](https://colab.research.google.com/)
2. Upload `main.py`
3. Run all cells

#### 🔹 Option 2: Local (VS Code / Terminal)
```bash
git clone https://github.com/<your-username>/multi-bus-queue-simulation.git
cd multi-bus-queue-simulation
python main.py
```

---

### 📜 License
MIT License © 2025 Biswajit
