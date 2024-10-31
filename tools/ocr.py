import pyperclip
from PIL import ImageGrab, Image
import pytesseract
import time

# Set up tesseract path if necessary
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Uncomment this line and add your path if needed

def capture_image_from_clipboard():
    """Attempts to capture an image from the clipboard."""
    image = ImageGrab.grabclipboard()
    if isinstance(image, Image.Image):
        return image
    return None

def perform_ocr(image):
    """Extracts text from an image using OCR."""
    return pytesseract.image_to_string(image)

def main():
    print("Paste an image with Ctrl+V to capture it.")
    
    # Allow some time for pasting after the script starts
#    time.sleep(2)

    # Capture image from clipboard
    image = capture_image_from_clipboard()

    if image:
        text = perform_ocr(image)
        print("Extracted Text:\n", text)
    else:
        print("No image found on clipboard. Please copy an image and try again.")

if __name__ == "__main__":
    main()
