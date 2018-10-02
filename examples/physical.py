# Example of Dimensions

# from cromulent.model import factory
# from cromulent.vocab import Painting, Width, Height, add_art_setter, instances
# add_art_setter()

# obj = Painting("https://linked.art/example/object/51", "Example 16x20 Painting", art=1)
# w = Width("https://linked.art/example/value/6", value=16)
# h = Height("https://linked.art/example/value/7", value=20)
# inch = instances["inches"]
# w.unit = inch
# h.unit = inch
# obj.dimension = w
# obj.dimension = h
# print(factory.toString(obj, compact=False))





# Example of Dimension Statement

# from cromulent.model import factory
# from cromulent.vocab import Painting, add_art_setter, DimensionStatement
# add_art_setter()

# obj = Painting("https://linked.art/example/object/52", "Example Painting", art=1)
# ds = DimensionStatement("https://linked.art/example/text/23", value="The painting is approximately 16 inches wide, by 20 inches high")
# obj.referred_to_by = ds
# print(factory.toString(obj, compact=False))






# Example of Shapes

# from cromulent.model import factory
# from cromulent.vocab import Painting, add_art_setter, instances
# add_art_setter()

# obj = Painting("https://linked.art/example/object/53", "Example oval Painting", art=1)
# shape = instances["oval"]
# obj.classified_as = shape
# print(factory.toString(obj, compact=False))






# Example of Materials

# from cromulent.model import factory
# from cromulent.vocab import Sculpture, add_art_setter, instances
# add_art_setter()

# obj = Sculpture("https://linked.art/example/object/54", "Example Marble Sculpture", art=1)
# mat = instances["marble"]
# obj.made_of = mat 
# print(factory.toString(obj, compact=False))








# Example of Material Statement

# from cromulent.model import factory
# from cromulent.vocab import Painting, add_art_setter, MaterialStatement
# add_art_setter()

# obj = Painting("https://linked.art/example/object/55", "Example Multi-Media Painting", art=1)
# ms = MaterialStatement("https://linked.art/example/text/24", value="Oil, French Watercolors on Paper, Graphite and Ink on Canvas, with an Oak frame")
# obj.referred_to_by = ms
# print(factory.toString(obj, compact=False))







# Example of Parts

# from cromulent.model import factory
# from cromulent.vocab import Painting, add_art_setter, instances, SupportPart
# add_art_setter()

# obj = Painting("https://linked.art/example/object/56", "Example Painting", art=1)
# part = SupportPart("https://linked.art/example/object/56/part/1", "Canvas Support")
# mat = instances["watercolor"]
# pmat = instances["canvas"]
# obj.made_of = mat
# obj.part = part
# part.made_of = pmat
# print(factory.toString(obj, compact=False))










# Example of Sides of an object

from cromulent.model import factory, VisualItem, LinguisticObject, ManMadeObject
from cromulent.vocab import PhotographColor, add_art_setter, FrontPart, BackPart
add_art_setter()

obj = PhotographColor("https://linked.art/example/object/57", "Photograph of Example Artwork")
front = FrontPart("https://linked.art/example/object/58", "Front of Photograph", art=1)
back = BackPart("https://linked.art/example/object/59", "Back of Photograph")
vi = VisualItem("https://linked.art/example/VisualItem/5")
awork = ManMadeObject("https://linked.art/example/object/60", "Example Artwork", art=1)
lo = LinguisticObject("https://linked.art/example/text/25", value="Photograph of Example Artwork, taken 1932")
obj.part = front
obj.part = back
front.shows = vi
vi.represents = awork 
back.carries = lo 
print(factory.toString(obj, compact=False))









