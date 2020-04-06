import happybase as hb

db = hb.Connection()

print db.tables()
