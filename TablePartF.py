import happybase as hb

# DON'T CHANGE THE PRINT FORMAT, WHICH IS THE OUTPUT
# OR YOU WON'T RECEIVE POINTS FROM THE GRADER

db = hb.Connection()
table = db.table('powers')

for key, data in table.scan():
	color = data['custom:color']
	name = data['professional:name']
	power = data['personal:power']

	for key1, data1 in table.scan():
		if key != key1 and color == data1['custom:color'] and name != data1['professional:name']:
			color1 = data1['custom:color']
			name1 = data1['professional:name']
			power1 = data1['personal:power']

			print('{}, {}, {}, {}, {}'.format(name, power, name1, power1, color))

db.close()
