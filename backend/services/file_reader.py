import os
from PyPDF2 import PdfReader
from docx import Document


def read_file(filepath):
    ext = os.path.splitext(filepath)[1].lower()

    # TXT
    if ext == ".txt":
        with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
            return f.read()

    # PDF
    elif ext == ".pdf":
        reader = PdfReader(filepath)
        text = ""

        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"

        return text

    # DOCX
    elif ext == ".docx":
        doc = Document(filepath)

        text = ""

        for para in doc.paragraphs:
            text += para.text + "\n"

        return text

    return "Unsupported file type."