import os

# Define the nested directory structure
structure = [
    "cosmological",
    "cosmological/neuroscientific", 
    "cosmological/neuroscientific/fundamental_physics",
    "cosmological/neuroscientific/fundamental_physics/statistical",
    "cosmological/neuroscientific/fundamental_physics/statistical/containers"
]

# Create directories
for directory in structure:
    os.makedirs(directory, exist_ok=True)
    print(f"Created: {directory}")

print("Directory structure created successfully!")
