
print("you are now hercule poirot,the detective   date is may5th.")
print("do you want to start?")
yn=input("enter yes or no  ")
if yn=="yes":
    print("we are now going inside miss hubbards house")
elif yn=="no":
    print("you have quit")
    end()
else:
    print("do you want to start?")
yn=input("enter yes or no  ")
    
print("miss hubbard has been murdered")
print("we now have only 3 suspects: miss mary(sister of victim), miss lucy(works under miss hubbard) and miss bethany(who also works under miss hubbard).motive for mary:she always wanted a share of her sisters property but hubbard always refused.lucy:she was once teased by hubbard for not working properly.bethany:no motive.")
print("you have investigated this case and found out that it was lucy who killed hubbard, but you have no evidence.")
search=input("do you want to search for clues?  ")
if search=="yes":
    print("good")
else:
    print("you have quit")
    end()
print("ÿou are now in the living room, there is blood everywhere!the tv is on.ther is a small cupboard on the other end.")
cb=input("do you want to go into the next room or search the cupboard?  ")
if cb=="next room":
    print("KITCHEN, you are locked.you chose the wrong option.YOU LOSE!")
    END()
else:
    print("there is a key and a letter the letter is a bit burnt and the letters are very faint")
letter=input("check or go to the next room? ")
if letter=="check":
     print("you cannot make out whats been written! what do you do next?(go to the next room or try continuing with the handwriting?")
     next1=input("next room or handwriting? ")
     if next1=="next room":
         print("you are now in the bedroom.there is nothing to see here.you have two staircases.one to the attic and another to the garden.")
         next2=input("attic or garden?  ")
         if next2=="ättic":
             print("you made a blunder.YOU LOSE.")
             end()
         else:
             print("in the garden you see footsteps of the same person going into the house but not out.they are not yours.you are the only person who has come to hubbards house other than the murderer.so if it is not yours,then it is the murderes that means she is still somewhere in the house hiding.")
             print("you go into the house again, you have the kitchen to your left and the storeroom to your right")
         next3=input("kitchen or storeroom?     ")
         if next3=="kitchen":
             print("KITCHEN, you are locked.you chose the wrong option.YOU LOSE!")
             END()
         else:
             print("you are now in the storeroom and you find lucy hiding between a broom and a mop.you have found evidence and you completed the mission.YOU WIN")
     else:
          print("you have got a clear print of the handwriting and voila it matches with lucys handwriting.using a decipherer you find out that the letter said""you will pay with your life for insulting me in front of my coworkers.you will die on may5th") 
          print("you got the evidence and you completed the mission.YOU WIN!")


else:
     print("you are now in the bedroom.there is nothing to see here.you have two staircases.one to the attic and another to the garden.")
     next2=input("attic or garden?  ")
     if next2=="attic":
             print("you made a blunder.YOU LOSE.")
             end()
     else:
             print("in the garden you see footsteps of the same person going into the house but not out.they are not yours.you are the only person who has come to hubbards house other than the murderer.so if it is not yours,then it is the murderes that means she is still somewhere in the house hiding.")
             print("you go into the house again, you have the kitchen to your left and the storeroom to your right")
             next3=input("kitchen or storeroom?     ")
             if next3=="kitchen":
                 print("KITCHEN, you are locked.you chose the wrong option.YOU LOSE!")
                 END()
             else:
                 print("you are now in the storeroom and you find lucy hiding between a broom and a mop.you have found evidence and you completed the mission.YOU WIN")
     
    


