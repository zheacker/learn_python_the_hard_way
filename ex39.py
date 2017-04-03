## Dictionaries!
## create a mapping of state to abbreviation

states = {
    'oregon' : 'or',
    'florida' : 'fl',
    'california' : 'ca',
    'new york' : 'ny',
    'michigan' : 'mi'
}

## create a basic set of states and some cities in them
cities = {
    'ca' : 'san francisco',
    "mi" : 'detroit',
    'fl' : "jacksonville"
}

## add some more cities
cities["ny"] = "new york"
cities['or'] = 'portland'

## print out some cities
print '-'*10
print "NY state has: ", cities['ny']
print "OR state has: ", cities['or']

## print some states
print '-' * 10
print "Michigan's abbreviation is: ", states['michigan']
print "florida's abbreviation is : ", states['florida']

## do it by using the states then cities dict
print '-' * 10
print "michigan has: ", cities[states['michigan']]
print "florida has: ", cities[states['florida']]

## print every state abbreviation
print '-' * 10
for state, abbrev in states.items():
    print "%s is abbreviated as %s" % (state, abbrev)

## print every city in state
print '-' * 10
for abbrev, city in cities.items():
    print "%s has the city %s" % (abbrev, city)

## now do both at the same time
print "-" * 10
for state, abbrev in states.items():
    print "%s state is abbreviated %s and has city %s" % (state, abbrev, cities[abbrev])

print '-' * 10
# safely get an abbreviation by state that might not be there
state = states.get('texas')

if not state:
    print "sorry, no texas (HURRAY!)"

## get a city with a default value
city = cities.get('tx', 'does not exist')
print "The city for the state of 'tx' is: %s" % city
