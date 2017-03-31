people = 30
cars = 40
trucks = 15

if cars > people:
    print "we should take the cars"
elif cars < people:
    print "we shouldn't take the cars"
else:
    print "dunno which to take"

if trucks > cars:
    print "too many trucks"
elif trucks < cars:
    print "maybe take the trucks"
else:
    print "still dunno which to take"

if people > trucks:
    print "fuck it, let's just take the trucks"
else:
    print "fuck it, let's just stay home"
