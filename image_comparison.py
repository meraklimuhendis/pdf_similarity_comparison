import pdfplumber
import io
import cv2
from skimage.metrics import structural_similarity as ssim
from PIL import Image

def extract_images_from_pdf(pdf_file):
    images = []
    with pdfplumber.open(pdf_file) as pdf:
        for page_num, page in enumerate(pdf.pages):
            for img_num, img in enumerate(page.images):
                img_data = img["stream"].get_data()
                img = Image.open(io.BytesIO(img_data))
                images.append((page_num, img_num, img))
    return images

def compare_images(image1, image2):
    # Görüntüleri gri tonlamalı olarak yükle
    gray_image1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
    gray_image2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)

    # SSIM skoru hesapla
    score, _ = ssim(gray_image1, gray_image2, full=True)
    return score

def main():
    # Karşılaştırılacak PDF dosyalarının adını ve yolu belirtin
    pdf_file1 = "pdf1_with_images.pdf"
    pdf_file2 = "pdf2_with_images.pdf"

    # PDF dosyalarından görüntüleri çıkar
    images1 = extract_images_from_pdf(pdf_file1)
    images2 = extract_images_from_pdf(pdf_file2)

    # Karşılaştırma sonuçlarını depolamak için bir liste oluştur
    similarity_scores = []

    # Görüntülerin karşılaştırılması
    for image1 in images1:
        for image2 in images2:
            score = compare_images(cv2.cvtColor(np.array(image1[2]), cv2.COLOR_RGB2BGR), cv2.cvtColor(np.array(image2[2]), cv2.COLOR_RGB2BGR))
            similarity_scores.append((image1, image2, score))

    # En yüksek benzerlik skorunu bul
    max_score = max(similarity_scores, key=lambda x: x[2])

    # Sonucu yazdır
    print("En yüksek benzerlik skoru:", max_score[2])

if __name__ == "__main__":
    main()