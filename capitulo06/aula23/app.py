from pathlib import Path
from PyPDF2 import PdfReader, PdfWriter, PdfMerger

ROOT = Path(__file__).parent
FOLDER_PDFS = ROOT / "pdfs"
NEW_FOLDER = ROOT / "pdfs_updated"
REPORT = FOLDER_PDFS / "teste.pdf"
NEW_FOLDER.mkdir(exist_ok=True)

reader = PdfReader(REPORT)
first_page = reader.pages[0]

for page in reader.pages:
    print(page)
    print()


for i, page in enumerate(reader.pages):
    writer = PdfWriter()
    with open(NEW_FOLDER / f"page{i}.pdf", "wb") as file:
        writer.add_page(page)
        writer.write(file)


files = [
    NEW_FOLDER / "page0.pdf",
    NEW_FOLDER / "page1.pdf",
    NEW_FOLDER / "page2.pdf",
    NEW_FOLDER / "page3.pdf",
    NEW_FOLDER / "page4.pdf",
]

merger = PdfMerger()

for file in files:
    merger.append(file)

merger.write(NEW_FOLDER / "merged.pdf")
merger.close()
