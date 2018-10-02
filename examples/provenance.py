# Example of Production

# from cromulent.model import factory, Production, Person 
# from cromulent.vocab import Painting, add_art_setter
# add_art_setter()

# artist = Person("https://linked.art/example/person/23", "Artist")
# prod = Production("https://linked.art/example/activity/27", "Production of Painting")
# obj = Painting("https://linked.art/example/object/61", "Painting", art=1)
# obj.produced_by = prod
# prod.carried_out_by = artist

# print(factory.toString(obj, compact=False))





# Example of Ownership

# from cromulent.model import factory, Acquisition
# from cromulent.vocab import Painting, MuseumOrg, add_art_setter
# add_art_setter()
# acq = Acquisition("https://linked.art/example/activity/28", "Acquisition of Painting")
# org = MuseumOrg("https://linked.art/example/group/16", "Museum")
# obj = Painting("https://linked.art/example/object/62", "Painting", art=1)
# obj.current_owner = org
# org.acquired_title_through = acq 
# print(factory.toString(obj, compact=False))




# Example of Location

from cromulent.model import factory, Place
from cromulent.vocab import Painting, add_art_setter
add_art_setter()
loc = Place("https://linked.art/example/place/8", "Gallery W6")
obj = Painting("https://linked.art/example/object/63", "Painting", art=1)
obj.current_location = loc 
print(factory.toString(obj, compact=False))