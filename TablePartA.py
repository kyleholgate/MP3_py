import happybase as hb

db = hb.Connection()

power = {
                'personal': dict(),
                        'professional': dict(),
                                'custom' : dict()
                                    }

food = {
                'nutrition' : dict(),
                        'taste' : dict()
                            }

db.create_table('powers', power)
db.create_table('food', food)
db.close()
