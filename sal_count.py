from sys import argv

sal_count, vir, stav, bonus = argv
def salary(x, y, z):
    try:
        return(float(x) * float(y) + float(z))
    except ValueError: # если премия в процентах
        p = float(z.strip('%')) / 100
        return (float(x) * float(y) * (1 + p))
print("Заработная плата сотрудника: ", salary(vir, stav, bonus))