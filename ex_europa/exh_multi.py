# Travelling Exhibitions

from cromulent.model import factory, Place, TimeSpan, Aggregation
from cromulent.vocab import Painting, add_art_setter, ExhibitionIdea, MultiExhibition, \
	Exhibition, Name, MuseumPlace

add_art_setter() 

i = ExhibitionIdea(label="The Age of Rembrandt")
obj = Painting("http://www.getty.edu/art/collection/objects/882/rembrandt-harmensz-van-rijn-the-abduction-of-europa-dutch-1632/", 
	label="The Abduction of Europa", art=1)

e = MultiExhibition(label="The Age of Rembrandt")
d = TimeSpan(label="1966-1967")
d.begin_of_the_begin = "1966-10-10T00:00:00Z"
d.end_of_the_end = "1967-03-05T23:59:59Z"
e.timespan = d 

e1 = Exhibition(label="Exhibition at first location")
c1 = Aggregation()
l1 = MuseumPlace(label="The Fine Arts Museums of San Francisco")
e1.took_place_at = l1
l1.part_of = Place(label="San Francisco")
d1 = TimeSpan(label="1966")
d1.begin_of_the_begin = "1966-10-10T00:00:00Z"
d1.end_of_the_end = "1966-11-13T23:59:59Z"
e1.timespan = d1
c1.aggregates = obj 
e1.used_specific_object = c1

e2 = Exhibition(label="Exhibition at second location")
c2 = Aggregation()
l2 = MuseumPlace(label="Toledo Museum of Art")
e2.took_place_at = l2
l2.part_of = Place(label="Toledo")
d2 = TimeSpan(label="1966-1967")
d2.begin_of_the_begin = "1966-11-26T00:00:00Z"
d2.end_of_the_end = "1967-01-08T23:59:59Z"
e2.timespan = d2
c2.aggregates = obj 
e2.used_specific_object = c2

e3 = Exhibition(label="Exhibition at third location")
c3 = Aggregation()
l3 = MuseumPlace(label="Museum of Fine Arts")
e3.took_place_at = l3
l3.part_of = Place(label="Boston")
d3 = TimeSpan(label="1967")
d3.begin_of_the_begin = "1967-01-21T00:00:00Z"
d3.end_of_the_end = "1967-03-05T23:59:59Z"
e3.timespan = d3
c3.aggregates = obj 
e3.used_specific_object = c3

i.identified_by = Name(value="The Age of Rembrandt")
i.motivated = e 
e.part = e1
e.part = e2
e.part = e3

print(factory.toString(i, compact=False))

