# 🚌 Multi-Bus Queue Simulation (Colab Edition)

### 👤 Author
**Biswajit (2025)**

---

## 🎯 Overview
This project demonstrates a **simulation + animation** of a university shuttle system using **Python in Google Colab**.  
It visually represents how students queue for a bus, how the bus arrives, boards up to capacity, and departs — all within a short 3–4 second MP4 video.

---

## ⚙️ Features
- Simulates **bus movement** and **student queueing**
- Implements **simple math** for arrivals, boarding, and departures  
- Generates a **3–4 second MP4 animation** in real time  
- Fully runnable on **Google Colab**

---

## 🧠 Core Logic
| Concept | Description |
|----------|--------------|
| **Entity** | Student |
| **Resource** | Bus |
| **Queue Discipline** | FCFS (First-Come, First-Served) |
| **Capacity** | 5 students per bus |
| **Events** | Arrival → Boarding → Departure |

---

## 📜 How It Works
1. A queue of 12 students waits for the bus.  
2. The bus enters the scene, boards up to 5 students (its capacity).  
3. Remaining students stay in the queue.  
4. The bus exits while showing live stats (time, queue length, boarded count).  

---

## 🧮 Mathematical Logic
- **Bus position (x)** is interpolated using a normalized timeline `t ∈ [0, 1]`.  
- **Boarding rate:**  
  \[
  \text{Boarded} = \min(C, \lfloor P_{\text{board}} \times (C+1)\rfloor)
  \]
  where \( P_{\text{board}} \) is progress between arrival and departure.  
- **Queue size:**  
  \[
  Q = \max(0, \text{Total} - \text{Boarded})
  \]

---

## 🧰 Run on Google Colab

### Step 1. Install dependencies
```python
!pip install imageio imageio-ffmpeg matplotlib --quiet
