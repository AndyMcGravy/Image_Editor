#this will hold the code that will resize the images

from PIL import Image 

#REMINDER TO SELF ---> PIL is the Python Imaging Library

#open image -> resize -> save image
def resize(image_path, output_path, width, height):
    try:
        #open image
        img = Image.open(image_path)
        #resize img to desired w and h
        img = img.resize((width, height))
        #save img to output_path
        img_format = img.format if img.format else 'PNG'  # Default to 'PNG' if format is None
        img.save(output_path, format=img_format)
        #print success message
        print("Image resized and save to", output_path)

    except Exception as e:
        print("Error resizing image:", e)
