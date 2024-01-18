# Ece Nur Taş 2210356039
from sys import argv
# python Assignment4.py Player1.txt Player2.txt Player1.in Player2.in

file_names=[]
ship1=[]
ship2=[]
optional1=[]
optional_dict1=[]
optional2=[]
optional_dict2=[]


alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
board1=[["-","-","-","-","-","-","-","-","-","-"], ["-","-","-","-","-","-","-","-","-","-"], ["-","-","-","-","-","-","-","-","-","-"], ["-","-","-","-","-","-","-","-","-","-"], ["-","-","-","-","-","-","-","-","-","-"], ["-","-","-","-","-","-","-","-","-","-"], ["-","-","-","-","-","-","-","-","-","-"], ["-","-","-","-","-","-","-","-","-","-"], ["-","-","-","-","-","-","-","-","-","-"], ["-","-","-","-","-","-","-","-","-","-"]]
board2=[["-","-","-","-","-","-","-","-","-","-"], ["-","-","-","-","-","-","-","-","-","-"], ["-","-","-","-","-","-","-","-","-","-"], ["-","-","-","-","-","-","-","-","-","-"], ["-","-","-","-","-","-","-","-","-","-"], ["-","-","-","-","-","-","-","-","-","-"], ["-","-","-","-","-","-","-","-","-","-"], ["-","-","-","-","-","-","-","-","-","-"], ["-","-","-","-","-","-","-","-","-","-"], ["-","-","-","-","-","-","-","-","-","-"]]
input3=[]
outputs=[]

def letter_to_number(letter):       # return which index is the letter (P,S,C,B,D)
  return alphabet.index(letter)

with open("OptionalPlayer1.txt","r") as op_file1:
    for op in op_file1:
        op=op.split(";")
        optional1.append(op)

for opp in optional1:
    integer=opp[0][-3:-2]
    integer=(int(integer)-1)
    let=int(letter_to_number(opp[0][-1:]))
    
    opp[0]=opp[0][:-2]+str(let)

    op_dict1={opp[0][0:-3]:str(integer)+opp[0][-1:]}
    optional_dict1.append(op_dict1)
    for xxx in op_dict1:
        if op_dict1[xxx][0]=="-":
            op_dict1[xxx]="9"+op_dict1[xxx][2:]    
        if opp[1]=="right":
            pass
for opp2 in optional2:
    integer2=opp2[0][-3:-2]
    integer2=(int(integer2)-1)
    let2=int(letter_to_number(opp2[0][-1:]))
    
    opp2[0]=opp2[0][:-2]+str(let)

    op_dict2={opp2[0][0:-3]:str(integer2)+opp2[0][-1:]}
    optional_dict2.append(op_dict2)
    for xxxx in op_dict2:
        if op_dict2[xxxx][0]=="-":
            op_dict2[xxxx]="9"+op_dict2[xxxx][2:]    
        if opp[1]=="right":
            pass

def output():       # write function to a file as appending lines a list (outputs)
    outfile = open("Battleship.out", "w")
    for out in outputs:
        outfile.write(out + "\n")

print("Battle of Ships Game")
outputs.append("Battle of Ships Game")



def board(val):     # function for printing 10x10 board
    val = ["-"*10]*10
    print("  A B C D E F G H I J")
    for i in range(len(val)-1):
        print(f"{i+1} {' '.join(val[i])}")
    for i in range(len(val)-1,len(val)):
        print(f"{i+1}{' '.join(val[i])}")

def add(filenames):             # shortcut for appending the names of the files which was opened
    file_names.append(filenames)

def open_func():
    try:
        player1=argv[1]
        player2= argv[2]
        user_input1=argv[3]
        user_input2=argv[4]
        # player1="Player1.txt"
        # player2= "Player2.txt"
        # user_input1="Player1.in"
        # user_input2= "Player2.in"
        empty = [player1,player2,user_input1,user_input2]       # for checking IOError
        file1=open(player1,"r")
        add(player1)                                # append
        file2=open(player2,"r")
        add(player2)                                #append
        file3=open(user_input1,"r")
        add(user_input1)                                #append
        file4=open(user_input2,"r")
        add(user_input2)                            #append

        for l in file3:             # file3 = file of player1's moves
            input1 = l.split(";")
            input1.pop()        # 1. user's moves
    
        for li in file4:             # file4 = file of player2's moves
            input2 = li.split(";")
            input2.pop()        # 2. users's moves
        
        for ii, iii in zip(input1, input2):     # zip is for getting same order of each player's moves 
            input3.append(ii)                   # ii = input1[0]     iii = input2[0]       # ii = input[1]      iii = input2[1]
            input3.append(iii)                  # input3 = [input1[0], input2[0], input[1], input2[1], ...]

        for p in file1:             # file1 = file of ships of player1
            if p[len(p)-1:] == "\n":       # for the last indices of each line, discard new line(\n)
                p=p[:-1]
            p=p.split(";")           
            ship1.append(p)     # 1. user's ships, list in list        

        for pp in file2:             # file2 = file of ships of player2
            if pp[len(pp)-1:] == "\n":       # for the last indices of each line, discard new line(\n)
                pp=pp[:-1]
            pp=pp.split(";")
            ship2.append(pp)        # 2. user's ships, list in list
    except IOError:
        list=[x for x in empty if x not in file_names ]     # empty includes all file names regardless of their existence or being reachable
        list2=", ".join(list)                               # file_names includes file names that are reachable when we try to open the files
        print(f"IOError: input file(s) {list2} is/are not reachable.")
        outputs.append(f"IOError: input file(s) {list2} is/are not reachable.")
    except IndexError:
        print("Inputs are less than expected.")             # inputs are files that were entered to the terminal at the beginning of the code
        outputs.append("Inputs are less than expected.")
    
