import cv2
import numpy as np
import os
from PIL import Image

# مسیر پوشه‌ای که تصاویر در آن ذخیره شده‌اند
image_folder_path = 'path_to_your_images/'

# بارگذاری مدل پیش‌آموزش دیده برای تشخیص چهره
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# تابعی برای تشخیص وضوح چهره در تصویر
def detect_face_and_clarity(image_path):
    image = cv2.imread(image_path)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # تشخیص چهره‌ها
    faces = face_cascade.detectMultiScale(gray_image, 1.1, 4)
    
    if len(faces) == 0:
        return 0  # اگر چهره‌ای تشخیص داده نشد، وضوح را 0 درصد در نظر می‌گیریم
    
    # محاسبه مساحت کل تصویر
    total_area = image.shape[0] * image.shape[1]
    
    # محاسبه مساحت کل چهره‌های تشخیص داده شده
    face_area = sum((x2 - x) * (y2 - y) for x, y, x2, y2 in faces)
    
    # محاسبه درصد وضوح چهره بر اساس نسبت مساحت چهره به کل تصویر
    clarity_percentage = (face_area / total_area) * 100
    
    return clarity_percentage

# برای هر تصویر در پوشه، تشخیص وضوح چهره را انجام دهید و یک دیکشنری بسازید
clarity_dict = {}
for image_name in os.listdir(image_folder_path):
    image_path = os.path.join(image_folder_path, image_name)
    clarity_percentage = detect_face_and_clarity(image_path)
    clarity_dict[image_name] = clarity_percentage

# نمایش دیکشنری وضوح چهره
for image_name, clarity in clarity_dict.items():
    print(f"Image: {image_name}, Clarity: {clarity:.2f}%")
