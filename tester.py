from PIL import Image

try:
    original = Image.open("pic.png")
    print("OK")
except FileNotFoundError:
    print("Файл не найден")