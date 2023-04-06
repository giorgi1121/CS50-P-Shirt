#import modules
import sys
from PIL import Image, ImageOps
from os.path import splitext

#main function checks if file exists or not and resize, crop and makes new picture
def main():
    check_command_lines()
    try:
        #open shirt image
        shirt = Image.open("shirt.png")
        #define size of shirt image
        size = shirt.size
        #open input image
        image = Image.open(sys.argv[1])
        #resize input image
        image = ImageOps.fit(image, size)
        #paste shirt image in input image
        image.paste(shirt, shirt)
        #save image
        image.save(sys.argv[2])

    except FileNotFoundError:
        sys.exit("File does not exist")

#check command-line arguments
def check_command_lines():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    file1 = splitext(sys.argv[1])
    file2 = splitext(sys.argv[2])

    if extensions(file1[1]) != True:
        sys.exit("Invalid input")
    elif extensions(file2[1]) != True:
        sys.exit("Invalid output")

    if file1[1].lower() != file2[1].lower():
        sys.exit("Input and output have different extensions")

#check extensions
def extensions(file):
    extensions = [".jpg", ".jpeg", ".png"]
    if file in extensions:
        return True
    return False

main()
