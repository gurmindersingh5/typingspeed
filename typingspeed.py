import datetime

sentence = "hello how are you"
l1 = list(sentence.split(" "))
print("word:", sentence)
before = datetime.datetime.now()
print(before)
inp = input()
after = datetime.datetime.now()
print(after)
if inp == sentence:
    print(f"{int(len(l1)/(after.second-before.second)*60)} words per minute")
else:
    print(f"please enter correct word --> {sentence}")
