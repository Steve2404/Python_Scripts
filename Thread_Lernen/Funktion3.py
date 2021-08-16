import phonenumbers
from phonenumbers import carrier
from phonenumbers import geocoder
from Funktion2 import Countdown

t = Countdown(10)
t.start()

def number_ken():

    snumber = input("Entrez un numero")
    phone_number = phonenumbers.parse(snumber)

    print(geocoder.description_for_number(phone_number, 'de'))
    print(carrier.name_for_number(phone_number, 'de'))


number_ken()