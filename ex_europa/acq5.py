# Sold by the estate of Jeanne Baptiste d'Albert de Luynes

from cromulent.model import factory, TimeSpan, Aggregation, Actor, Place
from cromulent.vocab import Painting, add_art_setter, LotNumber, Purchase, Description

add_art_setter()

acq = Purchase()
lot = Aggregation(label="Verrue sale, lot 87")
acq2 = Purchase()
obj = Painting("http://www.getty.edu/art/collection/objects/882/rembrandt-harmensz-van-rijn-the-abduction-of-europa-dutch-1632/", label="The Abduction of Europa", art=1)
est = Actor(label="The estate of Jeanne Baptiste d'Albert de Luynes, comtesse de Verrue")

lot.identified_by = LotNumber(value="87")
lot.aggregates = obj 

# Date of Acquisition
date = TimeSpan()
date.begin_of_the_begin = "1737-03-27T00:00:00Z"
date.end_of_the_end = "1737-03-27T23:59:59Z"


# Description 
des = Description(value="1736 - 1737: Estate of Jeanne Baptiste d'Albert de Luynes, comtesse de Verrue, 1670 - 1736 [sold, Verrue sale, Paris, March 27, 1737, lot 87.]")


acq.used_specific_object = lot
acq.part = acq2
acq2.timespan = date
acq2.transferred_title_from = est
acq2.transferred_title_of = obj
acq2.referred_to_by = des

print(factory.toString(acq, compact=False)) 