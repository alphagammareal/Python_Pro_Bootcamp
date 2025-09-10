# Love Calculator
# 💪 This is a difficult challenge! 💪
# You are going to write a function called calculate_love_score() that tests the compatibility between two names.
# To work out the love score between two people:
# 1. Take both people's names and check for the number of times the letters in the word TRUE occurs.
# 2. Then check for the number of times the letters in the word LOVE occurs.
# 3. Then combine these numbers to make a 2 digit number and print it out.

# e.g.
# name1 = "Angela Yu" name2 = "Jack Bauer"
# T occurs 0 times
# R occurs 1 time
# U occurs 2 times
# E occurs 2 times
# Total = 5
# L occurs 1 time
# O occurs 0 times
# V occurs 0 times
# E occurs 2 times
# Total = 3
# Love Score = 53

def calculate_love_score(name1, name2):
    combined_name = (name1 + name2).lower()
    #  counting True in combined name
    t = combined_name.count("t")
    r = combined_name.count("r")
    u = combined_name.count("u")
    e = combined_name.count("e")
    # counting love in combined name
    l = combined_name.count("l")
    o = combined_name.count("o")
    v = combined_name.count("v")
    love_e = combined_name.count("e")
    # finding total score
    total_true = str(sum([t,r,u,e]))
    total_love = str(sum([l, o, v, love_e]))
    total_score = total_true + total_love
    # print(type(total_score))
    print(f"Love score is {total_score}")

calculate_love_score("Angela Yu", "Jack Bauer")
calculate_love_score("Alpha Coder", "Lovelina Python")