def all():        # which is body part of the code
    
    d,c,s,p,b=0,0,0,0,0         # all letters correspond to numbers of that ships that will be counted and printing X for every sunked ships
                                # first board's ships
    dd,cc,ss,pp,bb=0,0,0,0,0    # second board's ships

    all_1ships={"Carrier\t\t":"-\t\t","Battleship\t":"- -\t\t","Destroyer\t":"-\t\t","Submarine\t":"-\t\t","Patrol Boat\t":"- - - -\t"}
# for printing situation of current ships just after the printed boards  
    all_2ships={"Carrier\t\t":"-\t\t","Battleship\t":"- -\t\t","Destroyer\t":"-\t\t","Submarine\t":"-\t\t","Patrol Boat\t":"- - - -\t"}
    
    for move3 in range(len(input3)):        # input3 = [input1[0], input2[0], input[1], input2[1], ...]
                                            # figuring out e.g which indices does the 4,E correspond
        comma=input3[move3].find(",")       # comma=1
        row=int(input3[move3][:comma])-1    # 4,E  =>  3,E       row=3
        colum=input3[move3][comma+1:]       # 4,E  =>  4,4       colum=E       column=4
        column=(letter_to_number(colum))    # which indices does the letter correspond
        
        if move3 % 2 == 0:        # input3 = [input1[0], input2[0], input[1], input2[1], ...]
            print("\nPlayer1’s Move\n")         # so, input1[0] is at even index, that means every 1. player's move has even index
            print(f"Round : {int(move3/2+1)}\t\t\t\t\tGrid Size: 10x10\n")					
            print("Player 1's Hidden Board\t\tPlayer 2's Hidden Board")
            outputs.append("\nPlayer1’s Move\n")
            outputs.append(f"Round : {int(move3/2+1)}\t\t\t\t\tGrid Size: 10x10\n")          
            outputs.append("Player 1's Hidden Board\t\tPlayer 2's Hidden Board")        
            print("  A B C D E F G H I J\t\t  A B C D E F G H I J")          
            outputs.append("  A B C D E F G H I J\t\t  A B C D E F G H I J")

            for i in range(9):
                print(f"{i+1} {' '.join(board1[i])}\t\t{i+1} {' '.join(board2[i])}")    # printing numbers of rows at the beginning of the each row
                outputs.append(f"{i+1} {' '.join(board1[i])}\t\t{i+1} {' '.join(board1[i])}")  # 1 - O - - - -   \t\t     1 - - X - -         
                                                                                                # this will go like this row by row
            for i in range(9,10):                                                              # 2 - - - - - X   \t\t     2 - - - - -
                print(f"{i+1}{' '.join(board1[i])}\t\t{i+1}{' '.join(board2[i])}\n")                 # just the last row because we need to add \n at the end of this row
                outputs.append(f"{i+1}{' '.join(board1[i])}\t\t{i+1}{' '.join(board2[i])}\n")      


            
            # assert row <= 9, "AssertionError: Invalid Operation.\n"
            # assert column <= 9, "AssertionError: Invalid Operation.\n"
            
            for key in all_1ships:          # all_1ships and all_2ships are same so, it doesn't matter which one I wrote down there
                print(key,all_1ships[key],"\t\t", key, all_2ships[key])    # Carrier X     \t\t...     Carrier -
                outputs.append(key+all_1ships[key]+"\t\t"+key+all_2ships[key])     #line by line in the dictionaries
            try:
                assert row <= 9, "AssertionError: Invalid Operation.\n"
                assert column <= 9, "AssertionError: Invalid Operation.\n"                                                        # we have specific ships P B C S D
                if ship2[row][column] in ["P","B","C","S","D"]:    # one part of ship shot by Player 1,
                    board2[row][column]="X"              # Replace the character at board2[row][column] 
                    if ship2[row][column]=="C":
                        cc += 1                                 
                        if cc==5:                           # when all parts of c ship sunk, write X instead of - at the dictionary
                            all_2ships["Carrier\t\t"]="X"           # and same for all ...
                        
                    elif ship2[row][column]=="S":            
                        ss += 1
                        if ss==3:
                            all_2ships["Submarine\t"]="X"
                        
                    elif ship2[row][column]=="D":            
                        dd += 1
                        if dd==3:
                            all_2ships["Destroyer\t"]="X"
                    elif ship2[row][column]=="P":           
                        pp += 1
                        if pp==8:
                            all_2ships["Patrol Boat\t"]="X X X X"
                        elif pp==6:
                            all_2ships["Patrol Boat\t"]="X X X -"
                        elif pp==4:
                            all_2ships["Patrol Boat\t"]="X X - -"
                        elif pp==2:
                            all_2ships["Patrol Boat\t"]="X - - -"
                        
                    elif ship2[row][column]=="B":  
                        bb += 1
                        if bb==8:
                            all_2ships["Battleship\t"]="X X"
                        elif bb==4:
                            all_2ships["Battleship\t"]="X -"

                elif ship2[row][column] not in ["P","B","C","S","D"]:       # if opponent couldn't shoot any part of any ships,
                    board2[row][column]="O"                                 # replace that part of board2 with O
                print(f"\nEnter your move: {row+1},{colum}")
                outputs.append(f"\nEnter your move: {row+1},{colum}")
            except AssertionError as ae:         
                print(f"\nEnter your move: {row+1},{colum}")
                outputs.append(f"\nEnter your move: {row+1},{colum}")
                print(ae)
                outputs.append("AssertionError: Invalid Operation.")
            

        elif move3 % 2 != 0:        # input3 = [input1[0], input2[0], input[1], input2[1], ...]
            print("\nPlayer2’s Move\n")     # so, input1[0] is at even index, that means every 1. player's move has even index

            print(f"Round : {int((move3+1)/2)}\t\t\t\t\tGrid Size: 10x10\n")					        
            print("Player 1's Hidden Board\t\tPlayer 2's Hidden Board")          
            
            print("  A B C D E F G H I J\t\t  A B C D E F G H I J")
        
            outputs.append("\nPlayer2’s Move\n")
            outputs.append(f"Round : {int((move3+1)/2)}\t\t\t\t\tGrid Size: 10x10\n")
            
            outputs.append("Player 1's Hidden Board\t\tPlayer 2's Hidden Board")
            outputs.append("  A B C D E F G H I J\t\t  A B C D E F G H I J")

            for i in range(9):
                print(f"{i+1} {' '.join(board1[i])}\t\t{i+1} {' '.join(board2[i])}")    # printing numbers of rows at the beginning of the each row
                outputs.append(f"{i+1} {' '.join(board1[i])}\t\t{i+1} {' '.join(board2[i])}")  # 1 - O - - - -   \t\t     1 - - X - -  
                                                                                                # this will go like this row by row             
            for i in range(9,10):                                                              # 2 - - - - - X   \t\t     2 - - - - -
                print(f"{i+1}{' '.join(board1[i])}\t\t{i+1}{' '.join(board2[i])}\n")            # just the last row because we need to add \n at the end of this row              
                outputs.append(f"{i+1}{' '.join(board1[i])}\t\t{i+1}{' '.join(board2[i])}\n")
          
            for key in all_1ships:
                print(key, all_1ships[key],"\t\t", key, all_2ships[key])    # Carrier X     \t\t...     Carrier -
                outputs.append(key+all_1ships[key]+"\t\t"+key+all_2ships[key])       #line by line in the dictionaries
            try:          
                assert row <= 9, "AssertionError: Invalid Operation.\n"
                assert column <= 9, "AssertionError: Invalid Operation.\n"                                              # we have specific ships P B C S D
                if ship1[row][column] in ["P","B","C","S","D"]:    # one part of ship shot by Player 2,
                    board1[row][column]="X"              # Replace the character at board1[row][column] 
                    
                    if ship1[row][column]=="C":
                        c += 1                           # when all parts of c ship sunk, write X instead of - at the dictionary
                        if c==5:                                    # and same for all ...
                            all_1ships["Carrier\t\t"]="X\t\t"

                    elif ship1[row][column]=="S": 
                        s += 1
                        if s==3:
                            all_1ships["Submarine\t"]="X\t\t"
                    
                    elif ship1[row][column]=="D":
                        d += 1
                        if d==3:
                            all_1ships["Destroyer\t"]="X\t\t"
                    elif ship1[row][column]=="P":           
                        p += 1
                        if p==8:
                            all_1ships["Patrol Boat\t"]="X X X X\t"
                        elif p==6:
                            all_1ships["Patrol Boat\t"]="X X X -\t"
                        elif p==4:
                            all_1ships["Patrol Boat\t"]="X X - -\t"
                        elif p==2:
                            all_1ships["Patrol Boat\t"]="X - - -\t"

                    elif ship1[row][column]=="B":      
                        b += 1
                        if b==8:
                            all_1ships["Battleship\t"]="X X\t\t"  
                        elif b==4:
                            all_1ships["Battleship\t"]="X -\t\t"

                elif ship1[row][column] not in ["P","B","C","S","D"]:       # if opponent couldn't shoot any part of any ships,
                    board1[row][column]="O"                                 # replace that part of board2 with O
                print(f"\nEnter your move: {row+1},{colum}")       
                outputs.append(f"\nEnter your move: {row+1},{colum}")
            except AssertionError as ae:
                print(f"\nEnter your move: {row+1},{colum}")
                outputs.append(f"\nEnter your move: {row+1},{colum}")
                print(ae)
                outputs.append("AssertionError: Invalid Operation.")
                

    if (c,b,p,d,s)==(5,8,8,3,3) and (cc,bb,pp,dd,ss)==(5,8,8,3,3):      # We were counting them if they had sunk
        print("\nIt is a Draw!\n")                              # e.g c is 5 when all c ships sunk
        outputs.append("\nIt is a Draw!\n")                     # both players finished at the same round
    elif (c,b,p,d,s)==(5,8,8,3,3):
        print("\nPlayer2 Wins!\n")                              # player 2 finished before player 1
        outputs.append("\nPlayer2 Wins!\n")
    elif (cc,bb,pp,dd,ss)==(5,8,8,3,3):
        print("\nPlayer1 Wins!\n")                              # player 1 finished before player 2
        outputs.append("\nPlayer1 Wins!\n")
    print("Final Information\n")                                # printing board for the final situation right after game's finishing
    print("Player 1's Board\t\tPlayer 2's Board")

    print("  A B C D E F G H I J\t\t  A B C D E F G H I J")
    
    outputs.append("Final Information\n")
    outputs.append("Player 1's Board\t\tPlayer 2's Board")

    outputs.append("  A B C D E F G H I J\t\t  A B C D E F G H I J")



    for i in range(9):
        for j in range(9):    
            if board1[i][j]=="-" and ship1[i][j] in ["P","S","C","B","D"]: 
                board1[i][j]=ship1[i][j]             # if any part of any ship didn't shoot by opponent, show that unshot part of ship
            if board2[i][j]=="-" and ship2[i][j] in ["P","S","C","B","D"]:
                board2[i][j]=ship2[i][j]             # if any part of any ship didn't shoot by opponent, show that unshot part of ship
        print(f"{i+1} {' '.join(board1[i])}\t\t{i+1} {' '.join(board2[i])}")     # e.g 1 - O - - - -   \t\t     1 - - X - -
        outputs.append(f"{i+1} {' '.join(board1[i])}\t\t{i+1} {' '.join(board2[i])}")     # this will go like this row by row until i reaches 9
    for i in range(9,10):
        for j in range(9,10):
            if board1[i][j]=="-" and ship1[i][j] in ["P","S","C","B","D"]:
                board1[i][j]=ship1[i][j]            # if any part of any ship didn't shoot by opponent, show that unshot part of ship
            if board2[i][j]=="-" and ship2[i][j] in ["P","S","C","B","D"]:
                board2[i][j]=ship2[i][j]            # if any part of any ship didn't shoot by opponent, show that unshot part of ship
        print(f"{i+1}{' '.join(board1[i])}\t\t{i+1}{' '.join(board2[i])}\n")     # e.g 10 - O - X - X   \t\t     1 O - X O X 
        outputs.append(f"{i+1}{' '.join(board1[i])}\t\t{i+1}{' '.join(board2[i])}\n")   # just for the last row because we should add \n at the end of the just last row
        for key in all_1ships:          # all_1ships and all_2ships are same so, it doesn't matter which one I wrote down there
            print(key, all_1ships[key],"\t"*2, key, all_2ships[key])    # Carrier X     \t\t...     Carrier -
                                                                            #line by line in the dictionaries
            outputs.append(key+all_1ships[key]+"\t"*2+key+all_2ships[key])
    # except AssertionError as ae:
    #                 print(ae)


open_func()     # calling functions
all()
output()

