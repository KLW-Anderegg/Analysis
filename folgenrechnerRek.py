def a(n):
    # Das erste Folgenglied wird direkt ausgegeben.
    if n == 1:
        return 20
    # Alle anderen Folgenglieder werden mit der Rekursionsformel berechnet
    else:
        return a(n - 1) - 4


n = 1
while n <= 5:
    print("a_", n, " = ", a(n))
    n += 1
