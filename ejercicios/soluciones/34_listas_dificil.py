texto = "aba"
histograma = {}
for letra in texto:
    if letra not in histograma:
        histograma[letra] = 0
    histograma[letra] = histograma[letra] + 1
for letra in sorted(histograma.keys()):
    print(letra + ":", histograma[letra])
