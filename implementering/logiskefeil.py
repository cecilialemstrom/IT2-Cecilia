assert 10 > 5 # 10 er større enn 5, derfor gjør denne ingenting

try:
    assert 10 > 20 # 10 er ikke større enn 20, derfor gir denne en feilmelding
except:
    print ("Hei på deg")

# Oppgave: definer en funksjon med navn areal, som tar inn høyde og bredde og returnerer arealet av rektangelet

def areal(høyde, bredde):
    return høyde*bredde

def omkrets(høyde, bredde):
    return høyde + høyde + bredde + bredde

# Oppgave: Test funksjonen areal på tre forskjellig rektangler

assert areal(3,2) == 6
assert areal(3,3) == 9
assert areal(3,4) == 12
assert omkrets(3,2) == 10
assert omkrets(3,3) == 12
assert omkrets(3,4) == 14



print ("Koden er ferdig")