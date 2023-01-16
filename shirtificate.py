#implementation of cs50 shirtificate exercise
from fpdf import FPDF

class Shirt(FPDF):
    def Page(self):
        #Setting Title of PDF
        self.set_font('Times', 'U', 16)
        
        #Render shirt png

        




def main():
    name = input("Name: ")

if __name__ == "__main__":
    main()