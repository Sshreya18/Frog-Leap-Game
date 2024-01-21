#Step1: assign positions list and string for the reference index
positions=['G','G','G','-','B','B','B']
print(positions)
string=(0   ,    1  ,    2  ,    3 ,    4 ,    5 ,    6)

#step2: Create the final winning condition
result=['B','B','B','-','G','G','G']

print(string)

#Step3: for a infinite loop play the game and break the loop if quit
while True:
  user_input=input("Press q/Q to quit else \nEnter position of piece: ")
  if user_input=='q' or user_input=='Q':
    print('You Lose')
    break

#Step4: convert input to integer and check validilty of the positions
  else:
    move=int(user_input)
    if (0>move) or (move>6):
      print("invalid move")
      continue
    if positions[move]=='-':
      print("invalid move")
      continue
#Step5: Check for conditions if green frog and move it to right
    pos2=0
    if positions[move]=='G':
      if (move+1 <= 6) and (positions[move+1]=='-'):
        pos2=move+1
      elif (move+2 <=6) and (positions[move+2]=='-') and (positions[move+1]=='B'):
        pos2=move+2
      else:
        print("Invalid Move")
        continue

#Step5: Check for conditions if Brown frog and move it to left
    elif positions[move]=='B':
      if (move-1 <= 6) and (positions[move-1]=='-'):
        pos2=move-1
        print(pos2)
      elif (move-2 <=6) and (positions[move-2]=='-') and (positions[move-1]=='G'):
        pos2=move-2
      else:
        print("Invalid Move")
        continue
#Step6: Swap empty position if the selected position
    positions[move],positions[pos2] = positions[pos2],positions[move]

#Step7: print the current status after each iteration
    print("Current Game Status: \n")
    print(positions)

#Step8: if the result list and position list is equal, winning conditions
    if result==positions:
      print("YOU WIN")
      break
