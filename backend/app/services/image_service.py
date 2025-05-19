import os
import cv2
import numpy as np
import tensorflow as tf

"""
Модуль наложения мультяшного стиля на изображения.
"""

model_path = os.path.join(os.path.dirname(__file__), 'weights', 'munchkinGAN.tflite')

if not os.path.isfile(model_path):
    raise FileNotFoundError(f"По пути {model_path} не найдены веса модели.")

# Загрузка модели
modelGAN = tf.lite.Interpreter(model_path=model_path)
modelGAN.allocate_tensors()
ind = modelGAN.get_input_details()
index = ind[0]['index']


def load_image(image_path):
    """
    Загружает и нормализует изображение.

    Аргументы:
        image_path (str): Путь к изображению.

    Возвращает:
        Tensor: Нормализованное изображение с диапазоном [-1, 1],
        расширенное до батч-формата (1, H, W, 3).
    """

    image = cv2.imread(image_path)  # Загружаем изображение в формате BGR
    image = image.astype(np.float32) / 127.5 - 1  # Нормализация: [0,255] → [-1,1]
    image = np.expand_dims(image, 0)  # Добавляем размер батча
    image = tf.convert_to_tensor(image)  # Преобразуем в TensorFlow tensor

    return image


def resize_image(image, img_size=512):
    """
    Масштабирует изображение.

    Аргументы:
        image (Tensor): Изображение (1, H, W, 3).
        img_size (int): Целевой размер выходного изображения (ширина и высота).

    Возвращает:
        Tensor: Изображение размера (1, img_size, img_size, 3).
    """

    img_shape = tf.cast(tf.shape(image)[1:-1], tf.float32)
    short_side = min(img_shape)
    scale = img_size / short_side  # Масштаб по короткой стороне
    new_shape = tf.cast(img_shape * scale, tf.int32)  # Новые размеры с сохранением пропорций

    image = tf.image.resize(image, new_shape)  # Масштабируем изображение
    image = tf.image.resize_with_crop_or_pad(image, img_size, img_size)  # Центрированная обрезка

    return image


def apply_munchkin_style(image_path, styled_image_path=None):
    """
    Применяет стиль рисовки манчкина к изображению и сохраняет полученное изображение.

    Аргументы:
        image_path (str): Путь к изображению.
        Должен быть на английском, без пробелов, в формате jpg или png
        styled_image_path (str): Путь для сохранения стилизованного изображения.

    Возвращает:
        str: Путь, по которому сохранилось стилизованное изображение.
    """

    # Формирование пути до изменённого изображения
    if not styled_image_path:
        directory = os.path.dirname(image_path)
        filename = os.path.basename(image_path)

        styled_image_path = os.path.join(directory, f"munchkin_{filename}")

    # Загрузка и предварительная обработка изображения
    image = load_image(image_path)
    image = resize_image(image, img_size=512)  # Приводим изображение к размеру 512x512, т.к. с ним работает модель

    # Загрузка изображения в модель
    modelGAN.set_tensor(index, image)
    modelGAN.invoke()

    # Получаем выход в формате списка списков
    result = modelGAN.tensor(modelGAN.get_output_details()[0]['index'])()

    # Постобработка
    output_image = (np.squeeze(result) + 1.0) * 127.5  # Возвращаем к диапазону [0, 255]
    output_image = np.clip(output_image, 0, 255).astype(np.uint8)

    # Сохранение
    if not cv2.imwrite(styled_image_path, output_image):
        raise RuntimeError(f"Не удалось сохранить изображение по пути: {styled_image_path}")

    return styled_image_path
