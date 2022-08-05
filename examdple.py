import Roguelike
import random
player = Roguelike.System(random.randint(0,1000000))
player.startGame('play', [[[6,[4,69]],0],[0,0],[0,{'tile': 'floor', 'entity': 'NONE', 'loot': {'type':'gold_coin', 'amount':1}, 'text': 'NONE'}]])
# Jouw python instructies zet je vanaf hier:


while True: player.movePlayer(input())
player.movePlayer('Down')    
player.movePlayer('Left')    
player.movePlayer('Right')   


#launch program
player.gameWindow.mainloop()
# exit the program
player.exit()