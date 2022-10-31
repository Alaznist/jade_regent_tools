# Programme qui permet de calculer la consommation
# de la caravane pour une journée de voyage

print("\nSuper-calculateur de la consommation journalière de la caravane !\n")

voyageurs = 14
chariots = 9
chevaux = 1
eclaireurs = int(input("Quel est le nombre d'éclaireuses et d'éclaireurs aujourd'hui ? : "))
role_des_eclaireurs = int(input("Parmis ces éclaireuses, combien vont chercher de la nourriture ? : "))
cuisiniers = int(input("Quel est le nombre de cuistots aujourd'hui ? : "))


conso = voyageurs - eclaireurs  + chariots  + chevaux
apport = (2 * role_des_eclaireurs) + (2 * cuisiniers)
stock = conso - apport

print("\nAujourd'hui, la consommation de la caravane est de", conso,"unités.\n")

print("Mais heureusement, les éclaireuses et les cuisinières vous apportent", apport,"unités de nourriture pour aujourd'hui !\n")


if stock <= 0:
    print("L'apport vous suffit pour la journée : pas besoin de taper dans votre stock !")
else:
    print("Vous devez donc prélever seulement", stock,"unités de votre stock.")

    
if stock < 0 and role_des_eclaireurs > 0:
    reste = abs(stock)
    if reste >= (2*role_des_eclaireurs):
        reste = 2*role_des_eclaireurs
    print("\nPar ailleurs, vous pouvez stocker le surplus de nourriture rapporté par les éclaireuses aujourd'hui :", reste,"unités à ajouter dans les placards !")
