# Day 19 - Custom Data Structures
# Min Stack
# Supports push, pop and getMin in O(1)

import random


class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, value):
        self.stack.append(value)

        # Store the minimum value seen so far
        if not self.min_stack or value <= self.min_stack[-1]:
            self.min_stack.append(value)
        else:
            self.min_stack.append(self.min_stack[-1])

    def pop(self):
        if not self.stack:
            print("Stack is empty.")
            return None

        self.min_stack.pop()
        return self.stack.pop()

    def get_min(self):
        if not self.stack:
            return None

        return self.min_stack[-1]

    def display(self):
        print("Temperature Stack:", self.stack)
        print("Minimum Stack:", self.min_stack)


# -----------------------------
# Main Program
# -----------------------------

print("=== Temperature Min Stack ===")

min_stack = MinStack()

temperatures = [24, 18, 30, 12, 20, 9, 15]

print("\nAdding temperature readings:")

for temperature in temperatures:
    min_stack.push(temperature)
    print(
        f"Push: {temperature}°C | "
        f"Current Minimum: {min_stack.get_min()}°C"
    )

print("\nStack State:")
min_stack.display()

print("\nPopping values:")

while min_stack.stack:
    removed = min_stack.pop()

    if min_stack.stack:
        print(
            f"Pop: {removed}°C | "
            f"Current Minimum: {min_stack.get_min()}°C"
        )
    else:
        print(f"Pop: {removed}°C | Stack is empty.")


# -----------------------------
# Random Input Test
# -----------------------------

print("\n=== Random Temperature Test ===")

random_stack = MinStack()

random_temperatures = [
    random.randint(-10, 45)
    for _ in range(10)
]

print("Random readings:")
print(random_temperatures)

for temperature in random_temperatures:
    random_stack.push(temperature)

print("Minimum temperature:", random_stack.get_min(), "°C")