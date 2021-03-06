# those two lines are useful if running without PyCharm /proper "Content Root" settings...
import sys
sys.path.append('../vendor')

from PuzzleCtrl import PuzzleCtrl
from PuzzleMod import PuzzleMod
import coremon_main
from PuzzleView import PuzzleView
from coremon_main.runners import VanillaGameCtrl


# - main program
coremon_main.init()
mod = PuzzleMod()
v = PuzzleView(mod)
c = PuzzleCtrl(mod)
ctrl = VanillaGameCtrl()

# - run the game
v.turn_on()
c.turn_on()
ctrl.turn_on()
ctrl.loop()

coremon_main.cleanup()
print('done.')
