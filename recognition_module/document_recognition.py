import cv2
import pytesseract

def recognize_document_type(image):
    # Preprocess the image (grayscale, thresholding)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, binary = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

    # Perform OCR on the processed image
    ocr_result = pytesseract.image_to_string(binary)

    # Check for keywords to determine the document type
    if "INCOME TAX DEPARTMENT" in ocr_result.upper():
        return "PAN Card"
    elif "PASSPORT" in ocr_result.upper():
        return "Passport"
    elif "INVOICE" in ocr_result.upper():
        return "Invoice"
    else:
        return "Unknown Document Type"