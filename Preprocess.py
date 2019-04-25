import csv
import pandas as pd

# Extract the 108 indicators
f=pd.read_csv("E://JI//Temp//data//data.csv")
keep_col=[]
for i in range(1,109):
    keep_col.append('indicator'+str(i))

new_f = f[keep_col]
new_f.to_csv("E://JI//Temp//data//data108.csv", index=False)

# Extract the midPrice
'''
f=pd.read_csv("E://JI//Temp//data//data.csv")
keep_col=['midPrice']
new_f = f[keep_col]
new_f.to_csv("E://JI//Temp//data//midPrice.csv", index=False)
'''



'''
row=0
with open('E://JI//Temp//data//data.csv', 'r') as myFile:
    lines = csv.reader(myFile)
    for line in lines:
        row += 1

print(row)
# Total rows: 1721578
'''