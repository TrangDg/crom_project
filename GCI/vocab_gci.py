
from cromulent.model import Type, Identifier
from cromulent.vocab import instances, register_aat_class


register_aat_class("Barcode", Identifier, "300343361", "Barcode")
register_aat_class("CatalogNumber", Identifier, "300404620", "Catalog Number")

# Grid Location
# cat = Type("http://vocab.getty.edu/page/aat/300404620", label="Catalog Number")

notes = Type("http://vocab.getty.edu/aat/300027200", label="Notes")

natural = Type("http://vocab.getty.edu/aat/300219527", label="Natural")
synthetic = Type("http://vocab.getty.edu/aat/300218678", label="Synthetic")

# Physical form
opaque = Type("http://vocab.getty.edu/aat/300056216", label="opaque")
liquid = Type("http://vocab.getty.edu/aat/300015378", label="liquid")

# Sample Type
wood = Type("http://vocab.getty.edu/aat/300011914", label="Wood")
oleoresin = Type("http://vocab.getty.edu/aat/300012891", label="Oleoresin / Balsam")

# Typical Use
construction = Type("http://vocab.getty.edu/aat/300014857", label="Construction Material")



# instances["catalog number"]
instances["notes"] = notes 
instances["natural"] = natural 
instances["synthetic"] = synthetic
instances["opaque"] = opaque  
instances["liquid"] = liquid
instances["wood"] = wood 
instances["oleoresin / balsam"] = oleoresin
instances["construction material"] = construction