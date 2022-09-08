import scenarios
#where the scenarios come from
#sets up the intro and responses to it
right = True
start = input
#asks if the user wants to play and sets up a response if they say no
while right:
    print("type yes to start game")
    answer = input()
    if answer.lower() == "yes":
        right = False
    else:
        print("try again")
#provides the first scenario and the two paths you could take
print(scenarios.scen.get(1))
answer = input().lower()
while answer != "a" and answer != "b":
    print("try again")
    print(scenarios.scen.get(1))
    answer = input().lower()
if answer == "a":
    print(scenarios.scen.get(2))
elif answer == "b":
    print(scenarios.scen.get(3))
