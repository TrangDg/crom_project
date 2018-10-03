from cromulent.model import factory, Actor, Production, BeginningOfExistence, \
	EndOfExistence, TimeSpan, Place, InformationObject, Phase, VisualItem 
from cromulent.vocab import Painting, add_art_setter, PrimaryName, Name, \
	CollectionSet, instances, aat_culture_mapping, AccessionNumber, Height, Width, \
	SupportPart, Gallery, MuseumPlace, Signature, BottomPart, \
	Description, RightsStatement, MuseumOrg, Purchase

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

# Culture
vitem = VisualItem()
vitem.style = instances["dutch nationality"]
obj.shows = vitem 

# Production date
date = TimeSpan(label="1632")
date.begin_of_the_begin = "1632-01-01T00:00:00Z"
date.end_of_the_end = "1633-01-01T00:00:00Z"
prod.timespan = date

# Object No.
loc_no = AccessionNumber(label="Object Number", value="95.PB.7")
obj.identified_by = loc_no

# Dimensions 
h_cm = Height(label="Height in centimeter", value=64.6)
h_cm.unit = instances["cm"]
w_cm = Width(label="Wisth in centimiter", value=78.7)
w_cm.unit = instances["cm"]
h_in = Height(label="Height in inches", value=25+(7/16))
h_in.unit = instances["inches"]
w_in = Width(label="Width in inches", value=31)
w_in.unit = instances["inches"]
obj.dimension = h_cm
obj.dimension = w_cm
obj.dimension = h_in
obj.dimension = w_in

# Materials
sup = SupportPart(label="Single oak panel")
obj.made_of = instances["oil"]
obj.part = sup 
sup.made_of = instances["oak"]

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


print(factory.toString(obj, compact=False))











