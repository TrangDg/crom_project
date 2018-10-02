from cromulent.model import factory, Phase, TimeSpan, Acquisition, Actor, \
	BeginningOfExistence, EndOfExistence, Place, TransferOfCustody
from cromulent.vocab import Painting, add_art_setter
add_art_setter()

prov = Phase(label="Provenance of The Abduction of Europa by Rembrandt")
obj = Painting("http://www.getty.edu/art/collection/objects/882/rembrandt-harmensz-van-rijn-the-abduction-of-europa-dutch-1632/", label="The Abduction of Europa", art=1)

# First Acquisition  
# acq1 = Acquisition()

p1 = Actor(label="Jacques Specx")
b1 = BeginningOfExistence()
bt1 = TimeSpan(label="1585")
bt1.begin_of_the_begin = "1585-01-01"
bt1.end_of_the_end = "1585-12-31"
bp1 = Place(label="Amsterdam")
bp1.part_of = Place(label="The Netherlands")
b1.timespan = bt1
b1.took_place_at = bp1
d1 = EndOfExistence()
dt1 = TimeSpan(label="1652")
dt1.begin_of_the_begin = "1652-01-01"
dt1.end_of_the_end = "1652-12-31"
dp1 = Place(label="Amsterdam")
dp1.part_of = Place(label="The Netherlands")
d1.timespan = dt1 
d1.took_place_at = dp1
p1.brought_into_existence_by = b1
p1.taken_out_of_existence_by = d1 

# acq1.transferred_title_of = obj
# acq1.transferred_title_to = p1 

# Phase 1
pha1 = Phase(label="Ownership by Jacques Specx")
dur1 = TimeSpan(label="- 1652")
dur1.end_of_the_end = "1652-12-31"
pha1.timespan = dur1
pha1.related_entity = p1 

# Second Acquisition
# acq2 = Acquisition()

p2 = Actor(label="Jeanne Baptiste d'Albert de Luynes, comtesse d Verrue")
b2 = BeginningOfExistence()
bt2 = TimeSpan(label="1670")
bt2.begin_of_the_begin = "1670-01-01"
bt2.end_of_the_end = "1670-12-31"
bp2 = Place(label="Paris")
bp2.part_of = Place(label="France")
b2.timespan = bt2
b2.took_place_at = bp2
d2 = EndOfExistence()
dt2 = TimeSpan(label="1736")
dt2.begin_of_the_begin = "1736-01-01"
dt2.end_of_the_end = "1736-12-31"
dp2 = Place(label="Savoy")
dp2.part_of = Place(label="France")
d2.timespan = dt2
d2.took_place_at = dp2
p2.brought_into_existence_by = b2
p2.taken_out_of_existence_by = d2 

# acq2.transferred_title_of = obj 
# acq2.transferred_title_to = p2

# Phase 2
pha2 = Phase(label="Ownership by Jeanne Baptiste d'Albert de Luynes, comtesse de Verrue")
dur2 = TimeSpan(label=" - 1736")
dur2.end_of_the_end = "1736-12-31"
pha2.timespan = dur2
pha2.related_entity = p2 

# Transfer of Custody
toc1 = TransferOfCustody()
est2 = Actor(label="Estate of Jeanne Baptiste d'Albert de Luynes, comtesse de Verrue")
toc1.transferred_custody_of = obj
toc1.transferred_custody_from = p2
toc1.transferred_custody_to = est2

# Phase 3
pha3 = Phase(label="Held in trust by the estate of Jeanne Baptiste d'Albert de Luynes")
dur3 = TimeSpan(label="1736-1737")
dur3.begin_of_the_begin = "1736-12-31"
dur3.end_of_the_end = "1737"

prov.part = acq1
prov.part = pha1
prov.part = acq2
prov.part = pha2



prov.phase_of = obj 

print(factory.toString(prov, compact=False)) 