import cv2
import numpy as np
import time

import easyocr
import torch

from constants import CROP_LOCATIONS


print("CUDA available:", torch.cuda.is_available())
print("CUDA device count:", torch.cuda.device_count())
print("Device name:", torch.cuda.get_device_name(0) if torch.cuda.is_available() else "No GPU")



def crop_region(image_input, x, y, w, h):
    if isinstance(image_input, str):
        image = cv2.imread(image_input)
    elif isinstance(image_input, np.ndarray):
        image = image_input
    else:
        raise TypeError("image_input must be a filepath (str) or a numpy.ndarray")
    
    cropped = image[y:y+h, x:x+w]
    return cropped

def preprocess_image(image_input):
    if isinstance(image_input, str):
        image = cv2.imread(image_input)
    elif isinstance(image_input, np.ndarray):
        image = image_input
    else:
        raise TypeError("image_input must be a filepath (str) or a numpy.ndarray")
    
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Optional: increase contrast or sharpen
    blur = cv2.GaussianBlur(gray, (3, 3), 0)
    thresh = cv2.adaptiveThreshold(blur, 255,
                                    cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                    cv2.THRESH_BINARY_INV, 11, 2)
    return thresh

def enhance_contrast(image):
    """Apply CLAHE to enhance local contrast."""
    lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
    l, a, b = cv2.split(lab)

    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    cl = clahe.apply(l)

    merged = cv2.merge((cl, a, b))
    result = cv2.cvtColor(merged, cv2.COLOR_LAB2BGR)
    return result

def denoise_image(image):
    """Apply bilateral filter for edge-preserving denoising."""
    return cv2.bilateralFilter(image, d=9, sigmaColor=75, sigmaSpace=75)

def run_easyocr_on_image(image_path, use_gpu=True, preprocess=False, denoise=False, enhance_contrast=False, crop_loc=None):
    image_input = image_path
    reader = easyocr.Reader(['en'], gpu=use_gpu)

    if preprocess:
        image_input = preprocess_image(image_input)
    if crop_loc is not None:
        image_input = crop_region(image_input, **crop_loc)

    if denoise:
        image_input = denoise_image(image_input)
    if enhance_contrast:
        image_input = enhance_contrast(image_input)
    image_input = cv2.resize(image_input, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)

    results = reader.readtext(image_input)
    # for bbox, text, conf in results:
    #     print(f"{text} ({conf:.2f}) | {bbox}")
    return results



if __name__ == "__main__":

    t_0 = time.time()

    path = "/Users/brianpennington/git/cfb/capture_stream/mnt/cfb_shared/screenshots/frame_20250802_171000_000049.jpg"
    cuda = torch.cuda.is_available()
    print(f"cuda = {cuda}")
    data = run_easyocr_on_image(
        image_path = path, 
        use_gpu = cuda, 
        preprocess = False, 
        denoise = False,
        enhance_contrast = False,
        crop_loc = CROP_LOCATIONS['ROSTER']['table_data']
    )
    print(data)
    print(f"cuda = {cuda}")
    print(f"time = {round(time.time() - t_0, 6)}")