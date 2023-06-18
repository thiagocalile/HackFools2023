from datetime import date
today = date.today()

d1 = int(today.strftime("%w"))
#print("d1 =", d1)
materia94 = ["Sem aula", ("IP, Calc"), ("TADI, SMD"), ("RP"), ("FSI, IP"), ("Calc, FSI"),"Sem aula"]
dSemana = ["Domingo","Segunda", "Terça", "Quarta", "Quinta","Sexta","Sabado"]


def diaSemana():
    return dSemana[d1]

def materiaDia():
    return materia94[d1]

def data():
    return today.strftime("%d/%m/%y")

print(diaSemana())
print(materiaDia())
print(data())
