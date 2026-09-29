# Day 19 - Min Stack

## 📌 Overview

A futuristic monitoring vault receives temperature readings every second.

The goal of this project is to build a custom Min Stack that supports:

- Push
- Pop
- Get Minimum

The important requirement is that the minimum temperature must be
retrieved in O(1) time.

---

## 🎯 Objective

Build a stack that can:

1. Add a temperature reading
2. Remove the latest temperature
3. Instantly return the minimum temperature recorded so far

---

## 🧠 Approach

A normal stack cannot return the minimum value in O(1) time
unless additional information is maintained.

Therefore, this implementation uses two stacks.

### Main Stack

Stores all temperature readings.

### Minimum Stack

Stores the minimum value at every stack level.

Example:

Temperature values:

24, 18, 30, 12, 20

Main Stack:

[24, 18, 30, 12, 20]

Minimum Stack:

[24, 18, 18, 12, 12]

The top of the Minimum Stack always contains
the current minimum temperature.

---

## 🔄 Operations

### Push

Add the temperature to the main stack.

Also add the current minimum to the minimum stack.

### Pop

Remove the top element from both stacks.

### GetMin

Return the top element of the minimum stack.

No loop is required.

---

## 🧪 Example

Input:

24 18 30 12 20

Operations:

Push 24
Push 18
Push 30
Push 12
Push 20

Current minimum:

12°C

---

## 🌍 Real-World Impact

Efficient minimum-value tracking can be useful in:

- Temperature monitoring
- Cloud infrastructure monitoring
- Financial systems
- Monitoring dashboards
- Sensor systems
- Performance tracking

---

## ⏱️ Complexity

| Operation | Time |
|-----------|------|
| Push | O(1) |
| Pop | O(1) |
| GetMin | O(1) |

Space Complexity:

O(n)

---

## 🧪 Random Testing

The program also generates random temperature values
to test the Min Stack with different inputs.

---

## ▶️ How to Run

Open the VS Code terminal:

python day19_min_stack.py

---

## 📂 Project Structure

day19/
│
├── day19_min_stack.py
└── README.md

---

## 🚀 Learning Outcome

Through this project, I learned:

- Custom data structures
- Stack implementation
- Two-stack technique
- O(1) minimum lookup
- Push and pop operations
- Edge-case handling
- Random testing
- Time and space complexity
