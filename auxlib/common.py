import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import matplotlib.gridspec as gridspec
import random
import os
import time

import keras
from keras.models import Sequential
from keras.models import load_model as keras_load_model
from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout, Conv2DTranspose

import h5py
from tqdm import tqdm
from datetime import datetime


from scipy.optimize import curve_fit

def common_utility_function():
    print("This is a utility function shared across modules.")