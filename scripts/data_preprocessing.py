import pandas as pd
import os

# بارگذاری داده‌های CSV
data = pd.read_csv('data/dataset.csv', skiprows=1)  # اگر سربرگ ندارید

# تعیین مسیر پوشه ریشه برای ذخیره فایل‌های CSV
root_save_path = 'data/train/'

# اطمینان از ایجاد پوشه ریشه اگر پیش‌تر ایجاد نشده است
if not os.path.exists(root_save_path):
    os.makedirs(root_save_path)

# گروه‌بندی داده‌ها بر اساس برچسب
grouped = data.groupby(data.columns[0])

# حلقه برای ذخیره هر گروه در فایل CSV جداگانه
for label, group in grouped:
    # تعیین مسیر پوشه برای ذخیره فایل‌های CSV بر اساس برچسب
    label_save_path = os.path.join(root_save_path, str(label))
    # اطمینان از ایجاد پوشه برچسب اگر پیش‌تر ایجاد نشده است
    if not os.path.exists(label_save_path):
        os.makedirs(label_save_path)
    
    # تعیین مسیر فایل CSV بر اساس برچسب و ذخیره آن
    csv_file_path = os.path.join(label_save_path, f'label_{label}.csv')
    group.to_csv(csv_file_path, header=False, index=False)
