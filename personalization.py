import ctypes
import datetime


# Function to set the desktop background image
def set_wallpaper(image_path):
    # Load the user32 library
    user32 = ctypes.WinDLL("user32.dll")

    # Set the wallpaper
    result = user32.SystemParametersInfoW(20, 0, image_path, 3)

    if result:
        print(f"Desktop background set successfully. Image: {image_path}")
    else:
        print("Failed to set desktop background.")


# Get the current time
current_time = datetime.datetime.now().time()

# Determine the image path based on the current time
if current_time < datetime.time(12):
    image_path = "C:/Users/sriva/Downloads/emma-simpson-mNGaaLeWEp0-unsplash.jpg"
elif current_time < datetime.time(18):
    image_path = "C:/Users/sriva/Downloads/pngwing.com.png"
else:
    image_path = "C:/Users/sriva/Desktop/pic/pics.jpg"

# Set the wallpaper
set_wallpaper(image_path)
