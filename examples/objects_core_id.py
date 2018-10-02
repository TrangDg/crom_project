from cromulent.model import factory, Aggregation



# Example of URI and Non-URI Identifiers:

# from cromulent.vocab import Painting, AccessionNumber, LocalNumber, add_art_setter
# add_art_setter()
# acc_num = AccessionNumber("https://linked.art/example/identifier/7", "Accession Number for Painting", "X198-093")
# loc_num = LocalNumber("https://linked.art/example/identifier/8", "Local Repository Number", 677)
# obj = Painting("https://linked.art/example/object/46", "Example Painting", art=1)

# obj.identified_by = acc_num
# obj.identified_by = loc_num

# print (factory.toString(obj, compact=False))




# Example of Context for Non-URI Identifiers

from cromulent.vocab import Painting, AccessionNumber, add_art_setter
add_art_setter - 
acc_num = AccessionNumber("https://linked.art/example/identifier/9", value="P1998-27")
aggr = Aggregation("https://linked.art/example/set/15", label="Paintings Collection")
o = Painting("https://linked.art/example/object/47", label="Example Painting", art=1)
o.identified_by = acc_num
o.aggregated_by = aggr 
print (factory.toString(o, compact=False))





# Example of Titles

# from cromulent.vocab import Painting, PrimaryName, Name, add_art_setter
# add_art_setter()
# ptitle = "Self Portrait"
# atitle = "Portrait of the Artist"
# prim_name = PrimaryName("https://linked.art/example/name/16", value=ptitle)
# alt_name = Name("https://linked.art/example/name/18", value=atitle)
# obj = Painting("https://linked.art/example/object/48", label=ptitle, art=1)
# obj.identified_by = prim_name 
# obj.identified_by = alt_name
# print(factory.toString(obj, compact=False))





