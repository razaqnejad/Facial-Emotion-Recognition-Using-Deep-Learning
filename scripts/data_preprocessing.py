import pandas as pd
import numpy as np

def load_data(filepath):
    """Load CSV data into a DataFrame."""
    return pd.read_csv(filepath)

def clean_data(df):
    """Perform data cleaning tasks like removing missing values and unnecessary columns."""
    # اینجا کدهای مربوط به پاک‌سازی داده‌ها را اضافه کنید
    return df

# مسیر فایل داده‌های خام
file_path = 'data/dataset.csv'

# بارگذاری و پیش‌پردازش داده‌ها
data = load_data(file_path)
data = clean_data(data)

# ذخیره داده‌های پیش‌پردازش شده در یک فایل جدید
data.to_csv('data/cleaned_data.csv', index=False)

def show_encoded_image(data):
    # دیکد کردن رشته base64 به بایت‌های تصویر
    image_data = base64.b64decode(data)
    image = Image.open(io.BytesIO(image_data))
    image.show()

# یا اگر مسیر تصویر داخل فایل CSV ذخیره شده است:
def show_image_from_path(image_path):
    image = Image.open(image_path)
    image.show()

# نمایش اولین تصویر
if 'image_data' in data.columns:
    show_encoded_image(data['image_data'][0])
elif 'image_path' in data.columns:
    show_image_from_path(data['image_path'][0])
