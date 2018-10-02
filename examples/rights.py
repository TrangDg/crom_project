# Example of Credit/Attribution Statement

# from cromulent.model import factory
# from cromulent.vocab import Painting, CreditStatement, add_art_setter
# add_art_setter()
# obj = Painting("https://linked.art/example/object/64", "Example Painting", art=1)
# credit = CreditStatement("https://linked.art/example/text/26", value="Donation of Ms J. Smith; Example Organization")
# obj.referred_to_by = credit
# print(factory.toString(obj, compact=False))






# Example of Rights Statement

# from cromulent.model import factory
# from cromulent.vocab import Painting, RightsStatement, add_art_setter
# add_art_setter()
# obj = Painting("https://linked.art/example/object/65", "Example Painting", art=1)
# rights = RightsStatement("https://linked.art/example/text/27", value="Copyright of this object has not yet been assessed")
# obj.referred_to_by = rights 
# print(factory.toString(obj, compact=False))







# Example of Rights Assertions

from cromulent.model import factory
from cromulent.vocab import Painting, RightsStatement, add_art_setter
add_art_setter()
obj = Painting("https://linked.art/example/object/66", "Object", art=1)
rights = RightsStatement("http://rightsstatements.org/vocab/NKC/1.0/", "No known copyright")
obj.referred_to_by = rights
print(factory.toString(obj, compact=False))