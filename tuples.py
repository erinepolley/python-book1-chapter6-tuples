zoo = ("aardvark", "cheetah", "elephant", "giraffe", "monkey", "hippo", "flamingo", "heron", "rabbit", "frogs")

(first, second, third, fourth, fifth, sixth, seventh, eighth, ninth, tenth) = zoo

print(first)

animal = "flamingo"
if animal in zoo:
    print(f'There is a {animal} in the zoo!')
else:
    print(f'Sorry, we couldn\'t find a {animal} in the zoo.')

zoo_list = list(zoo)
print(zoo_list)

zoo_extend = ["dingo", "cat", "bat"]
zoo_list.extend(zoo_extend)
print(zoo_list)

print(tuple(zoo_list))
print(zoo_list)
