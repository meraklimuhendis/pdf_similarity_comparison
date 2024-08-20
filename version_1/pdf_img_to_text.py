import pdfplumber
import pytesseract
from PIL import Image
import io

def extract_text_from_pdf(pdf_file):
    text = ""
    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages:
            # Sayfa görüntüsünü al
            page_image = page.to_image()
            # PIL formatına dönüştür
            image = Image.open(io.BytesIO(page_image.original_bytes))
            # Görüntüden metni çıkar
            page_text = pytesseract.image_to_string(image, lang='eng')
            # Çıkarılan metni genel metne ekle
            text += page_text + "\n"
    return text

def main():
    # Metin çıkarmak istediğiniz PDF dosyasının adını ve yolu belirtin
    pdf_file = "your_pdf_file.pdf"

    # PDF dosyasından metni çıkar
    extracted_text = extract_text_from_pdf(pdf_file)

    # Çıkarılan metni yazdır
    print(extracted_text)

if __name__ == "__main__":
    main()