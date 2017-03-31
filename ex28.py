print "#1 Guess: %s, Is: %s" % (True, True and True)

print "#2 Guess: %s, Is: %s" % (False, False and True)

print "#3 Guess: %s, Is: %s" % (False, 1 == 1 and 2 == 1)

print "#4 Guess: %s, Is: %s" % (True, "test" == "test")

print "#5 Guess: %s, Is: %s" % (True, 1 == 1 or 2 != 1)

print "#6 Guess: %s, Is: %s" % (True, True and 1 == 1)

print "#7 Guess: %s, Is: %s" % (False, False and 0 != 0)

print "#8 Guess: %s, Is: %s" % (True, True or 1 == 1)

print "#9 Guess: %s, Is: %s" % (False, "test" == "testing")

print "#10 Guess: %s, Is: %s" % (False, 1 != 0 and 2 == 1)

print "#11 Guess: %s, Is: %s" % (True, "test" != "testing")

print "#12 Guess: %s, Is: %s" % (False, "test" == 1)

print "#13 Guess: %s, Is: %s" % (True, not (True and False))

print "#14 Guess: %s, Is: %s" % (False, not (1 == 1 and 0 != 1))

print "#15 Guess: %s, Is: %s" % (False, not (10 == 1 or 1000 == 1000))

print "#16 Guess: %s, Is: %s" % (False, not (1 != 10 or 3 == 4))

print "#17 Guess: %s, Is: %s" % (True, not ("testing" == "testing" and "Zac" == "Badass"))

print "#18 Guess: %s, Is: %s" % (True, 1 == 1 and (not ("testing" == 1 or 1 == 0)))

print "#19 Guess: %s, Is: %s" % (False, "chunky" == "bacon" and (not( 3 == 4 or 3 == 3)))

print "#20 Guess: %s, Is: %s" % (False, 3 == 3 and (not ("testing" == "testing" or "Python" == "Fun")))
