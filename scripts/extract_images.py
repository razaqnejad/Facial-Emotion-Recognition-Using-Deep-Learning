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

# بارگذاری داده‌های CSV
data = pd.read_csv('data/dataset.csv', skiprows=1)

# تعیین مسیر پوشه برای ذخیره تصاویر
save_path = 'data/image_files/'

# اطمینان از ایجاد پوشه اگر پیش‌تر ایجاد نشده است
if not os.path.exists(save_path):
    os.makedirs(save_path)

# حلقه برای تبدیل رشته پیکسل‌ها به تصویر و ذخیره آن‌ها
for index, row in data.iterrows():
    # استخراج برچسب و پیکسل‌ها
    label = row.iloc[0]
    pixels = row.iloc[1].split(' ')  # فرض بر این است که پیکسل‌ها با فاصله جدا شده‌اند
    pixels = list(map(int, pixels))  # تبدیل پیکسل‌ها به اعداد صحیح
    
    # محاسبه ابعاد تصویر
    image_size = int(math.sqrt(len(pixels)))  # فرض بر این است که تصویر مربعی است
    image_array = np.array(pixels, dtype=np.uint8).reshape((image_size, image_size))
    
    # ایجاد تصویر و ذخیره آن
    image = Image.fromarray(image_array)
    image.save(os.path.join(save_path, f'label_{label}_index_{index}.png'))