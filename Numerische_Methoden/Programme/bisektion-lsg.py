# Funktion definieren, deren Nullstelle berechnet wird
def f(x):
    return x**3 + 5 * x - 9


####### Bisektionsverfahren ########
# Zu Beginn wird das Intervall definiert
# in welchem die Nullstelle gesucht wird
a = 1
b = 2

# Anzahl Iterationsschritte festlegen
n = 5

# Schrittzaehler
i = 1
while i <= n:
    # Hier kommt Ihr Code hin
    # Mitte des Intervalls berechnen
    m = (a + b) / 2
    # Einsetzen in f
    y = f(m)
    # Je nach Vorzeichen a oder b ersetzen
    if f(b) * f(m) < 0:
        a = m
    else:
        b = m

    print("Resultat nach ", i, " Iterationen: x_0 = ", (a + b) / 2)
    i += 1
