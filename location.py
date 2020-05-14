import csv
import pandas as pd
import ensembl_rest
df = pd.read_csv("~/Desktop/thesis/200321.csv",sep = ',', header=None)
#print(df.shape[0]) rows
#print(df.shape[1]) cols
#print(df[0][1])

cols1 = []

for k in range(df.shape[0]):
    cols1.append(df[0][k])
print(len(cols1))

cols2 = []
for j in range(df.shape[0]):
    cols2.append(df[1][j])
print(len(cols2))
    
res = []

for i in cols2:
	try:
		seq = ensembl_rest.sequence_id(i)
	    loc = seq.get("desc")
		result = (i, loc)
		print(str(cols2.index(i)) + " " + str(result))
		res.append(str(result))
	except ensembl_rest.HTTPError as err:
		error_code = err.response.status_code
		error_message = err.respinse.json()["error"]
		if (error_code == 400):
			print("not found")
			res.append("not found")
			pass
		else:
			raise

with open("location.txt", "w") as output:
    for m in range(df.shape[0]):
        output.writelines(str(cols1[m]) + "," + str(res[m])+ "\n")
