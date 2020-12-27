import io
from google.cloud import vision
from google.cloud.vision_v1 import types
from PIL import ImageGrab, Image


def get_clipboard_image():
    im = ImageGrab.grabclipboard()
    if isinstance(im, Image.Image):
        return im
    if isinstance(im, list):
        return Image.open(im[0])
    raise Exception("No image data in clipboard")


# getting image from clipboard
im = get_clipboard_image()
# google vision client
client = vision.ImageAnnotatorClient()

# loading clipboard to byte array
imgByteArr = io.BytesIO()
im.save(imgByteArr, "PNG")

# passing image to Google Vision
image = types.Image(content=imgByteArr.getvalue())
response = client.document_text_detection(image=image)

# retrieving response
texts = response.text_annotations
if texts:
    description = texts[0].description
    print(description)
