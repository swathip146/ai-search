import PyPDF2

class DocumentLoader:
    """Extracts text from a PDF file."""

    @staticmethod
    def extract_text(pdf_path):
        """Reads a PDF and extracts text."""
        text = ""
        with open(pdf_path, "rb") as file:
            reader = PyPDF2.PdfReader(file)
            for page in reader.pages:
                text += page.extract_text() + "\n"
        return text
