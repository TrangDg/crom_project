# Example of Description

# from cromulent.model import factory
# from cromulent.vocab import Painting, Description, add_art_setter
# add_art_setter()

# obj = Painting("https://linked.art/example/object/33", "Example Painting", art=1)
# des = Description("https://linked.art/example/text/22", value="The Example Painting is a great example of exampleness.")
# obj.referred_to_by = des
# print(factory.toString(obj, compact=False))




# Example of Related Object 

# from cromulent.model import factory
# from cromulent.vocab import Painting, Description, add_art_setter
# add_art_setter()
# obj = Painting("https://linked.art/example/object/34", "Another Example Painting", art=1)
# obj2 = Painting("https://linked.art/example/object/35", "Yet Another Example Painting", art=1)
# obj.related = obj2
# print(factory.toString(obj, compact=False))






# Example of Depiction

# from cromulent.model import factory, Production, VisualItem, Actor
# from cromulent.vocab import Painting, Description, add_art_setter
# add_art_setter()
# obj = Painting("https://linked.art/example/object/36", "Self Portrait")
# prod = Production("https://linked.art/example/activity/26")
# person = Actor("https://linked.art/example/actor/3", "Artist")
# vitem = VisualItem("https://linked.art/example/VisualItem/1")
# obj.produced_by = prod
# prod.carried_out_by = person
# obj.shows = vitem
# vitem.represents = person
# print(factory.toString(obj, compact=False))




# Example of Subject

# from cromulent.model import factory, VisualItem
# from cromulent.vocab import Painting, instances, add_art_setter
# add_art_setter()
# obj = Painting("https://linked.art/example/object/37", "Portrait of Lord Nelson", art=1)
# vitem = VisualItem("https://linked.art/example/VisualItem/2")
# sub = instances["war"]
# obj.shows = vitem
# vitem.about = sub
# print(factory.toString(obj, compact=False))







# Example of Style 

from cromulent.model import factory, VisualItem
from cromulent.vocab import Painting, add_art_setter, instances
add_art_setter()
obj = Painting("https://linked.art/example/object/38", "Example Impressionist Painting", art=1)
vitem = VisualItem("https://linked.art/example/VisualItem/3")
style = instances["impressionism"]
obj.shows = vitem
vitem.style = style
print(factory.toString(obj, compact=False))






# Example of Classification

# from cromulent.model import factory, VisualItem
# from cromulent.vocab import Painting, instances

# obj = Painting("https://linked.art/example/object/39", "Example Landscape Painting")
# vitem = VisualItem("https://linked.art/example/VisualItem/4")
# clas = instances["landscapes"]
# obj.shows = vitem
# vitem.classified_as = clas 
# print(factory.toString(obj, compact=False))
