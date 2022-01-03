import csv
with open("desktop/car.csv","r") as csvfile:
    a=[tuple(x) for x in csv.reader(csvfile)]

num_att=len(a[0])-1

S=['0']*num_att
G=['?']*num_att
i=0
print("S[{0}]: ".format(i),S)
print("G[{0}]: ".format(i),G)
temp=[]
for i in range(num_att):
    S[i]=a[1][i]

print("-----------")


for i in range(1,len(a)):
    if a[i][num_att]=='YES':
        for j in range(num_att):
            if S[j]!=a[i][j]:
                S[j]='?'
        for j in range(num_att):
            for k in range(len(temp)-1):
                if temp[k][j]!=S[j] and temp[k][j]!='?':
                    del temp[k]
    
    if a[i][num_att]=='NO':
        if len(temp)==0:
            for j in range(num_att):
                if a[i][j]!=S[j] and S[j]!='?':
                    G[j]=S[j]
                    temp.append(G)
                    G=['?']*num_att
        else:
            for h in range(len(temp)):
                c=0
                for j in range(num_att):
                    if temp[h][j]!=a[i][j]:
                        c+=1
                        if temp[h][j]!='?':
                            v=temp[h][j]

                if c<num_att:
                    #print(temp[h])
                    G=temp[h].copy()
                    hypo=temp[h].copy()
                    del temp[h]
                    for j in range(num_att):
                        if a[i][j]!=S[j] and S[j]!='?' and S[j]!=v:
                            G[j]=S[j]
                            #print(G)
                            temp.append(G)
                            G=hypo.copy()


    print("S[{0}]: ".format(i),S)

    if len(temp)==0:
        print("G[{0}]: ".format(i),G)
    else:
        print("G[{0}]: ".format(i),temp)
    print("-----------")
