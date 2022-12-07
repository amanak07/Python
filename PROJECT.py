n=int(input("Enter the no. of students\n"))
if(n==0):
    print("NO STUDENTS")
    exit()
nml=[]
mrl=[]
upl=[]
i=0
while i<n:
    name=input("Name of Student: ").upper()
    marks=int(input("Marks of Student: "))
    update=int(input("Update in marks: "))
    nml.append(name)
    mrl.append(marks)
    upl.append(update)
    i+=1

print("\n"*100)

for i in range(n-1):
    for j in range(n-i-1):
        if(mrl[j]<mrl[j+1]):
            mrl[j], mrl[j + 1] = mrl[j + 1], mrl[j]
            nml[j], nml[j + 1] = nml[j + 1], nml[j]
            upl[j], upl[j + 1] = upl[j + 1], upl[j]

print("\n\t\t\tORIGINAL RANK LIST:")

print("\nName\t\t\t\Marks\t\t\t Update\n")
for i in range(n):
    print("{0:20s}".format(nml[i]),"{0:3d}".format(mrl[i]),"{0:20d}".format(upl[i]))


mrl=[mrl[x]+upl[x] for x in range(len(mrl))]
max1=mrl.index(max(mrl))

for i in range(n-1):
    for j in range(n-i-1):
        if(mrl[j]<mrl[j+1]):
            mrl[j], mrl[j + 1] = mrl[j + 1], mrl[j]
            nml[j], nml[j + 1] = nml[j + 1], nml[j]

print("\n\n\t\t\tUPDATED RANK LIST:")
print("\nName\t\t\t Marks\n")
for i in range(n):
    print("{0:20s}".format(nml[i]),"{0:3d}".format(mrl[i]))

print("\nStudent with the highest marks:\n"+nml[0])
print("Original rank: ",max1+1,"\nRanks jumped:  ",max1)
