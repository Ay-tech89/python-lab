import random
quiz = ["What is the capital of Uttar Pradesh?",
        "How many states are in North-East India?\nWrite the answer in words.",
        "Which is India\'s largest city in terms of population?",
        "What is the national song of India?",
        "Which Indian state has the highest literacy rate?"]
ans = ["LUCKNOW","EIGHT","MUMBAI","VANDE MATARAM","KERALA"]
userInp = []
sequence = []
remarks =["General knowledge will always help you. Take it seriously",
          "Needs to take interest",
          "Read more to score more",
          "Good",
          "Excellent",
          "Outstanding"]
def score():
    s = 0
    for i in range(0,5):
        if(userInp[i] == ans[sequence[i]]):
            s += 1
    return s
def remark(score):
    print(remarks[score])
def disp(r):
    print(quiz[r])
    inp = input("Answer:")
    userInp.append(inp.upper())
    sequence.append(r)                    

i = 0;
while i < 5:
    r = random.randint(0, 4)
    if(r not in sequence):
        i += 1                                    
        disp(r)
s = score()
print("Your score :", s, "out of 5")
remark(s)
