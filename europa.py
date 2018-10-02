from cromulent.model import factory, Actor, Production, BeginningOfExistence, \
	EndOfExistence, TimeSpan, Place, InformationObject, Phase 
from cromulent.vocab import Painting, add_art_setter, PrimaryName, Name, \
	CollectionSet, instances, aat_culture_mapping, LocalNumber, DimensionStatement, \
	MaterialStatement, Gallery, MuseumPlace, Signature, BottomPart, \
	Description, RightsStatement, MuseumOrg, Purchase, Exhibition, ExhibitionPlace, \
	MultiExhibition 
factory.id_type_label = True
add_art_setter()

obj = Painting("http://www.getty.edu/art/collection/objects/882/rembrandt-harmensz-van-rijn-the-abduction-of-europa-dutch-1632/", 
	label="The Abduction of Europa", art=1)
# Title
obj.identified_by = PrimaryName(label="Title", value="The Abduction of Europa")
obj.identified_by = Name(label="ALternate Title", value="El rapto de Europa (Published Title)")

prod = Production()
obj.produced_by = prod 

# Collection
col = CollectionSet("http://www.getty.edu/art/collection/", label="The J. Paul Getty Museum Collection")
obj.aggregated_by = col 

# Artist info
artist = Actor("http://www.getty.edu/art/collection/artists/469/rembrandt-harmensz-van-rijn-dutch-1606-1669/", label="Artist")
artist.identified_by = PrimaryName(value="Rembrandt Harmensz. van Rijn")
artist.classified_as = instances["dutch nationality"]
birth = BeginningOfExistence()
btime = TimeSpan(label="1606")
btime.begin_of_the_begin = "1606-01-01T00:00:00Z" 
btime.end_of_the_end = "1607-01-01T00:00:00Z"
birth.timespan = btime
death = EndOfExistence()
dtime = TimeSpan(label="1669")
dtime.begin_of_the_begin = "1669-01-01T00:00:00Z"
dtime.end_of_the_end = "1670-01-01T00:00:00Z"
death.timespan = dtime
artist.brought_into_existence_by = birth
artist.taken_out_of_existence_by = death
prod.carried_out_by = artist

# # Culture
# obj.genre = aat_culture_mapping["dutch"]

# Production date
date = TimeSpan(label="1632")
date.begin_of_the_begin = "1632-01-01T00:00:00Z"
date.end_of_the_end = "1633-01-01T00:00:00Z"
prod.timespan = date

# Object No.
loc_no = LocalNumber(label="Object Number", value="95.PB.7")
obj.identified_by = loc_no

# Dimensions and Materials
dim = DimensionStatement(label="Dimensions", value="64.6 x 78.7 cm (25 7/16 x 31 in.)")
mat = MaterialStatement(label="Medium", value="Oil on single oak panel")
obj.referred_to_by = dim
obj.referred_to_by = mat

# Current location
loc = Gallery(label="Gallery E205")
mu = MuseumPlace(label="Museum East Pavillion")
place = Place(label="The Getty Center")
loc.part_of = mu
mu.part_of = place 
obj.current_location = loc

# Signature
sign = Signature(label="RHL [in ligature]. van Rÿn.1632")
bpart = BottomPart(label="Lower Right")
bpart.carries = sign
obj.part = bpart

# Description
des = Description(label="Description", value="In the Metamorphoses, the ancient Roman poet Ovid told a story about the god Jupiter, who disguised himself as a white bull in order to seduce the princess Europa away from her companions and carry her across the sea to the distant land that would bear her name.\nDuring his long career Rembrandt rarely painted mythological subjects. Here he conveys a narrative story through dramatic gesture and visual effects. Bewildered, Europa grasps the bull's horn, digs her fingers into his neck, and turns back to look at her companions on the water's edge. One young woman falls to the ground and raises her arms in alarm, dropping the flower garland intended for the bull's neck into her lap, while her friend clasps her hands in consternation and watches helplessly. The carriage driver above rises to his feet and stares at the departing princess in horror. In the background, a city shrouded in mist extends along the horizon, perhaps serving as an allusion to the ancient city of Tyre as well as to contemporary Amsterdam.The dark thicket of trees to the right contrasts with the pink and blue regions of the sea and sky. Sunlight breaks through the clouds and reflects off the water, but the sky behind the trees is dark and foreboding.\nA master of visual effects, Rembrandt took pleasure in describing the varied textures of sumptuous costumes and glittering gold highlights on the carriage and dresses.")
obj.referred_to_by = des

