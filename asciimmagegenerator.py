import os
import sys
import time
from PIL import Image
import cv2
from blessed import Terminal
from colorama import init

term = Terminal()

name = 1

DEFAULT_CHARSET = "@#$%&*()0!=-.,"
IMG_SIZE = (0, 0)
imgs = []

def get_terminal_size():
    return os.get_terminal_size()

frame_index = 1  # global counter outside the function

def print_img(image):
    global frame_index

    img = image.resize(IMG_SIZE, Image.Resampling.LANCZOS)
    gimg = img.convert('L')
    pixels = list(gimg.getdata())

    output_string = ""

    for i, pixel in enumerate(pixels):
        if i % IMG_SIZE[0] == 0 and i != 0:
            output_string += "\n"

        ind = int(pixel / 255 * (len(DEFAULT_CHARSET) - 1))
        char = DEFAULT_CHARSET[ind]
        output_string += char    # Ensure the ASCII art ends with a newline
    output_string += "\n"
    # Save the full ASCII art frame to a text file
    with open(f"frame_{frame_index}.txt", "w") as f:
        f.write(output_string)

    frame_index += 1

    # Display in terminal
    with term.hidden_cursor():
        sys.stdout.write(term.home + output_string)
        sys.stdout.flush()

        
def open_image(file):
    try:
        return Image.open(file)
    except Exception as e:
        print(f"Error: Unable to open image file {file}. {e}")
        return None

def open_video(file):
    vid = cv2.VideoCapture(file)
    if not vid.isOpened():
        print(f"Error: Unable to open video file {file}.")
        return

    while True:
        ret, img = vid.read()
        if not ret:
            break
        conv = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        imgs.append(Image.fromarray(conv))

    vid.release()

def main():
    global IMG_SIZE, DEFAULT_CHARSET

    IMG_SIZE = get_terminal_size()

    if len(sys.argv) < 2:
        print("No file provided. Please provide an image or video file as an argument.")
        return

    file_path = sys.argv[1]
    ext = file_path.split('.')[-1].lower()

    if ext in ["mp4", "avi", "mov", "gif"]:
        open_video(file_path)
    else:
        img = open_image(file_path)
        if img:
            imgs.append(img)

    for arg in sys.argv[2:]:
        if arg == "-f":
            DEFAULT_CHARSET = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~<>i!lI;:,^`'."

    for img in imgs:
        print_img(img)
        time.sleep(0.033)  # ~30fps

if __name__ == "__main__":
    main()
