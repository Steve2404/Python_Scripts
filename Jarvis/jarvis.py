import pyttsx3
import datetime
import speech_recognition as sr

def parler(audio):
    AV = pyttsx3.init()
    AV.say(audio)
    AV.runAndWait()

def heure():
    h = datetime.datetime.now().strftime('%I:%M:%S')
    parler(h)

def date():
    annee = int(datetime.datetime.now().year)
    mois =int(datetime.datetime.now().month)
    print(datetime.datetime.now().month)
    jour = int(datetime.datetime.now().day)
    parler(jour)
    parler(mois)
    parler(annee)


#Creation de la fonction de salutation
def salutation():
    parler("Willkommen une autre fois ")
    parler("La date est ")
    date()
    h = datetime.datetime.now().hour
    if h > 16 :
        parler("Bonsoir Leonel")
    elif h >= 12:
        parler("Bon apres midi leonel")
    else:
        parler("Bonjour leonel")

def commande():
    r = sr.Recognizer()
    with sr.Microphone() as source: # defeni le microphone comme source de reconnaissance vocale
        print("Donnez moi un ordre ..... ")
        r.pause_threshold = 1   # faire une pause d une seconde
        audio = r.listen(source)
        # cas ou la machine n a pas bie ecoute ce que le user demandait
    try:
        print("En écoute ....")
        requete = r.recognize_google(audio, language='fr-FR')
        print(requete)
    except Exception as e :
        print(e)
        parler("Bitte könnten Sie noch mal Ihre Befehl wiederholen ?")
        return 'None'
    return requete

parler(commande())