# IIIF digital image
dimg = InformationObject("http://media.getty.edu/viewers/mirador/?manifest=https://data.getty.edu/museum/api/iiif/882/manifest.json")
io = InformationObject("http://iiif.io/api/presentation")
dimg.conforms_to = io
dimg.format = "application/ld+json;profile=\"http://iiif.io/api/presentation/2/context.json\""
rights = RightsStatement("http://www.getty.edu/about/whatwedo/opencontent.html", label="Open Content Program", value="This image is available for download, without charge.")
dimg.referred_to_by = rights
obj.subject_of = dimg

# Provenance
owner = MuseumOrg(label="The J. Paul Getty Museum")
purch = Purchase()
purch.carried_out_by = Actor(label="Deborah Gage Works of Art Ltd.")
purch.transferred_title_from = Actor(label="Estate of Leopold Hugo Paul Klotz")
purch.timespan = TimeSpan(label="1995")
purch.took_place_at = Place(label="New York")
owner.acquired_title_through = purch
obj.current_owner = owner

# Exhibitions
exh1 = Exhibition(label="Masterpieces of Art (European Paintings and Sculpture from 1300-1800)")
pl1 = ExhibitionPlace(label="New York World's Fair")
exh1.took_place_at = pl1
pl1.part_of = Place(label="Queens")
extime1 = TimeSpan(label="1939")
extime1.begin_of_the_begin = "1939-05-01"
extime1.end_of_the_end = "1939-10-01"
exh1.timespan = extime1
obj.used_for = exh1

exh2 = Exhibition(label="A Loan Exhibition of Rembrandt")
pl2 = ExhibitionPlace(label="Wildenstein & Co.")
exh2.took_place_at = pl2
pl2.part_of = Place(label="New York")
extime2 = TimeSpan(label="1950")
extime2.begin_of_the_begin = "1950-01-19"
extime2.end_of_the_end = "1950-02-25"
exh2.timespan = extime2
obj.used_for = exh2

exh3 = MultiExhibition(label="The Age of Rembrandt")
extime3 = TimeSpan(label="1966-1967")
extime3.begin_of_the_begin = "1966-10-10"
extime3.end_of_the_end = "1967-03-05"
exh3.timespan = extime3

exh31 = Exhibition(label="Exhibition at first location")
pl31 = ExhibitionPlace(label="The Fine Arts Museums of San Francisco")
exh31.took_place_at = pl31
pl31.part_of = Place(label="San Francisco")
extime31 = TimeSpan(label="1966")
extime31.begin_of_the_begin = "1966-10-10"
extime31.end_of_the_end = "1966-11-13"
exh31.timespan = extime31

exh32 = Exhibition(label="Exhibition at second location")
pl32 = ExhibitionPlace(label="Toledo Museum of Art")
exh31.took_place_at = pl32
pl32.part_of = Place(label="Toledo")
extime32 = TimeSpan(label="1966-1967")
extime32.begin_of_the_begin = "1966-11-26"
extime32.end_of_the_end = "1967-01-08"
exh32.timespan = extime32

exh33 = Exhibition(label="Exhibition at third location")
pl33 = ExhibitionPlace(label="Museum of Fine Arts")
exh33.took_place_at = pl33
pl33.part_of = Place(label="Boston")
extime33 = TimeSpan(label="1967")
extime33.begin_of_the_begin = "1967-01-21"
extime33.end_of_the_end = "1967-03-05"
exh33.timespan = extime33

exh3.part = exh31
exh3.part = exh32
exh3.part = exh33
obj.used_for = exh3

exh4 = Exhibition(label="The Glory of the Golden Age")
pl4 = ExhibitionPlace(label="Rijksmuseum")
exh4.took_place_at = pl4
pl4.part_of = Place(label="Amsterdam")
extime4 = TimeSpan(label="2000")
extime4.begin_of_the_begin = "2000-04-15"
extime4.end_of_the_end = "2000-09-17"
exh4.timespan = extime4
obj.used_for = exh4

exh5 = Exhibition(label="Rembrandt: Pintor de Historias")
pl5 = ExhibitionPlace(label="Museo del Prado")
exh5.took_place_at = pl5
pl5.part_of = Place(label="Madrid")
extime5 = TimeSpan(label="2008-2009")
extime5.begin_of_the_begin = "2008-10-15"
extime5.end_of_the_end = "2009-01-06"
exh5.timespan = extime5
obj.used_for = exh5


print(factory.toString(obj, compact=False))











