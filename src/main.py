import image_editor.image_resize as imgedit
import gui.user_interfaces as user_interfaces
import argparse
#REMINDER TO SELF --> argparse is a module that will allow us to pass arguments to the script


#trying to figure out what order to do things in...

##test argparse example from internet
# parser = argparse.ArgumentParser()
# parser.add_argument("echo", help="echo the string you use here")  #note that name of the arg matches the method it is describing
# args = parser.parse_args()
# print(args.echo)

# argparse to take in the image path and output path
parser = argparse.ArgumentParser()
args = parser.parse_args()

if parser.add_argument("-r", "-resize", action="store_true", help="Resize the image") == True:
    parser.add_argument("image_path", help="path to the image to be resized")
    parser.add_argument("output_path", help="path to save the resized image")
    parser.add_argument("width", type=int, help="width of the resized image")
    parser.add_argument("height", type=int, help="height of the resized image")
    imgedit.resize(args.image_path, args.output_path, args.width, args.height) #uncomment this line to test the image resizing function via CLI

else:
    print("no arguments provided, running GUI now")

def main():
    # Call the GUI function
    user_interfaces.resize_gui()

    # print("Image path:", gui.image_path.get()) #uncomment this line to test the image path input
    # print("Output path:", gui.output_path.get()) #output path input test
    # print("Width:", gui.width.get()) #width test
    # print("Height:", gui.height.get()) # height test

    imgedit.resize(user_interfaces.image_path.get(), user_interfaces.output_path.get(), user_interfaces.width.get(), user_interfaces.height.get())


main()