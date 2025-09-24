"""
A csoport:
Készítsünk programot, amely labdák csomagolásához végez számításokat.
A labdákat szalaggal kell átkötni úgy, hogy kétszer körbe érje őket, és a masni készítéséhez számolunk még 60 cm-t.
A labda körül a szalag egy kör (kerület képlete 2*r*PI)
A program kérje be a labda átmérőjét, a labdák számát, és a rendelkezésre álló szalag hosszát!
Számítsa ki, és írja a képernyőre, hogy a bekért számú labda csomagolásához hány centiméter szalagra van szükség, valamint állapítsa meg,
hogy elegendő szalagunk van-e a művelet elvégzéséhez, és ezt is közölje a felhasználóval!



"""
Radial = int(input("Kérlek add meg a labda sugarát! (centiméterben) " ))
Quantity = int(input("Kérlek add meg a labdák számát! (darabban) "))
Lenght = int(input("Kérlek add meg a szalagod hosszát (centiméterben) "))

Math = Quantity*(((2*Radial*3.14)*2)+60)

if Math > Lenght :
    print(f"Neked {Lenght} cm szalagod van a és neked {Math} cm szalagra van szükséged, nincs elég szalagod!")
else:
    print(f"Neked {Lenght} cm szalagod van a és neked {Math} cm szalagra van szükséged, van elég szalagod!")