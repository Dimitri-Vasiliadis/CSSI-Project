from PIL import Image

png = Image.open("photo/instagram.png")
#print png.getdata()[200]

def getRed(pixel):
    return pixel[0]

def getGreen(pixel):
    return pixel[1]

def getBlue(pixel):
    return pixel[2]

def getAveragePixel(pixel):
    avg = (getRed(pixel) + getGreen(pixel) + getBlue(pixel)) / 3
    return avg

new_pixels = []
size = png.height * png.width
old_pixels = png.getdata()
for i in range(size):
    old_pixel = old_pixels[i]
    if(i % png.width > png.width / 2):
        new_pixel = getAveragePixel(old_pixel)
    else:
        new_pixel = old_pixel
    new_pixels.append(new_pixel)

#for pixel in png.getdata():
    #new_pixels.append(pixel)
    #red_value = getRed(pixel)
    #green_value = getGreen(pixel)
    #blue_value = getBlue(pixel)
    #new_pixel = (getAveragePixel(pixel), getAveragePixel(pixel), getAveragePixel(pixel))
    #new_pixels.append(new_pixel)

new_image = Image.new("RGB", png.size)
new_image.putdata(new_pixels)
new_image.show()
