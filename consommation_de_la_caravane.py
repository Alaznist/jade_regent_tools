# Programme qui permet de calculer la consommation
# de la caravane pour une journée de voyage

print("\nSuper-calculateur de la consommation journalière de la caravane !\n")

voyageurs = int(input("Combien de voyageurs possède la caravane ? : "))
chariots = int(input("Combien de chariots possède la caravane ? : "))
don_consommation_efficace = input("La caravane possède-t-elle le don 'consommation efficace' ? [Oui/Non]: ")
while 'n' not in don_consommation_efficace.lower() and 'o' not in don_consommation_efficace.lower():
    don_consommation_efficace = input("La caravane possède-t-elle le don 'consommation efficace' ? [Oui/Non]: ")
if 'n' in don_consommation_efficace.lower():
    don_consommation_efficace = 0
else:
    don_consommation_efficace = -2
chevaux = int(input("Combien d'animaux supplémentaire consomment de la nourriture ? : "))
anneau = int(input("Combien de personnes portent un anneau de subsistance ? : "))
eclaireurs = int(input("Quel est le nombre d'éclaireuses et d'éclaireurs aujourd'hui ? : "))
role_des_eclaireurs = int(input("Parmis ces éclaireuses, combien vont chercher de la nourriture ? : "))
cuisiniers = int(input("Quel est le nombre de cuistots aujourd'hui ? : "))
magie = int(input("Combien de nourriture vous est apportée par magie ? : "))


conso = voyageurs - eclaireurs - anneau + chariots + don_consommation_efficace + chevaux
apport = (2 * role_des_eclaireurs) + (2 * cuisiniers) + magie
stock = conso - apport

print("\nAujourd'hui, la consommation de la caravane est de", conso,"unités.\n")

print("Mais heureusement, les éclaireuses, les cuisinières et la magie vous apportent", apport,"unités de nourriture pour aujourd'hui !\n")


if stock <= 0:
    print("L'apport vous suffit pour la journée : pas besoin de taper dans votre stock !")
else:
    print("Vous devez donc prélever seulement", stock,"unités de votre stock.")


if stock < 0 and role_des_eclaireurs > 0:
    reste = abs(stock)
    if reste >= (2*role_des_eclaireurs):
        reste = 2*role_des_eclaireurs
    print("\nPar ailleurs, vous pouvez stocker le surplus de nourriture rapporté par les éclaireuses aujourd'hui :", reste,"unités à ajouter dans les placards !")
