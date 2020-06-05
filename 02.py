"""
RETO 2:
Pasar a romano cualquier año que se lea de teclado comprendido entre 1 y 3000.
"""

unidades = ('','I','II','III','IV','V','VI','VII','VIII','IX','X')
decenas = ('','X','XX','XXX','XL','L','LX','LXX','LXXX','LC')
centenas = ('','C','CC','CCC','CD','D','DC','DCC','DCCC','CM')
millares = ('','M','MM','MMM')

year = 2020
y =year

m = y // 1000
y = y % 1000
c = y // 100
y = y % 100
d = y // 10
u = y % 10

print(f"{millares[m]}{centenas[c]}{decenas[d]}{unidades[u]}")