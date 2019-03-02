"""

 
             Monty Hall's Game (using Numpy)
             
             Rules: 
             0) The game opposes a presenter and a player.
                The game consists of three doors, behind one of the doors
                there is a treasure.
             1) The player chooses a door among the three.
             2) The presenter then eliminates a door that does not hide
                the treasure among the two remaining.
             3) The player makes one last choice: either he keeps
                his original door, or he changes his door.
                
             Problem:
                In step 3), what is the best strategy between keeping
                its original door or changing the door?
                
             Procedure:
                To determine the best strategy, a sequence of Monty Hall's 
                game parts is simulated. Then one counts how many times 
                the player wins depending on either he keeps or changes 
                the door in step 3).
                The result are depicted on figures below (.ipynb).
                
             Result:
                 The best strategy is to change...


"""
import matplotlib.pyplot as plt
from play_game import *
import play_game


# play nb_parts games by calling the play function of play_game module
nb_parts = 100
res_CHANGE = play_game.play(Strategy.CHANGE, nb_parts)
res_KEEP = play_game.play(Strategy.KEEP, nb_parts)

plt.bar([1,2], (sum(res_CHANGE), sum(res_KEEP)), tick_label=["Change","Keep"])
plt.show()

gains_change = []
gains_keep = []
samples =  [1000, 10000, 20000, 50000, 80000, 100000]
for tours in samples:
    gains_change.append(play_game.play(Strategy.CHANGE, tours))
    gains_keep.append(play_game.play(Strategy.KEEP, tours))
    
figure = plt.figure()
plot = plt.scatter(samples, [sum(x) for x in gains_change])
plot = plt.scatter(samples, [sum(x) for x in gains_keep])  
plt.show()

