from component import vars
from PIL import Image

t = Image.open("Tulip.jpg")
d = Image.open("Daffodil.png")
s = Image.open("Sunflower.jpg")
b = Image.open("Bluebell.jpg")
c = Image.open("Cherry blossom.jpg")

def total(value):

    if (value == 10):
        t.show()
        print(t.format, t.size, t.mode)

    else:

        if (value == 20):
            d.show()
            print(d.format, d.size, d.mode)

        elif (value == 30):
            s.show()
            print(s.format, s.size, s.mode)

        elif (value == 40):
            b.show()
            print(b.format, b.size, b.mode)   

        else:
            c.show()
            print(c.format, c.size, c.mode)    
                    