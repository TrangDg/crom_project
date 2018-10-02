# from cromulent.model import factory, Activity, Place, TimeSpan, Actor

# act = Activity("https://linked.art/example/activity/64")
# loc = Place("https://linked.art/example/place/16", "Where")
# tspan = TimeSpan("https://linked.art/example/time/15", "When")
# p = Actor("https://linked.art/example/actor/17", "Who")
# act.took_place_at = loc
# act.timespan = tspan
# tspan.end_of_the_end = "latest-end-dateime"
# tspan.begin_of_the_begin = "earliest-start-datetime"
# act.carried_out_by = p 
# print(factory.toString(act, compact=False))








# from cromulent.model import factory, Production, Place, TimeSpan, Actor
# from cromulent.vocab import Painting, add_art_setter
# add_art_setter()
# prod = Production("https://linked.art/example/activity/70")
# loc = Place("https://linked.art/example/place/18", "Example Artist's Studio")
# tspan = TimeSpan("https://linked.art/example/time/20", "When")
# p = Actor("https://linked.art/example/actor/19", "Example Artist")
# obj = Painting("https://linked.art/example/object/85", "Example Painting", art=1)
# prod.produced = obj
# prod.took_place_at = loc
# prod.timespan = tspan
# tspan.end_of_the_end = "1780-03-06T00:00:00Z"
# tspan.begin_of_the_begin = "1780-03-05T00:00:00Z"
# prod.carried_out_by = p 
# print(factory.toString(prod, compact=False))




# from cromulent.model import factory, Production, Person
# from cromulent.vocab import Painting, add_art_setter
# add_art_setter()
# prod = Production("https://linked.art/example/activity/71")
# copy = Painting("https://linked.art/example/object/86", "Copy of Example Painting", art=1)
# org = Painting("https://linked.art/example/object/87", "Example Painting", art=1)
# p = Person("https://linked.art/example/person/35", "Copyist")
# prod.produced = copy
# prod.influenced_by = org
# prod.carried_out_by = p 
# print(factory.toString(prod, compact=False))







# from cromulent.model import factory, Production, VisualItem
# from cromulent.vocab import Negative
# prod = Production("https://linked.art/example/activity/72", "Printing of Photograph")
# src = Negative("https://linked.art/example/object/89", "Negative")
# vi = VisualItem("https://linked.art/example/VisualItem/6", "Visual Content of Photographs and Negative")
# prod.used_specific_object = src
# src.shows = vi 
# print(factory.toString(prod, compact=False))



# Example of Destructiom

from cromulent.model import factory, Destruction, TimeSpan
from cromulent.vocab import Painting, add_art_setter
add_art_setter()
prod = Destruction("https://linked.art/example/activity/80")
obj = Painting("https://linked.art/example/object/94", "Example Destroyed Painting", art=1)
tspan = TimeSpan("https://linked.art/example/time/22")
prod.timespan = tspan
tspan.begin_of_the_begin = "1823-03-01T00:00:00Z"
tspan.end_of_the_end = "1823-03-31T00:00:00Z"
prod.destroyed = obj
print(factory.toString(prod, compact=False))


