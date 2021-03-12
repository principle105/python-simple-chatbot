# importing dependencies
import json,random
from fuzzywuzzy import fuzz

b,lastresponse = "hi",""

# chat loop
while True:
  # loads the data
  with open("data.json", "r") as f:
    data = json.load(f)

  # gets the user input
  userInput = input("").lower()

  mostsimilar,score = "",0

  # finds the most similar sentence to the user input from the data
  for d in data:
    if (s := fuzz.ratio(userInput,d)) > score:
      mostsimilar,score = d,s
  if userInput != b:
    # adds new responses to data
    if score == 0 or b not in data:
      data[b] = [userInput]
    elif userInput not in data[b]:
      data[b].append(userInput)

  # dumps edited data into file
  with open("data.json", "w") as f:
    json.dump(data,f,indent=4)

  # creates the response 
  if score != 0:
    b = data[mostsimilar][random.randint(0,len(data[mostsimilar])-1)]
  else:
    b = "i don't understand what you are saying"
  # checks if it is going to repeat itself
  if lastresponse == b:
    b = random.choice(list(data))

  lastresponse = b
  
  # prints out the response
  print(f"{b} | Certainty: {score}%")
