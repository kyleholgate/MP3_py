import happybase as hb
import csv


db = hb.Connection()
table = db.table('powers')

file = open('input.csv')
data = csv.reader(file)

for r in data:
	table.put(r[0], {b'personal:hero': r[1],
                         b'personal:power': r[2],
                         b'professional:name': r[3],
                         b'professional:xp': r[4],
                         b'custom:color': r[5]}) 
                                                                                                
db.close()
