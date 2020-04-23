# BASIC.PY
# CREATE ENTRIES INTO THE TABLE

from models import db, Puppy, Toy, Owner

# CREATE TWO PUPPIES
rufus = Puppy('Rufus')
fido = Puppy('Fido')

# ADD  ENTRIES TO DATABASE
db.session.add_all([rufus, fido])
db.session.commit()

# CHECK!
print(Puppy.query.all())

rufus = Puppy.query.filter_by(name = 'Rufus').first()


# CREATE OWNER OBJECT

jose = Owner('Jose', rufus.id)

# GIVE RUFUS SOME TOYS

toy1 = Toy('Chew Toy', rufus.id)
toy2 = Toy('Ball', rufus.id)

db.session.add_all([jose, toy1, toy2])
db.session.commit()

# GRAB RUFUS AFTER THOSE ADDITIONS
rufus = Puppy.query.filter_by(name = 'Rufus').first()
print(rufus)

rufus.report_toys()
