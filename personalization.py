import ctypes


# Function to set the desktop background image
def set_wallpaper(image_path):
    # Load the user32 library
    user32 = ctypes.WinDLL("user32.dll")

    # Set the wallpaper
    result = user32.SystemParametersInfoW(20, 0, image_path, 3)

    if result:
        print("Desktop background set successfully.")
    else:
        print("Failed to set desktop background.")


# Example usage
image_path = "C:/Users/sriva/Desktop/pics.jpg"
set_wallpaper(image_path)
