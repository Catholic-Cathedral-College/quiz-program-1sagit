import scenarios
from time import sleep
#where the scenarios come from
#sets up the intro and responses to it

#asks if the user wants to play and sets up a response if they say no
def intro():
  right = True
  while right:
      print("type yes to start game")
      answer = input().strip().lower()
      if answer == "yes":
          print("\n tip: to select the choice, type the letter assigned to it or else \n") 
          right = False
      else:
          print("try again") 
#provides the first scenario and the two paths you could take
intro()
print(scenarios.scen.get(1))
answer = input().lower().strip()
while answer != "a" and answer != "b": #if the answer is wrong, it provides this result, if not it leads to next scenario
    print("try again") 
    print(scenarios.scen.get(1))
    answer = input().lower()
if answer == "a": #if you choose this choice you get this specific scenario
    print(scenarios.ans.get("1a"))
elif answer == "b":
    print(scenarios.x.get("bx"))
    print("sending you back to the\x1B[3m beginning \x1B[0m")
    sleep(1) #this gives the appearance of the code loading
    print(".")
    sleep(1)
    print(".")
    sleep(1)
    print(".")
    intro() #when the user dies it will give the option of sending them back to the beginning and restarting everything
