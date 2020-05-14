import pandas as pd
import mygene
import csv

df = pd.read_csv("~/Desktop/thesis/geneid.csv",sep = ',', header=None)
rows = df.shape[0]
cols = df.shape[1]
#print(df.iloc[0])
mg = mygene.MyGeneInfo()
res = []
for r in range(rows):
    for c in range(cols): 
        if pd.isna(df[c][r])== True :
            continue
        if "ENSG" in str(df[c][r]):
            complex1 = mg.querymany(str(df[c][r]), scope = "entrezgene", species = "human", fields='ensembl.gene',returnall=True)
            result = (r+1,complex1)
            print(result)
            res.append(str(result))
        else:
            complex1 = mg.querymany(str(int(df[c][r])), scope = "entrezgene", species = "human", fields='ensembl.gene',returnall=True)
            result = (r+1,complex1)
            print(result)
            res.append(str(result))
            #print([kv["ensembl"]["gene"] for kv in complex1])
print(len(res))
with open("s1.txt", "w") as output:
    for k in range(len(res)):
        output.writelines(str(res[k])+ "\n")
        
