from PIL import Image
# Rename this file to be "filters.py"
# Add commands to import modules here.

# Define your load_img() function here.
#       Parameters: The name of the file to be opened (string)
#       Returns: The image object with the opened file.
def load_img(filename):
    return Image.open(filename)

# Define your show_img() function here.
#       Parameters: The image object to display.
#       Returns: nothing.
def show_img(im):
    im.show()

# Define your save_img() function here.
#       Parameters: The image object to save, the name to save the file as (string)
#       Returns: nothing.
def save_img(im,filename):
    im.save(filename)

# Define your obamicon() function here.
#       Parameters: The image object to apply the filter to.
#       Returns: A New Image object with the filter applied.

def bluetint(im):
    filtered_image = Image.new("RGB", im.size)
    original_pixels = im.getdata()
    filtered_pixels = []

    for pixel in original_pixels:
        red = pixel[0]
        green = pixel[1]
        blue = pixel [2]
        intensity =  pixel[0] + pixel[1] + pixel[2]

        newblue = (red, green, blue + 100)
        filtered_pixels.append(newblue)

    filtered_image.putdata(filtered_pixels)
    return filtered_image


def pinktint(im):
    filtered_image = Image.new("RGB", im.size)
    original_pixels = im.getdata()
    filtered_pixels = []

    for pixel in original_pixels:
        red = pixel[0]
        green = pixel[1]
        blue = pixel [2]
        intensity =  pixel[0] + pixel[1] + pixel[2]

        newpink = (red + 100, green, blue)
        filtered_pixels.append(newpink)

    filtered_image.putdata(filtered_pixels)
    return filtered_image


def redtint(im):
    filtered_image = Image.new("RGB", im.size)
    original_pixels = im.getdata()
    filtered_pixels = []

    for pixel in original_pixels:
        red = pixel[0]
        green = pixel[1]
        blue = pixel [2]
        intensity =  pixel[0] + pixel[1] + pixel[2]

        newred = (red + 200, green, blue)
        filtered_pixels.append(newred)

    filtered_image.putdata(filtered_pixels)
    return filtered_image


def yellowtint(im):
    filtered_image = Image.new("RGB", im.size)
    original_pixels = im.getdata()
    filtered_pixels = []

    for pixel in original_pixels:
        red = pixel[0]
        green = pixel[1]
        blue = pixel [2]
        intensity =  pixel[0] + pixel[1] + pixel[2]

        newyellow = (red + 100, green + 100, blue)
        filtered_pixels.append(newyellow)

    filtered_image.putdata(filtered_pixels)
    return filtered_image


def negativefilter(im):
    filtered_image = Image.new("RGB", im.size)
    original_pixels = im.getdata()
    filtered_pixels = []

    for pixel in original_pixels:
        red = pixel[0]
        green = pixel[1]
        blue = pixel [2]
        intensity =  pixel[0] + pixel[1] + pixel[2]

        negativefilter = (255 - red, 255 - green, 255 - blue)
        filtered_pixels.append(negativefilter)

    filtered_image.putdata(filtered_pixels)
    return filtered_image


