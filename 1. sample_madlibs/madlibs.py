# https://www.youtube.com/watch?v=8ext9G7xspg&t=8369s
# reference link: https://github.com/kying18/beginner-projects/tree/master/sample_madlibs

# string concatenation (aka how to put strings together)
# suppose we want to create a string that says "subscribe to ____"

youtuber = "Francesco Gaudiello"

# a few ways to do this
print("subscribe to " + youtuber)
print("subscribe to {}".format(youtuber))
print(f"subscribe to {youtuber}")

adj = input("Adjective: ")
verb1 = input("Verb: ")
verb2 = input("Verb: ")
famous_person = input("Famous person: ")

madlib = f"Computer programming is so {adj}! It makes me so excited all the time because " \
         f"I love to {verb1}. Stay hydrated and {verb2} like you are {famous_person}!"

print(madlib)

