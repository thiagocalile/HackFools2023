from datetime import date
today = date.today()

dia = int(today.strftime("%w"))
#print("d1 =", d1)
materia94 = [("IP, Calc"), ("TADI, SMD"), ("RP"), ("FSI, IP"), ("Calc, FSI")]

if dia == 0 or dia == 6:
    pass
else:
    print("Hoje é", dia, "" materia94[dia-1])

