import json
from difflib import get_close_matches

data = json.load(open("data.json"))
def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w,data.keys())) > 0:
        ans  = input("Did you mean %s instead? Enter Y if yes,or N if no"
                     % get_close_matches(w,data.keys())[0])
        if ans == "Y":
           return data[get_close_matches(w,data.keys())[0]]
       elif ans == "N":
           return "The word doesn't exist."
       else:
           return "We didn't understand your query"       
    else:
        return "The word doesn't exist. Pleasae double check"

word = input("Enter word: ")

print(translate(word))
