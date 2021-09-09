#from playsound import playsound
from time import sleep as t


def countdown():
    #playsound('./tone.wav')
    print("DIIINGG")


#-----------------

length = 120

while length > 0:
    if length % 15 == 0:
        countdown()
    t(1)
    length = length - 1
    print(length)
