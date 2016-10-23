table  = {1: "Alan", 3: "Hong", 7: "Jack"}

for year in table:
    print (year  , '\t'*4 ,  table[year])

print(list(table.items()))