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
        print("\n tip: to select the choice, type the letter assigned to it or else \n") 
        right = False
    else:
        print("try again")
#provides the first scenario and the two paths you could take
print(scenarios.scen.get(1))
answer = input().lower()
while answer != "a" and answer != "b": #if the answer is wrong, it provides this result, if not it leads to next scenario
    print("try again") 
    print(scenarios.scen.get(1))
    answer = input().lower()
if answer == "a": #if you choose this choice you get this specific scenario
    print(scenarios.ans.get("1a"))
elif answer == "b":
    print(scenarios.scen.get("1b"))
