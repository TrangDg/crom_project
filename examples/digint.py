# Example of Digital Image

# from cromulent.model import factory
# from cromulent.vocab import Painting, add_art_setter, DigitalImage
# add_art_setter()
# obj =Painting("https://linked.art/example/object/40", "Painting", art=1)
# vi = DigitalImage("http://example.org/images/image.jpg", "Image of Painting")
# obj.representation = vi
# vi.format = "image/jpeg"
# print(factory.toString(obj, compact=False))





# Example of Homepage and Other pages

# from cromulent.model import factory
# from cromulent.vocab import Painting, add_art_setter, WebPage, instances
# add_art_setter()
# obj =Painting("https://linked.art/example/object/41", "Painting", art=1)
# hp = WebPage("http://example.org/collection/1/painting", "Homepage for Painting")
# op = WebPage("http://example.org/journal/article", "Webpage that discusses Painting")
# obj.subject_of = hp
# hp.classified_as = instances["primary"]
# hp.format = "text/html"
# obj.subject_of = op
# op.format = "text/html"
# print(factory.toString(obj, compact=False))







# Example of IIIF Images

from cromulent.model import factory, VisualItem, InformationObject
from cromulent.vocab import Sculpture, add_art_setter

add_art_setter()
obj = Sculpture("https://linked.art/example/object/43", "Sculpture", art=1)
vi = VisualItem("http://iiif.example.org/image/1", "IIIF Image API for Sculpture")
i = InformationObject("http://iiif.io/api/image")
obj.representation = vi
vi.conforms_to = i
print(factory.toString(obj, compact=False))







# Example of IIIF Manifests

# from cromulent.model import factory, InformationObject
# from cromulent.vocab import Painting, add_art_setter
# add_art_setter()
# obj =Painting("https://linked.art/example/object/44", "Painting", art=1)
# io = InformationObject("http://iiif.example.org/presentation//1/manifest.json")
# i = InformationObject("http://iiif.io/api/presentation")
# obj.subject_of = io
# io.conforms_to = i  
# io.format = "application/ld+json;profile=\"http://iiif.io/api/presentation/2/context.json\""
# print(factory.toString(obj, compact=False))
