import PyPDF2
from difflib import SequenceMatcher

def pdf_to_text(pdf_file):
    text = ""
    with open(pdf_file, "rb") as f:
        reader = PyPDF2.PdfFileReader(f)
        for page_num in range(reader.numPages):
            page = reader.getPage(page_num)
            text += page.extractText()
    return text

def calculate_similarity(text1, text2):
    similarity_ratio = SequenceMatcher(None, text1, text2).ratio()
    return similarity_ratio

def main():
    # İki PDF dosyasının adını ve yolu belirtin
    pdf_file1 = "pdf1.pdf"
    pdf_file2 = "pdf2.pdf"

    # PDF dosyalarını metin olarak oku
    text1 = pdf_to_text(pdf_file1)
    text2 = pdf_to_text(pdf_file2)

    # Metinler arasındaki benzerlik oranını hesapla
    similarity_ratio = calculate_similarity(text1, text2)

    print("PDF dosyaları arasındaki benzerlik oranı:", similarity_ratio)

if __name__ == "__main__":
    main()