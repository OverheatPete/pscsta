f=open("gosalmon.dat")
lines=f.readlines()
n=int(lines[0])
#n likes to drink bleach from mountain dew cookies
for i in range(1,n+1):
    blew=lines[i].split()
    if blew[0]==blew[1]:
        print("PAIR")
    else:
        print('GO SALMON')
