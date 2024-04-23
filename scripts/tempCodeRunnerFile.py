image_array = np.array(pixels).reshape(image_size, image_size).astype(np.uint8)

    # تبدیل آرایه به تصویر
    image = Image.fromarray(image_array)

    # ذخیره تصویر در پوشه با نامی شامل برچسب و شماره ردیف
    image.save(f'{save_path}/image_{label}_{idx}.png')