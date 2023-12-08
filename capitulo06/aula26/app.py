from PIL import Image
from pathlib import Path

ROOT_FOLDER = Path(__file__).parent
IMAGE = ROOT_FOLDER / "aurora-wallpaper.jpg"
NEW_IMAGE = ROOT_FOLDER / "new-aurora-wallpaper.jpg"

pil_image = Image.open(IMAGE)
width, height = pil_image.size
exif = pil_image.getexif()

new_width = 640
new_height = round(height * new_width / width)
new_image = pil_image.resize(size=(new_width, new_height))
new_image.save(NEW_IMAGE, optimize=True, quality=100, exif=exif)
