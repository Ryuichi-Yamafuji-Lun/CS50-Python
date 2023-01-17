#implementation of cs50 shirtificate exercise
from fpdf import FPDF

class Shirt(FPDF):
    def Page(self):
        #Setting Title of PDF
        self.set_font('Times', 'B', 20)
        self.cell(80)
        self.cell(30, 10, "CS50 Shirtificate", border = 1, align= "C")
        self.ln(20)
        #Render shirt png
        self.image(".../shirtificate.jpeg", 80)

def main():
    name = input("Name: ")
    shirt = Shirt()
    shirt.add_page()
    shirt.output("shirt.pdf")

if __name__ == "__main__":
    main()