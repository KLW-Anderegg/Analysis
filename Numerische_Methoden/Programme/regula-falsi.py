# Funktion definieren, deren Nullstelle berechnet wird
def f(x):
    return x**3 + 5 * x - 7


####### Regula Falsi ########
# Zu Beginn wird das Intervall definiert
# in welchem die Nullstelle gesucht wird
a = 1
b = 2

# Anzahl Iterationsschritte festlegen
n = 20

# Schrittzaehler
i = 1
while i <= n:
    # naechste Approximation berechnen
    m = (f(b) - f(a)) / (b - a)
    x = a - f(a) / m
    # Je nach Vorzeichen a oder b ersetzen
    if f(b) * f(x) < 0:
        a = x
    else:
        b = x

    print("Resultat nach ", i, " Iterationen: x_0 = ", x)
    i += 1
