from datetime import date
today = date.today()

d1 = int(today.strftime("%w"))
#print("d1 =", d1)
materia94 = ["Sem aula", "Introdução à Programação e Cálculo", "Tratamento e Análise de Dados e Sociedade, Multiculturalismo e Direitos Humanos", "Resolução de Problemas", "Fundamentos dos Sistemas de Informação e Introdução à Programação", "Cálculo e Fundamentos dos Sistemas de Informação","Sem aula"]
dSemana = ["Domingo","Segunda", "Terça", "Quarta", "Quinta","Sexta","Sabado"]
dd = int(today.strftime("%d"))
dd = dd + 1

def diaSemana():
    return dSemana[d1+1]

def materiaDia():
    return materia94[d1+1]

def data():
    return today.strftime(f"{dd}/%m/%y")

