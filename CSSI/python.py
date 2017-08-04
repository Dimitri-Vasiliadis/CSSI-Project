from random import randint

# def ps(number, word):
#     print number * word
# ps(2, "banana")

# tasks = ['my homework', 'my resume', 'my code']
# excuses = ['I am sick', 'I was at home', 'I feel asleep', 'my dog ate it']

# print "I did not complete %s because %s" % (tasks[randint(0,len(tasks) - 1)], excuses[randint(0,len(excuses) - 1)])

# noun = raw_input("Enter a noun: ")
# verb = raw_input("Enter a verb: ")
# adverb = raw_input("Enter a adverb: ")

# print "noun: %s verb: %s adverb: %s" % (noun, verb, adverb)

# def randompassword(num):
#     letters = ['a', 'b', 'c', 'd', 'e', 'i', 'o', 'u']
#     password = ""
#     for x in range(num):
#         password += letters[randint(0,len(letters) - 1)]
#     print "Password: %s" % (password)
# randompassword(8)

# def food():
#     items = []
#     number_item = []
#     num = int(raw_input("How many items: "))
#     for x in range(num):
#         item = raw_input("Enter an item: ")
#         items.append(item)
#         num_of = int(raw_input("How much? "))
#         number_item.append(num_of)
#         if item == "milk":
#             print "milk are dumb"
#     print items
#
#     for x in range(len(items)):
#         for i in range(len(number_item)):
#             print "%s. %s " % (x+1, items[i]*number_item[i])
# food()

# def game():
#     num = randint(1,10)
#     guess = int(raw_input("Enter a number: "))
#     print num
#     print guess
#     while guess != num:
#         if guess > num:
#             print "too high!"
#             guess = int(raw_input("Enter a number: "))
#         else:
#             print "too low!"
#             guess = int(raw_input("Enter a number: "))
#     print "you win!"
# game()

# english_dictionary = {
#     "rabbit": "bugs bunny"
# }

# numbers = {
#     1: "one",
#     2: "two"
# }
# print numbers[2]
#
# emoji_to_english = {
#     ":)": "smile",
#     ":(": "sad"
# }
# print emoji_to_english[":("]
