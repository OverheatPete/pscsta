f=open("gamereviews.dat")
lines=f.readlines()
n=int(lines[0])
ag={}
for i in range(1,n+1):
    rage=lines[i].strip().split(",")
    if rage[1] not in ag:
        ag[rage[1]]=[]
        ag[rage[1]].append(rage[2])
    else:
        ag[rage[1]].append(rage[2])
r={}
for j in ag:
    s=sum([float(k) for k in ag[j]])/len(ag[j])
    r[j]=round(s,1)
g=r.keys()
gg=sorted(g)
for k in gg:
    print(k,r[k])