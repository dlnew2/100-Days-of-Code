
#
#
# def greet(name):
#     print(f"hello {name}")
#     print(f"this {name}")
#     print(f"function {name}")
#
#
# name_input = input("what is your name")
#
# greet(name_input)

def calculate_love_score(name1, name2):
    test1 = ["t", "r", "u", "e"]
    test2 = ["l", "o", "v", "e"]
    score1 = 0
    score2 = 0
    combined_name = (name1 + " " + name2).lower()
    for letter in test1:
        score1 += combined_name.count(letter)
    for letter in test2:
        score2 += combined_name.count(letter)
    # print(combined_name)
    print(f"{score1}{score2}")


calculate_love_score("Kanye West", "Kim Kardashian")