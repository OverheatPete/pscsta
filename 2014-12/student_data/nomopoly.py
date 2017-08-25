f=open("nomopoly.dat")
lines=f.readlines()
n=int(lines[0])
for i in range(1,n+1):
    print(lines[i])