def calc_drone_min_energy(route):
  # your code goes here

  start_energy = 0
  for i in range(len(route) - 1, 0, -1):
    height_diff = route[i][2] - route[i - 1][2] 
    if height_diff < 0:
      if start_energy > 0:
        start_energy += height_diff
      # reset start energy to 0
      if start_energy < 0:
        start_energy = 0
    elif height_diff > 0:
      start_energy += height_diff
  return start_energy
# height diff =   -7 9 6  -10 
# startenergy   0 0  9 15  5
"""
route = [ [0,   2, 10],
                  [3,   5,  0],
                  [9,  20,  6],
                  [10, 12, 15],
                  [10, 10,  8] ]
            x,y,z 0,2,10
            row, col, height, 0,2,10
                              3,5,0
                                  0-10 = -10
                  10,0,6,15,8       
                                  
                 start energy = 5
                 current energy = 15,9,0,8
10,10,8                     start energy = 0
10,12,15    gain 7    means start energy = 0
9,20,6      lose 9    means start energy = 0 + 9
3,5, 0      lose 6    means start energy = 9 + 6
0,2,10      gain 10   means start energy = 15 - 10 = 5
                 
"""
      
