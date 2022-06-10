from stegano import lsbset
from stegano.lsbset import generators
import random
import time
import os

def how_long(y):
    result = ""
    for x in range(y):
        rand = random.randint(97,123)
        result += chr(rand)
    return result

short = how_long(10)
medium = how_long(1000)
long = how_long(10000)
messages= [short, medium, long]

small = "./100kb.png"
bigger = "./1mb.png"
biggest = "./14mb.png"
images = [small, bigger, biggest]

generators__ = [generators.eratosthenes(), generators.fibonacci()]

def encrypt_image(image_path, generator, message, x):
    secret_image = lsbset.hide(image_path,
                                    message,
                                    generator)
    secret_image.save("./image{}.png".format(x))

def decrypt_image(image_path, generator):
    message = lsbset.reveal(image_path, generator)
    return message

def main():
    original_img = "./100kb.png"
    start = time.time()
    encrypt_image(images[0], generators__[0],messages[2],"small_long_eratosthenes")
    decrypt_image("./imagesmall_long_eratosthenes.png", generators.eratosthenes())
    czas_malego_dlugi = time.time() - start
    print(str(float('%.2f' % (czas_malego_dlugi)) )+ "s - długość szyfrowania i deszyfrowania tekstu o długości 10 000 znakow")
    file_stat_original = os.stat(original_img)
    file_stat_encoded = os.stat("./imagesmall_long_eratosthenes.png")
    print( "Zdjęcie po zaszyfrowaniu tekstu o długości 10 000 znaków jest większe o: "+str(file_stat_encoded.st_size - file_stat_original.st_size) + " Bajtów\n")
    start = time.time()
    encrypt_image(images[0], generators.eratosthenes(), messages[1], "small_medium_eratosthenes")
    decrypt_image("./imagesmall_medium_eratosthenes.png", generators.eratosthenes())
    czas_malego_dlugi = time.time() - start
    print(str(float('%.2f' % (czas_malego_dlugi))) + "s - długość szyfrowania i deszyfrowania tekstu o długości 1000 znaków")
    file_stat_encoded = os.stat("./imagesmall_medium_eratosthenes.png")
    print( "Zdjęcie po zaszyfrowaniu tekstu o długości 1000 znaków jest większe o: "+str(file_stat_encoded.st_size - file_stat_original.st_size) + " Bajtów\n")
    start = time.time()
    encrypt_image(images[0], generators.eratosthenes(), messages[0], "small_short_eratosthenes")
    decrypt_image("./imagesmall_short_eratosthenes.png", generators.eratosthenes())
    czas_malego_dlugi = time.time() - start
    print(str(float(
        '%.2f' % (czas_malego_dlugi))) + "s - długość szyfrowania i deszyfrowania tekstu o długości 10 znaków")
    file_stat_encoded = os.stat("./imagesmall_short_eratosthenes.png")
    print("Zdjęcie po zaszyfrowaniu tekstu o długości 10 znaków jest większe o: " + str(
    file_stat_encoded.st_size - file_stat_original.st_size) + " Bajtów\n")
    iterator = 1
    for k in images:
        for d in messages:
            encrypt_image(k, generators.eratosthenes(), d, iterator)
            iterator += 1
main()