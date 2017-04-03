print "you enter a dark room with 2 doors. do you go through door #1 or door #2?"

door = raw_input("> ")

if door == "1":
    print "There's a giant bear here eating a cheesecake. What do you do?"
    print "1. Take the cake"
    print "2. Scream at the bear"

    bear = raw_input("> ")

    if bear == "1":
        print "the bear eats your face off. good job!"
    elif bear == "2":
        print "the bear eats your legs off. good job!"
    else:
        print "Well, doing %s is probably better. bear runs away." % bear

elif door == "2":
    print "you stare into the endless abyss at Cthulhu's retina"
    print "1. Blueberries"
    print "2. yellow jacket clothespins"
    print "3. understanding revolvers yelling melodies"

    insanity = raw_input("> ")

    if insanity == "1" or insanity == "2":
        print "your body survives powered by a mind of jello. good job!"
    else:
        print "the insanity rots your eyes into a pool of muck. good job!"

else:
    print "you stumble around and fall on a knife and die. good job!"
