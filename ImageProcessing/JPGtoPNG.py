import sys
import os
from PIL import Image

jpg_folder = sys.argv[1]
png_folder = sys.argv[2]

if not os.path.exists(png_folder):
	os.makedirs(png_folder)

for i in os.listdir(jpg_folder):
	img = Image.open(fr'{jpg_folder}\{i}')
	img.save(fr'{png_folder}\{os.path.splitext(i)[0]}.png', 'png')