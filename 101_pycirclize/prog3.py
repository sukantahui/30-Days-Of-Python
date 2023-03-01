

from pycirclize import Circos

sectors = {"A": 10, "B": 20, "C": 15}
circos = Circos(sectors, space=5)
circos.rect(r_lim=(80, 100))
circos.rect(r_lim=(60, 80), deg_lim=(0, 270), fc="tomato")
circos.rect(r_lim=(30, 50), deg_lim=(90, 360), fc="lime", ec="grey", lw=2, hatch="//")
circos.rect(r_lim=(30, 100), deg_lim=(0, 90), fc="orange", alpha=0.2)
fig = circos.plotfig()
circos.savefig("example03.png")