import happybase as hb

# DON'T CHANGE THE PRINT FORMAT, WHICH IS THE OUTPUT
# OR YOU WON'T RECEIVE POINTS FROM THE GRADER

db = hb.Connection()
table = db.table('powers')

for key, data in table.scan():
    print('Found: {}, {}'.format(key, data))

