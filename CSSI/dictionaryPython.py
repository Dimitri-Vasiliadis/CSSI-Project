emoji_dic = {
    ':)' : 'happy',
    ':(' : 'sad',
    '<3' : 'heart'
}
ans = raw_input("Enter an emoji: ")
if ans in emoji_dic:
    print emoji_dic[ans]
else:
    print "its not"
