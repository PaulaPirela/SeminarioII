import math
from pip import Image


def escagris():  # convierte la imagen de colores a escala de grises
    arr = img.load()
    for x in xrange(Image.size[0]):
        for y in xrange(Image.size[1]):
            arr[x, y] = img.getpixel((x, y))
    return arr


huella=Image.open("ImagenesInput/huella.png").convert("L")
convirtiendo = escagris(huella)
huella.save("ImagenesOutput/escagris.tif")
huella.show()  # muestra como la imagen va quedando
def binarizacion(img,umbral):
        arr = img.load()
        for x in xrange(Image.size[0]):
            for y in xrange(Image.size[1]):
                p = img.getpixel((x, y))
                if p>umbral:
                    arr[x,y] = 255  # colores negro
                else:
                    arr[x, y] = 0  # colores blanco
        return arr

huella=Image.open("ImagenesOutput/escagris.tif").convert("L")
convirtiendo = binarizacion(huella,128)
huella.save("ImagenesOutput/binarizacion.tif")
huella.show()  # muestra como la imagen va quedando


def adelgazamiento(img,mascaraH,mascaraV):  # adelgaza las huellas para su debido analisis
    arr = img.load()

    Ha = mascaraH[0][0]
    Hb = mascaraH[0][1]
    Hc = mascaraH[0][2]
    Hd = mascaraH[1][0]
    He = mascaraH[1][1]
    Hf = mascaraH[1][2]
    Hg = mascaraH[2][0]
    Hh = mascaraH[2][1]
    Hi = mascaraH[2][2]

    Va = mascaraV[0][0]
    Vb = mascaraV[0][1]
    Vc = mascaraV[0][2]
    Vd = mascaraV[1][0]
    Ve = mascaraV[1][1]
    Vf = mascaraV[1][2]
    Vg = mascaraV[2][0]
    Vh = mascaraV[2][1]
    Vi = mascaraV[2][2]


    for x in xrange(1,img.size[0]-1):
        for y in xrange(1, img.size[-1]- 1):
            Ia = img.getpixel(x-1,y-1)
            Ib = img.getpixel(x-1,y)
            Ic = img.getpixel(x-1,y+1)
            Id = img.getpixel(x,y-1)
            Ie = img.getpixel(x,y)
            If = img.getpixel(x,y+1)
            Ig = img.getpixel(x+1,y-1)
            Ih = img.getpixel(x+1,y)
            Ii = img.getpixel(x+1, y+1)
            Gx = Ha*Ia+Hb*Ib+Hc*Ic+Hd*Id+He*Ie+Hf*If+Hg*Ig+Hh*Ih+Hi*Ii
            Gy = Va*Ia+Vb*Ib+Vc*Ic+Vd*Id+Ve*Ie+Vf*If+Vg*Ig+Vh*Ih+Vi*Ii
            Gx = math.fabs(-Ia-Id-Ig+Ic+If+Ii)
            Gy = math.fabs(-Ia-Ib-Ic+Ig+Ih+Ii)
            valor = math.sqrt(Gx*Gx+Gy*Gy)
            if valor > 255.0:
                valor = 255.0
            arr[x-1,y-1] = int(valor)
    return arr


img = Image.open("ImagenesOutput/binarizacion.tif").convert("L")
thinningX = [[0.0, 0.0, 0.0],
             [0.0, 1.0, 0.0],
             [1.0, 1.0, 1.0],

             [1.0, 0.0, 0.0],
             [1.0, 0.0, 0.0],
             [1.0, 0.0, 0.0],

             [1.0, 1.0, 1.0],
             [0.0, 1.0, 0.0],
             [0.0, 0.0, 0.0],

             [0.0, 0.0, 1.0],
             [0.0, 1.0, 1.0],
             [0.0, 0.0, 1.0]]

thinningY = [[0.0, 0.0, 0.0],
             [1.0, 1.0, 0.0],
             [0.0, 1.0, 0.0],

             [0.0, 1.0, 0.0],
             [1.0, 1.0, 0.0],
             [0.0, 0.0, 0.0],

             [0.0, 1.0, 0.0],
             [0.0, 1.0, 1.0],
             [0.0, 0.0, 0.0, ],

             [0.0, 0.0, 0.0],
             [0.0, 1.0, 1.0],
             [0.0, 1.0, 0.0]]

I = adelgazamiento(img,thinningX,thinningY)
img.save("ImagenesOutput/imgAdelgazada.tif")
img.show()


def poda(img, mascaraH, mascaraV):  # Pule la imagen
    arr = img.load()

    Ha = mascaraH[0][0]
    Hb = mascaraH[0][1]
    Hc = mascaraH[0][2]
    Hd = mascaraH[1][0]
    He = mascaraH[1][1]
    Hf = mascaraH[1][2]
    Hg = mascaraH[2][0]
    Hh = mascaraH[2][1]
    Hi = mascaraH[2][2]

    Va = mascaraV[0][0]
    Vb = mascaraV[0][1]
    Vc = mascaraV[0][2]
    Vd = mascaraV[1][0]
    Ve = mascaraV[1][1]
    Vf = mascaraV[1][2]
    Vg = mascaraV[2][0]
    Vh = mascaraV[2][1]
    Vi = mascaraV[2][2]


    for x in xrange(1, img.size[0] - 1):
        for y in xrange(1, img.size[1] - 1):
            Ia = img.getpixel(x - 1, y - 1)
            Ib = img.getpixel(x - 1, y)
            Ic = img.getpixel(x - 1, y + 1)
            Id = img.getpixel(x, y - 1)
            Ie = img.getpixel(x, y)
            If = img.getpixel(x, y + 1)
            Ig = img.getpixel(x + 1, y - 1)
            Ih = img.getpixel(x + 1, y)
            Ii = img.getpixel(x + 1, y + 1)
            Gx = Ha * Ia + Hb * Ib + Hc * Ic + Hd * Id + He * Ie + Hf * If + Hg * Ig + Hh * Ih + Hi * Ii
            Gy = Va * Ia + Vb * Ib + Vc * Ic + Vd * Id + Ve * Ie * Vf * If + Vg * Ig + Vh * Ih + Vi * Ii
            Gx = math.fabs(-Ia - Id - Ig + Ic + If + Ii)
            Gy = math.fabs(-Ia - Ib - Ic + Ig + Ih + Ii)
            valor = math.sqrt(Gx * Gx + Gy * Gy)
            if valor > 255.0:
                valor = 255.0
            arr[x - 1, y - 1] = int(valor)
    return arr

img = Image.open("ImagenesOutput/imgAdelgazada.tif").convert("L")
prunningX = [[0.0, 0.0, 0.0, ],
             [0.0, 1.0, 0.0],
             [0.0, 0.0, 0.0]]

prunningY = [[0.0, 0.0, 0.0],
             [0.0, 1.0, 0.0],
             [0.0, 0.0, 0.0, ]]
I = poda(img, thinningX, thinningY)
img.save("ImagenesOutput/imgpoda.tif")
img.show()