def grayscale(im):
    filtered_image = Image.new("RGB", im.size)
    original_pixels = im.getdata()
    filtered_pixels = []

    for pixel in original_pixels:
        intensity =  pixel[0] + pixel[1] + pixel[2]
        newintensity = (intensity//3, intensity//3, intensity//3)
        filtered_pixels.append(newintensity)

    filtered_image.putdata(filtered_pixels)
    return filtered_image


def darken(im):
    filtered_image = Image.new("RGB", im.size)
    original_pixels = im.getdata()
    filtered_pixels = []

    for pixel in original_pixels:
        red = pixel[0]
        green = pixel[1]
        blue = pixel [2]
        intensity =  pixel[0] + pixel[1] + pixel[2]

        darken = (red - 100, green - 100, blue - 100)
        filtered_pixels.append(darken)

    filtered_image.putdata(filtered_pixels)
    return filtered_image


def whiten(im):
    filtered_image = Image.new("RGB", im.size)
    original_pixels = im.getdata()
    filtered_pixels = []

    for pixel in original_pixels:
        red = pixel[0]
        green = pixel[1]
        blue = pixel [2]
        intensity =  pixel[0] + pixel[1] + pixel[2]

        whiten = (red + 100, green + 100, blue + 100)
        filtered_pixels.append(whiten)

    filtered_image.putdata(filtered_pixels)
    return filtered_image


def galaxy(im):
    filtered_image = Image.new("RGB", im.size)
    original_pixels = im.getdata()
    filtered_pixels = []

    for pixel in original_pixels:
        red = pixel[0]
        green = pixel[1]
        blue = pixel [2]
        intensity =  pixel[0] + pixel[1] + pixel[2]

        galaxy = (red, green + 100, blue + 100)
        filtered_pixels.append(galaxy)

    filtered_image.putdata(filtered_pixels)
    return filtered_image


def obamicon(im):
    filtered_image = Image.new("RGB", im.size)
    original_pixels = im.getdata()
    filtered_pixels = []

    darkBlue = (0, 51, 76)
    red = (217, 26, 33)
    lightBlue = (112, 150, 158)
    yellow = (252, 227, 166)

    for pixel in original_pixels:
        intensity = pixel[0] + pixel[1] + pixel[2]

        if intensity < 182:
            filtered_pixels.append(darkBlue)
        elif intensity <= 364:
            filtered_pixels.append(red)
        elif intensity <= 546:
            filtered_pixels.append(lightBlue)
        else:
            filtered_pixels.append(yellow)

    filtered_image.putdata(filtered_pixels)
    return filtered_image


def redonly(im):
    filtered_image = Image.new("RGB", im.size)
    original_pixels = im.getdata()
    filtered_pixels = []

    for pixel in original_pixels:
        intensity = pixel[0] + pixel[1] + pixel[2]
        grey = (intensity//3, intensity//3, intensity//3)
        red = pixel[0]
        green = pixel[1]
        blue = pixel[2]
        addred = (red + 90, green, blue)

        if red > 160:
            filtered_pixels.append(addred)
        elif green > 1:
            filtered_pixels.append(grey)
        elif blue > 1:
            filtered_pixels.append(grey)
        else:
            filtered_pixels.append(grey)

    filtered_image.putdata(filtered_pixels)
    return filtered_image


def shadesofgrey(im):
    filtered_image = Image.new("RGB", im.size)
    original_pixels = im.getdata()
    filtered_pixels = []

    white = (255, 255, 255)
    lightgrey = (211, 211, 211)
    darkgrey = (169, 169, 169)
    black = (0, 0, 0)

    for pixel in original_pixels:
        intensity = pixel[0] + pixel[1] + pixel[2]
        grey = (intensity//3, intensity//3, intensity//3)

        if intensity < 182:
            filtered_pixels.append(white)

        elif intensity <= 364:
            filtered_pixels.append(lightgrey)

        elif intensity <= 455:
            filtered_pixels.append(grey)

        elif intensity <= 546:
            filtered_pixels.append(darkgrey)

        else:
            filtered_pixels.append(black)

    filtered_image.putdata(filtered_pixels)
    return filtered_image


def revshadesofgrey(im):
    filtered_image = Image.new("RGB", im.size)
    original_pixels = im.getdata()
    filtered_pixels = []

    white = (255, 255, 255)
    lightgrey = (211, 211, 211)
    darkgrey = (169, 169, 169)
    black = (0, 0, 0)

    for pixel in original_pixels:
        intensity = pixel[0] + pixel[1] + pixel[2]
        grey = (intensity//3, intensity//3, intensity//3)

        if intensity < 182:
            filtered_pixels.append(black)

        elif intensity <= 364:
            filtered_pixels.append(darkgrey)

        elif intensity <= 455:
            filtered_pixels.append(grey)

        elif intensity <= 546:
            filtered_pixels.append(lightgrey)

        else:
            filtered_pixels.append(white)

    filtered_image.putdata(filtered_pixels)
    return filtered_image
