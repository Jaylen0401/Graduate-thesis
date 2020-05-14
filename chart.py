import pandas as pd
import csv

df = pd.read_csv("~/Desktop/thesis/location0322.csv",sep = ',', header=None)

#print(max(df[0])) the max number of cols0
#print(len(df[0])) the rows of cols0
cols1 = []
cols2 = []
cols3 = []
result = []
for i in range(1,max(df[0])+1):
    for j in range(len(df[0])):
        if(df[0][j] == i):
            cols1.append(df[1][j])
            cols2.append(df[2][j])
            cols3.append(df[3][j])
        else:
            continue
    if(len(cols1)):
        header = "Complex"+str(i).zfill(4)+","
        for m in range(len(cols1)):
            header = header + str(cols1[m])+ ","
        print(header)
        result.append(header)
        #print(header) # convert to writelines
        rows = ""
        for n in range(len(cols1)):
            rows = cols1[n] + ","
            for p in range(len(cols1)):
                if(n<=p):
                    if(cols2[n] == cols2[p]):
                        rows = rows + str(abs(cols3[n] - cols3[p])) + ","
                    else:
                        rows = rows + "I,"
                else:
                    rows = rows + ","
            print(rows)
            result.append(rows)
            rows = ""
        print("\n")
        result.append("\n")
        #print(i)
        #print(cols1)
        #print(cols2)
        #print(cols3)
        #print("---")
        cols1.clear()
        cols2.clear()
        cols3.clear()

with open("Distance_chart.txt","w") as output:
    for q in range(len(result)):
        output.writelines(result[q]+"\n")
    
    
    

