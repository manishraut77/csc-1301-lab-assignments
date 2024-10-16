import sys
fname=sys.argv[1]
with open(fname) as f:
  hands= f.read().splitlines()

def validate_hands(hand): #this is the function to validate if the input is correct or not
    suits={'c','d','h','s'}
    ranks = {'2', '3', '4', '5', '6', '7', '8', '9', "t", "j", "q","k","a"}
    hand_list=hand.split(":") #hand is basically a string here. so by using
    #.spilit() i get a list like hand_list=[8c,9h,as,kc,5s]

    if len(hand_list)!=5:
        return False

    for x in hand_list:
      # for eg by using this loop, x takes values like x=8c at a time when the loop executes.  
        if len(x)!=2: 
            return False
        
        if x[0] not in ranks or x[1] not in suits:

            return False
    return True

def suit_process(hand): #the hand that i pass in these type of function is a string like 8s:5h:as:kd:7c
    suit_dict={
        "c":0,
        "d":0,
        "h":0,
        "s":0 
        }
    suit_dict["c"]=hand.count("c")
    suit_dict["d"]=hand.count("d")
    suit_dict["h"]=hand.count("h")
    suit_dict["s"]=hand.count("s")


    return(suit_dict)

def rank_process(hand):
    #this is the dictonary for how many cards in a particular rank. 
    rank_dict = {
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0,
        7: 0,
        8: 0,
        9: 0,
        10: 0,
        11: 0,
        12: 0,
        13: 0,
        14: 0,
    }

    rank_dict[2] = hand.count("2")
    rank_dict[3] = hand.count("3")
    rank_dict[4] = hand.count("4")
    rank_dict[5] = hand.count("5")
    rank_dict[6] = hand.count("6")
    rank_dict[7] = hand.count("7")
    rank_dict[8] = hand.count("8")
    rank_dict[9] = hand.count("9")
    rank_dict[10] = hand.count("t")
    rank_dict[11] = hand.count("j")
    rank_dict[12] = hand.count("q")
    rank_dict[13] = hand.count("k")
    rank_dict[14] = hand.count("a")

    keys_to_remove=[]

    for key in rank_dict:
        if rank_dict[key]==0:
            keys_to_remove.append(key)
    for key in keys_to_remove:
        rank_dict.pop(key)
    return rank_dict

#returns a dictonary for particular hand

def straight_check(temp):
   
    for key in temp:
       if temp[key]>1:
           return False

    sorted_keys=sorted(temp.keys())
    for i in range(1,len(sorted_keys)):

        if sorted_keys[i]-sorted_keys[i-1]!=1:
            return False
    return True
            
def flush_check(temp):
    
    if 5 in temp.values():
        return True
    else:
        return False
    
def fourofakind_check(temp):
    if 4 in temp.values():
        return True
    else:
        return False

def fullhouse_check(temp):
    if 3 in temp.values() and 2 in temp.values():
        return True
    else:
        return False
    
def threeofakind_check(temp):
    if 3 in temp.values() and 2 not in temp.values():
        return True
    else:
        return False
    
def twopair_check(temp):
    count=0
    for i in temp.values():
        if i==2:
            count+=1
    if count==2:
        return True
    else:
        return False

def pair_check(temp):
    count=0
    for i in temp.values():
        if i==2:
         count+=1

    if count==1:
        return True
    else:
        return False
    

for hand in hands:

    # Call validate function here
    if validate_hands(hand) == True:
# i am clling all other functions here if the card falls in any of the categories or not
        rank_dict = rank_process(hand)
        suit_dict = suit_process(hand)
        straight = straight_check(rank_dict)
        flush = flush_check(suit_dict)
        fourofakind = fourofakind_check(rank_dict)
        fullhouse = fullhouse_check(rank_dict)
        threeofakind = threeofakind_check(rank_dict)
        twopairs = twopair_check(rank_dict)
        pair = pair_check(rank_dict)

        if straight == True and flush == True:
            print(hand, "Straight Flush")
        elif fourofakind == True:
            print(hand, "Four of a kind")
        elif fullhouse == True:
            print(hand, "Full house")
        elif flush == True:
            print(hand, "Flush")
        elif straight == True:
            print(hand, "Straight")
        elif fourofakind == True:
            print(hand, "Four of a kind")
        elif threeofakind == True:
            print(hand, "Three of a kind")
        elif twopairs == True:
            print(hand, "Two Pairs")
        elif pair == True:
            print(hand, "Pair")
        else:
            print(hand, "High Hand")
    else:
        print(hand, "Invalid Hand")
