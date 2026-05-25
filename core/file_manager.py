import os
from datetime import datetime

PDF_STORAGE = os.path.join("storage", "pdfs")

class FileManager:

    def save_file(self, uploaded_file):
        # Generate unique filename
        os.makedirs(PDF_STORAGE, exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        clean_name = uploaded_file.name.replace(" ", "_")
        filename = f"{timestamp}_{clean_name}"

        file_path = os.path.join(PDF_STORAGE, filename)

        # Save file
        with open(file_path, "wb") as f:
            f.write(uploaded_file.read())

        return file_path