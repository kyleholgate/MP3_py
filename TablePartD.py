import happybase as hb

# DON'T CHANGE THE PRINT FORMAT, WHICH IS THE OUTPUT
# OR YOU WON'T RECEIVE POINTS FROM THE GRADER
db = hb.Connection()
table = db.table('powers')

r = table.row(b'row1')

hero = r[b'personal:hero']
power = r[b'personal:power']
name = r[b'professional:name']
xp = r[b'professional:xp']
color = r[b'custom:color']

print('hero: {}, power: {}, name: {}, xp: {}, color: {}'.format(hero, power, name, xp, color))

r = table.row(b'row19')

hero = r[b'personal:hero']
color = r[b'custom:color']

print('hero: {}, color: {}'.format(hero, color))

r = table.row(b'row1')

hero = r[b'personal:hero']
name = r[b'professional:name']
color = r[b'custom:color']
print('hero: {}, name: {}, color: {}'.format(hero, name, color))

db.close()
