import os
import libtcodpy as libtcod
from player import Player
from menu import InputMenu, OptionsMenu


class Game(object):    
    def __init__(self):
        self.SCREEN_WIDTH = 80
        self.SCREEN_HEIGHT = 50
        libtcod.console_set_custom_font("consolas12x12_gs_tc.png", libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_TCOD)
        libtcod.console_init_root(self.SCREEN_WIDTH, self.SCREEN_HEIGHT, "Zombies from the Graveyard", False)
        

    def handle_input(self):
        key = libtcod.console_wait_for_keypress(True)

        if key == libtcod.KEY_UP:
            playery -= 1
        elif key == libtcod.KEY_DOWN:
            playery += 1
        elif key == libtcod.KEY_LEFT:
            playerx -= 1
        elif key == libtcod.KEY_RIGHT:
            playerx += 1
        elif key == libtcod.KEY_ESCAPE:
            return "Exit"
            
    def on_loop(self):
        pass
    
    def on_render(self):
        libtcod.console_flush()
        
    def on_cleanup(self):
        pass

    def on_execute(self):
        while not libtcod.console_is_window_closed():
            self.on_render()
            
            if self.handle_input() == "Exit":
                break
                
            self.on_loop()
            
        self.on_cleanup()


game = Game();
game.on_execute();

#hero = Player()

##hero.give_name()
#hero.give_job()
#hero.job_description()

#print "You turn on the TV and you watch the news. There were 12 more deaths since yesterday. And they say the vaccine had some side effects."
#raw_input()
#print "Nobody should leave their homes so they don't get infected. Almost everyone that was infected died within 5 hours."
#raw_input()
#print "They are doing everything in their power to stop this from spreading."
#raw_input()
#print "You are tired from work anyway, and you could use these extra hours to get some sleep."
#raw_input()
#print "You go to bed..."
#raw_input()
#raw_input()
#raw_input()
#print "You wake up with siren noises coming from the street. You can also hear people screaming"
#menu = OptionsMenu("What do you want to do?", ["Kill yourself", "Go back to sleep", "Watch the street from the window", "Go outside"])
#menu.show()
