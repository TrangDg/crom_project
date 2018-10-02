from cromulent.model import factory, Person

p = Person("Mother")
p2 = Person("Son")
p3 = Person("Daughter")
p.parent_of = p2
p.parent_of = p3
parent_of._factory.validate_profile = False

print (factory.toString(p, compact=False))


