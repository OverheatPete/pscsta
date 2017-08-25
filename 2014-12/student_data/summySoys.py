f=open("sammysays.dat")
lines=f.readlines()
n=int(lines[0])
for i in range(1,n+1):
    carasu=str(lines[i].strip())
    if carasu[0:10]=='Sammy says':
        print(carasu[11:])
print(chr(2039))