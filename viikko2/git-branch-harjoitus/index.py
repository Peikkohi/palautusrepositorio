from logger import logger
from summa import summa
from erotus import erotus

logger("aloitetaan")

x = int(input("luku I: "))
y = int(input("luku II: "))
print(f"{summa(x, y)}")
print(f"{erotus(x, y)}")

logger("lopetetaan")
