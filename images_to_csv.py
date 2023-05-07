import pytesseract
from PIL import Image # pip install Pillow
import os
# set tesseract cmd to the be the path to your tesseract engine executable 
# (where you installed tesseract from above urls)

# IMPORTANT: this should end with '...\tesseract.exe'
pytesseract.pytesseract.tesseract_cmd = 'C:\Program Files\Tesseract-OCR\\tesseract.exe'

# and start doing it

images_dir = "image"
child_images = os.listdir(images_dir)
tmp = []
for child_image in child_images:
  tmp.append(os.path.join(images_dir, child_image))

list_with_many_images = tmp
# your saved images on desktop
# list_with_many_images = [
#   "image/image (1).jpeg"
# ]

# create a function that returns the text
def image_to_str(path):
    """ return a string from image """
    # return pytesseract.image_to_string(Image.open(path))
    
    print(pytesseract.image_to_boxes(path))

for i, image_path in enumerate(list_with_many_images):

  # now pure action + csv part
  with open("images_content" + str(i) + ".csv", "w+", encoding="utf-8") as file:
    file.write("ImagePath, ImageText")
    for image_path in list_with_many_images:
      image_to_str(image_path)
      # line = f"{image_path}, {text}\n"
      # file.write(line)