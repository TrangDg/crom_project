# Transfer from Jeanne Baptiste d'Albert de Luynes to the estate
# upon her death

from cromulent.model import factory, TimeSpan, Acquisition, Person, Actor, \
	BeginningOfExistence, EndOfExistence, Place
from cromulent.vocab import Painting, add_art_setter

add_art_setter()

acq = Acquisition(label="Held in trust by the estate")
obj = Painting("http://www.getty.edu/art/collection/objects/882/rembrandt-harmensz-van-rijn-the-abduction-of-europa-dutch-1632/", label="The Abduction of Europa", art=1)

# Info of acquirer

p = Person(label="Jeanne Baptiste d'Albert de Luynes, comtesse de Verrue")
birth = BeginningOfExistence(label="Birth")
tob = TimeSpan(label="1670")
tob.begin_of_the_begin = "1670-01-01T00:00:00Z"
tob.end_of_the_end = "1670-12-31T23:59:59"
pob = Place(label="Paris")
pob.part_of = Place(label="France")
birth.timespan = tob 
birth.took_place_at = pob
death = EndOfExistence(label="Death")
tod = TimeSpan(label="1736")
tod.begin_of_the_begin = "1736-01-01T00:00:00Z"
tod.end_of_the_end = "1736-12-31T23:59:59Z"
pod = Place(label="Savoy")
pod.part_of = Place(label="France")
death.timespan = tod 
death.took_place_at = pod
p.brought_into_existence_by = birth
p.taken_out_of_existence_by = death

# Estate
est = Actor(label="The estate of Jeanne Baptiste d'Albert de Luynes, comtesse de Verrue")

# Date of Acquisition
date = TimeSpan()
date.begin_of_the_begin = "1736-01-01T00:00:00Z"
date.end_of_the_end = "1736-12-31T23:59:59Z"

acq.transferred_title_of = obj
acq.timespan = date
acq.transferred_title_from = p
acq.transferred_title_to = est



print(factory.toString(acq, compact=False)) 