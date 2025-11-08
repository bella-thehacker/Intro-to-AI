import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import datasets

print("All basic imports successful!")

data = np.array([[1, 2], [3, 4]])
print("NumPy array:\n", data)

try:
    import tensorflow as tf
    print(f"TensorFlow {tf.__version__} is installed!")
    print("GPU is available!" if tf.config.list_physical_devices('GPU') else "CPU only.")
except ImportError:
    print("TensorFlow not installed yet.")

print("🎉 Your environment is ready for AI!")
