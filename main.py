import argparse
import os 
import sys

from src.inference import run

def main():
    parser = argparse.ArgumentParser(description="Convert tabular images to csvs")

    # defining arguments
    parser.add_argument(
        '--image',
        type=str,
        required=True,
        dest='image', 
        help='image path',
    )

    # parsing the arguments
    args = parser.parse_args()

    # if image is not present
    if not os.path.isfile(args.image):
        sys.stderr.write("File not found\n")
        sys.exit()

    # running inference
    if run(args.image):
        sys.stdout.write("Completed\n")
    else:
        sys.stderr.write("Failed to execute\n")

    
if __name__ == "__main__":
    main()