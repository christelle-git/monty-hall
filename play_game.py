from enum import Enum
import numpy as np
np.random.seed()

class Strategy(Enum):
    CHANGE = 1 # change the original choice
    KEEP = 0   # keep the original choice 

      
def play(strategy, laps):
    '''
    
        Simulates a sequence of Monty Hall's game.
        
        Args:
           * strategy: CHANGE or KEEP the original choice   
           * laps: number of party
           
        Return:
           * player's gain table (numpy array) of size laps:
             containing 1 if the player wins and 0 otherwise.

    '''  
    
    doors = np.full((laps, 3),[0, 1, 2]) 
    right_doors = np.random.randint(3, size=laps)
    first_choice = np.random.randint(3, size=laps)
    del_i = np.arange(laps)*3 + first_choice
    doors = np.delete(doors, del_i).reshape(laps,-1)
    mat_bool = (first_choice == right_doors).astype(int)

    # CASE first_choice != right_doors
    ind = np.where(mat_bool == 0) 
    ind_null = np.asarray(ind)
    doors_final = np.zeros(laps, dtype=int)
    np.put(doors_final, ind_null, right_doors[ind_null])

    # CASE: first_choice == right_doors
    ind = np.where(mat_bool > 0)
    ind_win = np.asarray(ind)
    val = np.random.randint(2, size=sum(mat_bool))
    ind_win = ind_win.ravel() 
    np.put(doors_final, ind_win, doors[ind_win, val])    
          
    second_choice = np.zeros(laps)
    if strategy == Strategy.KEEP:
        second_choice = first_choice
    elif strategy == Strategy.CHANGE:
        second_choice = doors_final  

    return (second_choice == right_doors).astype(int)  
