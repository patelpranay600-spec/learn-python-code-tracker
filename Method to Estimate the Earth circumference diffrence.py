# Eratosthenes’ Method to Estimate the Earth’s Circumference

angle=float(input("input your angle made by shadow"))
synes=float(input("input your synes distance"))
print("we know that earths circumference is 40075")
earcum=40075
uh=360/(angle)
rt= uh*synes
per= ((rt-40075)/40075)*100
pert=per%1
print("estimated diffrence is",pert)
