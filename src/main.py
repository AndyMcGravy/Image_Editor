import resize
import argparse as ap

#REMINDER TO SELF --> argparse is a module that will allow us to pass arguments to the script


#trying to figure out what order to do things in...



#function to take in the arguments

def get_args():
    parser = ap.ArgumentParser(description="Resize images")
    parser.add_argument("input image path", description="The image to edit")
    parser.add_argument("output image path", description="The path to save the edited image to")