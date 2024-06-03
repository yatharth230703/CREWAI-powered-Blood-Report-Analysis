#converting pdf to text for easy readability 
import fitz 
def pdf_to_text(pdf_path, txt_path):
    pdf_document = fitz.open(pdf_path)
    with open(txt_path, 'w', encoding='utf-8') as text_file:
        for page_num in range(len(pdf_document)):
            page = pdf_document.load_page(page_num)
            text = page.get_text()
            text_file.write(text)
            text_file.write("\n\n")  
    print(f"done")

# Example usage
pdf_path = 'C:\Users\SURFACE\Desktop\wingify_final_submission'
txt_path = 'output.txt'
pdf_to_text(pdf_path, txt_path)