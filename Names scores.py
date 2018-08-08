import string

letterList = list(string.ascii_lowercase)

with open("names_scores.txt", "r") as f:
    total = 0
    names = f.read()
    names = sorted(names.replace('"',"").lower().split(","))
    for i in range(len(names)):
        for letter in names[i]:
            letter_score = 0
            letter_score += letterList.index(letter)+1
            place = names.index(names[i])+1
            total += place*letter_score
print total
    
    
