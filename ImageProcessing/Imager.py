from PIL import Image, ImageFilter

img = Image.open(r'.\Images\Car.jpg')

#print(img)
#print(img.mode)
#print(img.size)
#print(img.histogram)
#print(dir(img))

new_Car = img.filter(ImageFilter.BLUR)
#new_Car.save('BlurredCar.png', 'png')

new_Car = img.convert('L')
#new_Car.save('GreyCar.png', 'png')
#print(new_Car.mode)

img = Image.open(r'.\Images\Moon.jpg')
new_Moon = img.filter(ImageFilter.BLUR)
new_Moon.save('BlurredMoon.png', 'png')
#print(img.size)

#print(new_Moon.size)
#new_Moon.thumbnail((400,200))
#print(new_Moon.size)



