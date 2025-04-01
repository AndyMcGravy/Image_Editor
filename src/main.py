import image_editor as imgedit
import argparse

#REMINDER TO SELF --> argparse is a module that will allow us to pass arguments to the script


#trying to figure out what order to do things in...

##test argparse example from internet
# parser = argparse.ArgumentParser()
# parser.add_argument("echo", help="echo the string you use here")  #note that name of the arg matches the method it is describing
# args = parser.parse_args()
# print(args.echo)

#argparse to take in the image path and output path
parser = argparse.ArgumentParser()
parser.add_argument("image_path", help="path to the image to be resized")
parser.add_argument("output_path", help="path to save the resized image")
parser.add_argument("width", type=int, help="width of the resized image")
parser.add_argument("height", type=int, help="height of the resized image")
args = parser.parse_args()

imgedit.resize(args.image_path, args.output_path, args.width, args.height)