from fpdf import FPDF
import os

def images_to_pdf(image_paths, output_pdf_path):
    pdf = FPDF()

    for image_path in image_paths:
        pdf.add_page()
        pdf.image(image_path, x=0, y=0, w=210, h=297)  # A4 size in mm

    pdf.output(output_pdf_path)
    print(f"✅ PDF created with {len(image_paths)} images at: {output_pdf_path}")
    os.startfile(output_pdf_path)  

if __name__ == "__main__":
    paths_input = input("Enter paths to image files (comma-separated): ").strip()
    image_paths = [path.strip() for path in paths_input.split(',')]

    first_image = image_paths[0]
    image_dir = os.path.dirname(first_image)
    pdf_path = os.path.join(image_dir, "combined_images.pdf")

    try:
        images_to_pdf(image_paths, pdf_path)
    except Exception as e:
        print(f"❌ Error: {e}")
