import datetime

ddn = input("Entrez votre date de naissance")
ddn = datetime.datetime.strptime(ddn, "%d/%m/%Y")
print(ddn)
d18 = ddn.replace(year=ddn.year+18)
print(f"Tu seras majeur le {d18.strftime("%d/%m/%Y")}")
if d18 <= datetime.datetime(2027, 6, 1):
    print("tu pourras voter le 01/06/2027")
else:
    print("tu devras attendre la prochaine élection")