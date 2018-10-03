# Acquisition by Jacques Specx

from cromulent.model import factory, TimeSpan, Acquisition, Person, \
	BeginningOfExistence, EndOfExistence, Place, LinguisticObject
from cromulent.vocab import Painting, add_art_setter, Description

add_art_setter()

acq = Acquisition()
obj = Painting("http://www.getty.edu/art/collection/objects/882/rembrandt-harmensz-van-rijn-the-abduction-of-europa-dutch-1632/", label="The Abduction of Europa", art=1)

# Info of acquirer

p = Person(label="Jacques Specx")
birth = BeginningOfExistence(label="Birth")
tob = TimeSpan(label="1585")
tob.begin_of_the_begin = "1585-01-01"
tob.end_of_the_end = "1585-12-31"
pob = Place(label="Amsterdam")
pob.part_of = Place(label="The Netherlands")
birth.timespan = tob 
birth.took_place_at = pob
death = EndOfExistence(label="Death")
tod = TimeSpan(label="1652")
tod.begin_of_the_begin = "1652-01-01"
tod.end_of_the_end = "1652-12-31"
pod = Place(label="Amsterdam")
pod.part_of = Place(label="The Netherlands")
death.timespan = tod 
death.took_place_at = pod
p.brought_into_existence_by = birth
p.taken_out_of_existence_by = death

# Date of Acquisition
date = TimeSpan()
date.begin_of_the_begin = "1632-01-01T00:00:00Z"
date.end_of_the_end = "1652-12-31T23:59:59Z"

# Description and Source
des = Description(value="- 1652: Jacques Specx, 1585 - 1652 (Amsterdam, The Netherlands)")
src = LinguisticObject(label="Source", value="In death inv. of 1652")


acq.transferred_title_of = obj
acq.timespan = date
acq.transferred_title_to = p
acq.referred_to_by = des
acq.referred_to_by = src


print(factory.toString(acq, compact=False)) 




