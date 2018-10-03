from cromulent.model import factory, ManMadeObject, Material, Type, Place
from cromulent.vocab import AccessionNumber, PrimaryName, Name, Color

factory.validate_profile = False

# Can create a class "Samples" - aat:300028825
s = ManMadeObject(label="Sample Object")

# AccessionNumber is used for now, will a new class Barcode - aat:300343361
s.identified_by = AccessionNumber(label="Full Barcode", value="WOOD10001") 
s.identified_by = AccessionNumber(label="Old Barcode", value="TIM0001")
s.identified_by = PrimaryName(label="Common Name", value="Pine, Shortleaf")
s.identified_by = Name(label="Additional Names", value="Pinus echinata")

# Need vocab for specific class and instances
s.classified_as = Material(label="Sample Type", value="Wood")
s.classified_as = Material(label="Physical Form", value="N/A")
s.dimension = Color(value="N/A")
s.classified_as = Type(label="Natural/Synthetic", value="Natural")
s.current_location = Place(label="Grid Location", value="8-A-1")
s.as_general_use = Type(label="Typical Use", value="Construction Material")

# Index (CI) No., Preparation, Certified Standard

print(factory.toString(s, compact=False))