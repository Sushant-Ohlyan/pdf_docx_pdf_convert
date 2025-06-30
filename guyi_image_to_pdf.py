from fpdf import FPDF
import os
from tkinter import Tk, filedialog

def images_to_pdf(image_paths, output_pdf_path):
    pdf = FPDF()

    for image_path in image_paths:
        pdf.add_page()
        pdf.image(image_path, x=0, y=0, w=210, h=297)  # A4 size

    pdf.output(output_pdf_path)
    print(f"✅ PDF created with {len(image_paths)} images at: {output_pdf_path}")
    os.startfile(output_pdf_path)

if __name__ == "__main__":
    root = Tk()
    root.withdraw()

    image_paths = filedialog.askopenfilenames(
        title="Select Images",
        filetypes=[("Image Files", "*.jpg *.jpeg *.png *.bmp *.tiff")]
    )

    if not image_paths:
        print("❌ No images selected.")
    else:
        first_image_dir = os.path.dirname(image_paths[0])
        pdf_path = os.path.join(first_image_dir, "combined_images.pdf")

        try:
            images_to_pdf(image_paths, pdf_path)
        except Exception as e:
            print(f"❌ Error: {e}")
