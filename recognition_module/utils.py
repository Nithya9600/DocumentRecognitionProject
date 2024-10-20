import pytesseract

# Specify the path to the Tesseract executable if necessary
# For Windows, it might look like: r"C:\Program Files\Tesseract-OCR\tesseract.exe"
pytesseract.pytesseract.tesseract_cmd = r"/path/to/tesseract"
import cv2
from PIL import Image
from PyPDF2 import PdfFileReader
import io

def load_image(image_path):
    return cv2.imread(image_path)

def load_pdf_as_image(pdf_path):
    images = []
    with open(pdf_path, "rb") as f:
        pdf = PdfFileReader(f)
        for page_num in range(pdf.getNumPages()):
            # Convert each PDF page to an image (use libraries like pdf2image)
            pass
    return images