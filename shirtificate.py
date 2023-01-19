#implementation of cs50 shirtificate exercise
from fpdf import FPDF

class Shirt():
    def __init__(self, name):
        self._pdf = FPDF()
        self._pdf.add_page()
        
    
def main():
    name = input("Name: ")
    shirt = Shirt()
    shirt.add_page()
    shirt.output("shirt.pdf")

if __name__ == "__main__":
    main()