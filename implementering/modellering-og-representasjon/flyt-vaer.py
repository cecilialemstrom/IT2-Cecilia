grader = int(input("Hvor mange grader er det ute?"))

if grader < 15:
    print("Ta på jakke")
    type = input("Regner det?")
    if type.lower() == "ja":
        print ("Ta med paraply")
else:
    print("Ha en fin dag i varmen!")

# Utvid diagrammet slik at det tar hensyn til den nye koden

i = 0
while 1 < 20:
    i+=2
    print(i)

