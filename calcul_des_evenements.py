# Script qui permet de calculer sur quel jour aura lieu un événement pour la caravane

from random import *


jour_debut = int(input('A partir de quel jour doit on commencer les calculs ? '))
jour_fin = int(input('A quel jour doivent-ils se terminer ? '))
probabilite_event = int(input('Quel est la probabilité actuelle d\'avoir une rencontre ?'))
if probabilite_event < 10:
    probabilite_event = 10

x = jour_debut

probabilite_event_depart = 10
jours_avec_events = ""

while x < jour_fin :
    dice = randint(1,100)
    if dice <= probabilite_event:
        nom_jour = "Jour " + str(x)
        jours_avec_events = jours_avec_events + "\n" + nom_jour
        probabilite_event = probabilite_event_depart

    else:
        probabilite_event = probabilite_event + 10
    x = x + 1

print(jours_avec_events)