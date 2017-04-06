from sys import exit
from random import randint

class Scene(object):

    def enter(self):
        print "this scene is not yet configured. subclass it and implement enter()"
        exit(1)

class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        # be sure to print out the last scene
        current_scene.enter()

class Death(Scene):

    quips = [
        "you died, you kinda suck at this",
        "wipe yourself off. you dead",
        "congratulations! You defeated the... nah, I'm just kidding, you died",
        "you're dead, horrible performance. Sad!"
    ]

    def enter(self):
        print Death.quips[randint(0, len(self.quips)-1)]
        exit(1)

class CentralCorridor(Scene):

    def enter(self):
        print "the gothons of planet percal #25 have invaded your ship and destroyed your entire crew. You are the last surviving member, and your last mission is to get eh neutron bomb from the Armory, put it in the bridge, and detonate it after you make it safely to an escape pod\nYou're running down the central corridor to the Armory when a gothon jumps out, blocking your path. He's drawing his weapon to blast you."

        action = raw_input("> ")

        if action == "shoot":
            print "you draw and fire at the gothon. he miraculously deflects your blaster's beam and now he's pissed, because you tried to kill him. He eats your face off."
            return 'death'
        elif action == "dodge":
            print "you duck and roll, dodging his blaster bolt and confounding the dim-witted thing. But you don't know how to safely roll and you bash your face into the floor. As you come to, you realize that a gothon is eating your face off."
            return 'death'
        elif action == "tell a joke":
            print "knock knock. Who's there, replies the gothon, but BAM, while he was focusing on your joke, you leap to the wall, then down onto the gothon as you punch and blast him to oblivion. You proceed through the door to the Armory."
            return 'laser_weapon_armory'
        else:
            print "DOES NOT COMPUTE"
            return 'central_corridor'

class LaserWeaponArmory(Scene):

    def enter(self):
        print "you enter the armory, crouch, and scan the room. It's silent, and you see the neutron bomb's crate in the far corner of the room. You approach it, and see a keypad lock on the box, 3 digits. If you get the code wrong 10 times, then the lock closes forever. You'll be dead."
        code = "%d%d%d" % (randint(1, 9), randint(1, 9), randint(1, 9))
        guess = raw_input("[keypad]> ")
        guesses = 0

        while guess != code and guesses < 9:
            print "BZZZZZD"
            guesses += 1
            guess = raw_input("[keypad]> ")

        if guess == code:
            print "the lock clicks open as poison gas emits from the crate and fills the room. You grab the bomb, and rush out, to the only place where you can ensure the gothons' destruction: the bridge."
        else:
            print "the lock turns red, beeps 3 times, and clicks shut forever. You die."

class TheBridge(Scene):

    def enter(self):
        # based on whether or not you has-a bomb
        # print "this is where the bomb goes" message
        # or print "you place bomb" message

class EscapePod(Scene):

    def enter(self):
        # based on whether or not the bomb has been placed
        # print "go place bomb" message, or print escape message

class Map(object):

    def __init__(self, start_scene):
        pass

    def next_scene(self, scene_name):
        pass

    def opening_scene(self):
        pass

a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
