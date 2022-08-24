callesList = []
file = open("calles_de_medellin_con_acoso.csv")
for line in file:
    callesList.extend(str(line).split(";"))
print("Rellenado completo")
"""for i in range(0,13):
    print(callesList[i])
print(callesList)"""