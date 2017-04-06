class Song(object):
    """so this is cool, atom creates the text structure for a class when you begin to create one, then you can tab through the elements and build your class"""

    # `__init__(self, lyrics)` means that when you instantiate an object from this class--which you do by calling `Song(<lyrics>)`--that new, instantiated object gets a variable (is this the right phrasing?) called `lyrics`, and that variable gets assigned the argument `lyrics` in the call to the class
    def __init__(self, lyrics):
        self.lyrics = lyrics

    # `sing_me_a_song(self)` means that the new, instantiated object gets a method called `sing_me_a_song`, which is a function that finds the `lyrics` variable of this instance (`self`), and prints each line
    def sing_me_a_song(self):
        for line in self.lyrics:
            print line

# when you assign an instance to a variable, here `happy_bday`, that variable is the thing that `self` refers to in the class definition
# so here, `happy_bday` gets assigned an instance of class `Song`, and that 3-element list is passed as the `lyrics` argument.
happy_bday = Song(["happy birthday to you", "I don't want to get sued", "so I'll stop right there"])

# as stated above, `self.lyrics = lyrics` means that `happy_bday.lyrics` gets assigned the argument that we passed in:
print "the lyrics argument of happy_bday: ", happy_bday.lyrics

# and `happy_bday` also gets the `sing_me_a_song` method
print "happy_bday.sing_me_a_song() is: "; happy_bday.sing_me_a_song()

# now we instantiate `bulls_on_parade`
bulls_on_parade = Song(["they rally around tha family", "with pockets full of shells"])

# it gets the `lyrics` variable
print "bulls_on_parade.lyrics: ", bulls_on_parade.lyrics

# and it gets the `sing_me_a_song` method
print "bulls_on_parade.sing_me_a_song(): "; bulls_on_parade.sing_me_a_song()
