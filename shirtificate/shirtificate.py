from fpdf import FPDF

def generate_shirtificate(name):
    # Create instance of FPDF class
    pdf = FPDF(orientation='P', unit='mm', format='A4')

    # Add a page
    pdf.add_page()

    # Set font for the title
    pdf.set_font("Arial", size=24)

    # Title
    pdf.cell(200, 10, txt="CS50 Shirtificate", ln=True, align='C')

    # Set font for the name
    pdf.set_font("Arial", size=16)

    # Add a line break
    pdf.ln(20)

    # Set location for the shirt image
    x = (pdf.w - 100) / 2
    y = pdf.y

    # Add shirt image
    pdf.image("shirtificate.png", x, y, 100)

    # Set font color to white
    pdf.set_text_color(255, 255, 255)

    # Set font size for the name
    pdf.set_font("Arial", size=12)

    # Add name on the shirt
    pdf.text(x + 25, y + 40, name)

    # Save the pdf with name .pdf
    pdf_file_name = "shirtificate.pdf"
    pdf.output(pdf_file_name)


if __name__ == "__main__":
    name = input("Enter your name: ")
    generate_shirtificate(name)
