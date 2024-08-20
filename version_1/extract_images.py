import pdfplumber
import io
from PIL import Image

def extract_images_from_pdf(pdf_file):
    images = []
    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages:
            for img in page.images:
                img_data = img["stream"].get_data()
                img = Image.open(io.BytesIO(img_data))
                images.append(img)
    return images

def main():
    # PDF dosyasının adını ve yolu belirtin
    pdf_file = "pdf_with_images.pdf"

    # PDF dosyasından görüntüleri al
    images = extract_images_from_pdf(pdf_file)

    # Alınan görüntülerle istediğiniz işlemi yapın
    # Örneğin, görüntüleri göstermek için:
    for i, img in enumerate(images):
        img.show()

if __name__ == "__main__":
    main()