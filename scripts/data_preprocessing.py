import pandas as pd
import os

# load CSV file
data = pd.read_csv('data/dataset.csv', skiprows=1)

# create destination directory
root_save_path = 'data/train/'
if not os.path.exists(root_save_path):
    os.makedirs(root_save_path)

# group images by lable
grouped = data.groupby(data.columns[0])

# extract and save data by in defferent directories
for label, group in grouped:
    label_save_path = os.path.join(root_save_path, str(label))
    if not os.path.exists(label_save_path):
        os.makedirs(label_save_path)
    csv_file_path = os.path.join(label_save_path, f'label_{label}.csv')
    group.to_csv(csv_file_path, header=False, index=False)
