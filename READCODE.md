<h1>Code Breakdown</h1>

<p>This project introduces a Python program designed to detect text in an image and translate it into a specified language. The program leverages Optical Character Recognition (OCR) to extract text from images and uses Azure AI Translator to convert the detected text into the desired language.</p>

<h2>Importing Libraries and Setting Up Tesseract</h2>

<p>
The necessary libraries are imported at the beginning, and the path to the Tesseract executable is set:
</p>

```py
import cv2
import pytesseract
from translate import Translator

pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

```

<h2>Text Detection Function</h2>

<p>The detect_text function loads an image, converts it to grayscale, and uses Tesseract to perform OCR on the image:</p>

<p>The input is the path to the image file and the output is the detected text as a string.</p>

```py
def detect_text(image_path):
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    custom_config = r'--oem 3 --psm 6'
    text = pytesseract.image_to_string(gray, config=custom_config)
    return text.strip()

```

<h2>Text Preprocessing Function</h2>

<p>The preprocess_text function handles hyphenated words that may be split across lines, ensuring they are properly joined:</p>

<p>The input is the detected text as a string and the output is the processed text with hyphenated words joined.</p>

```py
def preprocess_text(text):
    lines = text.split('\n')
    processed_lines = []
    skip_next = False
    for i in range(len(lines)):
        if skip_next:
            skip_next = False
            continue
        if lines[i].endswith('-') and i < len(lines) - 1:
            processed_lines.append(lines[i][:-1] + lines[i + 1])
            skip_next = True
        else:
            processed_lines.append(lines[i])
    return '\n'.join(processed_lines)


```

<h2>Text Translation Function</h2>

<p>The input is the processed text and target language code and the output is the translated text.</p>

```py
def translate_text(text, target_lang='en'):
    translator = Translator(to_lang=target_lang)
    lines = text.split('\n')
    translated_lines = []
    for line in lines:
        chunk_size = 500
        chunks = [line[i:i + chunk_size] for i in range(0, len(line), chunk_size)]
        translated_chunks = []
        for chunk in chunks:
            translated_chunks.append(translator.translate(chunk))
        translated_line = ''.join(translated_chunks)
        translated_lines.append(translated_line)
    return '\n'.join(translated_lines)


```

<h2>Main Function</h2>

<p>The input is the path to the image file and target language code, and the output is the translated text printed to the console.</p>

```py

def main(image_path, target_lang='en'):
    text = detect_text(image_path)
    print(f"Detected Text: {text}")
    preprocessed_text = preprocess_text(text)
    print(f"Preprocessed Text: {preprocessed_text}")
    translated_text = translate_text(preprocessed_text, target_lang)
    print(f"Translated Text: {translated_text}")

if __name__ == "__main__":
    image_path = r"D:\\Computer Vision\\OCR_Images\\image.jpg"
    target_lang = 'pt-br'
    main(image_path, target_lang)


```

<h2>Example Usage</h2>

<p>The example usage provided in the code runs the main function with a specified image path and target language (pt-br for Brazilian Portuguese).</p>

<p>This program demonstrates a practical application of OCR and translation technologies, converting text in images to different languages. It is useful for various applications, including document translation, assisting with language learning, and more.</p>
