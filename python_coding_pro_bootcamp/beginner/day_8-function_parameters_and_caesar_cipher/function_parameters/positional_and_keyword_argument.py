
# Positional Argument
# functions with more than one input
def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}")

greet_with("alpha", "ayeduase")


# using keyword argument
# greet_with ("Nowhwere", "Jack")
greet_with(name = "Jack", location = "nowhere")
greet_with(location = "nowhere", name = "Alpha")