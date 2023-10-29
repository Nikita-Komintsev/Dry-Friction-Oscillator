import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# Укажите путь к изображению
image_path = "2.png"

try:
    # Загрузка изображения с помощью Matplotlib
    img = mpimg.imread(image_path)

    # Отображение изображения
    plt.imshow(img)
    plt.axis('off')  # Отключение осей
    plt.show()

except FileNotFoundError:
    print(f"Изображение {image_path} не найдено.")
except Exception as e:
    print(f"Произошла ошибка при открытии изображения: {e}")
