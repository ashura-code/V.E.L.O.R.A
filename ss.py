from PIL import ImageGrab
import random
def take_screenshot():
    # Take a screenshot of the entire screen
    image = ImageGrab.grab()
    filename = f"screenshot_{random.randint(1, 100)}.png"
    # Save the screenshot to the specified filename
    image.save(filename)
    print(f"Screenshot saved as {filename}")

# Example usage
take_screenshot()
