import os
import math
import pandas as pd
import numpy as np
import base64
from PIL import Image
import io

def load_data(filepath):
    """Load CSV data into a DataFrame."""
    return pd.read_csv(filepath)

# load CSV data
data = pd.read_csv('data/dataset.csv', skiprows=1)

save_path = 'data/image_files/'
if not os.path.exists(save_path):
    os.makedirs(save_path)

# read dataset.csv data {lable, pixcels}
for index, row in data.iterrows():
    label = row.iloc[0]
    pixels = row.iloc[1].split(' ')
    pixels = list(map(int, pixels))
    
    # calculate image real sizes
    image_size = int(math.sqrt(len(pixels)))
    image_array = np.array(pixels, dtype=np.uint8).reshape((image_size, image_size))
    
    # creat image and save
    image = Image.fromarray(image_array)
    image.save(os.path.join(save_path, f'label_{label}_index_{index}.png'))