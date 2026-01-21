letter = ''' Dear <|NAME|>,
Greetings from ABC coding house. I am happy to tell your selection
You are Selected!
Have a great day

Date: <|DATE|>
'''
name = input("Enter your name\n")
date = input("Enter Date\n")
letter = letter.replace("<|NAME|>", name)
letter = letter.replace("<|DATE|>", date)
print(letter)