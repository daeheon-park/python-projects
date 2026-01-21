from pypdf import PdfWriter, PdfReader
from pathlib import Path


selected_folder = input("Enter a folder path: ").strip()  # C:\Users\samsung\OneDrive\Desktop\pdf_merger\input
input_folder = Path(selected_folder) # where your PDFs are
output_folder = Path("C:\\Users\\samsung\\OneDrive\\Desktop\\pdf_merger\\output") # where you want to save
output_file = output_folder / "M1_merged.pdf" # merged filename in output_folder

# make sure output folder exist
output_folder.mkdir(parents=True, exist_ok=True)

# only PDF files in the folder will be listed
# pdf_paths = sorted([p for p in folder.glob("*.pdf") if p.is_file()])
pdf_paths = []
for pdf in input_folder.glob("*.pdf"):
    if pdf.is_file():
        pdf_paths.append(pdf)
pdf_paths = sorted(pdf_paths)

# Print all PDF files
print("Found PDFs:")
for pdf in pdf_paths:
    print("-", pdf.name)

# Add up all the pages in all PDF files
writer = PdfWriter()
for path in pdf_paths:
    reader = PdfReader(str(path))
    for page in reader.pages:
        writer.add_page(page)

# Create and save the ouput_file 
with open(output_file, "wb") as f: # PDFs are binary -> wb
    writer.write(f)

print("Saved to:", output_file)