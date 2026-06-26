import random
import time

# Generate a random number between 3 and 35 (inclusive)
# random_seconds = random.randint(3, 35)

# Alternative: if you want floating point numbers (e.g., 3.5, 27.8)
random_seconds = random.uniform(3, 35)

print(f"Random number: {random_seconds} seconds")

# Optional: wait that many seconds
print(f"Waiting for {random_seconds} seconds...")
time.sleep(random_seconds)
print("Done waiting!")