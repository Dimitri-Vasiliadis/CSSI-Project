snax = {
    "fruit snacks" : 10,
    "apples" : 7,
    "raisins" : 5,
    "cookies" : 8
}



for item in snax:
    if item == "raisins":
        snax[item] = 2
    print "%s get a %s out of 10" % (item, snax[item])
