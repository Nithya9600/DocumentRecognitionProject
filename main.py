import os
from recognition_module.utils import load_image
from recognition_module.document_recognition import recognize_document_type

# Test recognition on sample images
sample_folder = "test_data/sample_images/"
for filename in os.listdir(sample_folder):
    image_path = os.path.join(sample_folder, filename)
    image = load_image(image_path)
    document_type = recognize_document_type(image)
    print(f"Document: {filename}, Type: {document_type}")