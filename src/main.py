import resize
import argparse as ap

#REMINDER TO SELF --> argparse is a module that will allow us to pass arguments to the script


#trying to figure out what order to do things in...



#function to take in the arguments

def get_args():
    parser = ap.ArgumentParser(description="Resize images")
    parser.add_argument("input image path", description="The image to edit")
    parser.add_argument("output image path", description="The path to save the edited image to")
    parser.add_argument("x", description="The x dimension to resize the image to")
    parser.add_argument("y", description="The y dimension to resize the image to")
    return parser.parse_args()

