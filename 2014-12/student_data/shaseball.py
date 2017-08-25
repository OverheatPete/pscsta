f=open("chaseball.dat")
lines=f.readlines()
n=int(lines[0])
for i in range(1,n+1):
    xtrem=int(lines[i])
    for j in range(0,xtrem*2):
        if xtrem*2-j>j:
            print(" "*(xtrem-j-1) + "/" + " "*(2*j) + "\\")
        elif xtrem*2-j<=j:
            print(" "*(j-xtrem) + "\\" + " "*(2*(xtrem*2-j-1)) + "/")