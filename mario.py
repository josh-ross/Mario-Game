# This is our game for the project

import os
import time
import sys
import random

def cont():
	cont=raw_input()

def clear():
	os.system('clear')

def start():
	global player
	clear()	
	print "Mario Apocalpyse! Press RETURN to start your adventure as Mario and CTRL-C to quit"
	time.sleep(1)
	cont()
	clear()
	print "Please select either Mario or Luigi (m/l)"
	player=str(raw_input())
	time.sleep(1)
	clear()

def begin():
	clear
	time.sleep(1)
	print "-------------"
	print "|Nintendo 64|"
	print "-------------"
	time.sleep(1)
	print "\nIt's a me Mario!"
	time.sleep(2)
	os.system('clear')
	print "Press Enter To Begin Your Journey Into The Wonderful World Of Mario"
	time.sleep(1)
	cont()
	start()  

def respond():
	respond=raw_input()

def diceGame(name):
  		  		p=0
    				c=0
    				pTotal=0
   				cTotal=0
    				rount=1
    				print 'You are now playing',name,'in a dice game!!!!\nThis will be a best 4 out of 7'
    				time.sleep(1)
    				print 'Whoever rolls the highest number wins!'
    				time.sleep(5)
    				clear()
   				while(pTotal<4 and cTotal<4):
            				print 'Round #'+str(rount)
            				rount+=1
            				yorn=raw_input('Would you like to roll?<y/n>\n>')
            				if(yorn=='y'):
                    				p = random.randint(1,6)
                   				print 'You rolled a',p
            				else:
                   				p=0
        				time.sleep(1)
        				if(cTotal>=2):
           					c=random.randint(1,3)
       					else:
            					c=random.randint(1,6)
            				print name+' rolled a',c
       					time.sleep(1)
            				if(p>c):
                   				print 'You win this round!'
                    				pTotal+=1
            				elif (c>p):
                    				print 'Awww... You lose this round!'
                    				cTotal+=1
           				else:
                    				print 'It was a draw! Nobody gets a point'
        				time.sleep(2)
        				clear()
        			if(pTotal>cTotal):
            				print 'You win. Here\'s a star!'
        			else:
            				print 'You lose. YOU LOSE A STAR CUZ YOU SUCK.'
        				time.sleep(2)
					print "Nice try Mario, but now you must return to the beginning!\n MWWWAAHAHAHAH!!"
					time.sleep(3)
					diceGame('Ghost')
					clear()

def getTime():
    n=time.localtime(time.time())
    return (n[4]*60+n[5])

def typingRound(roundNum,seconds,sentence):
    print 'Round',(str(roundNum)+': '+str(seconds)),'seconds'
    time.sleep(2)
    clear()
    print 'Go'
    time.sleep(.5)
    clear()
    num1=getTime()
    print sentence
    str1=raw_input()
    if(getTime()-num1<=seconds and (str1.lower()==sentence.lower())):
        return True
    else:
        return False
def typing():
    print 'You must type the following sentences. Case does not matter but spelling does. You will be told of your time limit'
    print 'When I say \'Go\', start typing the sentence that appears'
    time.sleep(5)
    r1=typingRound(1,6,'Snow white is an idiot')
    if(r1):
        print 'Well that was EASY! Let\'s see you try this one!'
        time.sleep(2)
        r2=typingRound(2,9,'This is totally the best game ever')
        if(r2):    
            print 'Maybe you\'re not as much of a cockroach as I thought. But you\'ll never make it past the next round!'
            time.sleep(4)
            r3=typingRound(3,18,'Jack and Jill went up the hill to fetch a pail of water')
            if(r3):
                print 'NOOOOOOO! You beat me!'
                print 'You recieved a star!'
            else:
                print'MWAHAHAHAHA! You lost!'
                print 'You lost a star!'
        else:
            print'MWAHAHAHAHA! You lost!'
            print 'You lost a star!'
    else:
        print'MWAHAHAHAHA! You lost!'
        print 'You lost a star!'
        time.sleep(3)
	clear()
	print 'So sorry, try again!'
	typing()
    time.sleep(4)
    clear()


begin()

if player=="m":
	global item_house
	global A_B
	print "Wow Mario..."
	time.sleep(1)
	print "Look out the window"
	time.sleep(2)
	print "What a beautiful night! I can see almost every single star in the sky!"
	time.sleep(2)
	print "Respond to Peach: "
	respond()
	print "Now try to make her laugh: "
	respond()
	time.sleep(1)
	print "Hahahaha, oh Mario, how you have your way with words!"
	time.sleep(3)
	clear()
	print "RRRRRRRRRRAAGGHHRRRHHAHGGHHRRR"
	time.sleep(1)
	print ".\n.\n.\n.\n."
	time.sleep (2)
	clear()
	print "."
	time.sleep(1)
	print ".."
	time.sleep(1)
	print "..."
	time.sleep(1)
	print "..........................................."
	time.sleep(1)
	clear()
	print "Mario..... What was that? :("
	time.sleep(1)
	print "What do you think happened? "
	respond()
	print "hmmmmmmmmmmm.. Whatever it was probably nothing.."
	time.sleep(2)
	clear()
	print "BAAAAAAAAANNNNNGGGG BOOOOOOOOMMMMMM!\nGRRRRRRRRRRRRRRRRRRRRRRRRRAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAHHHHHHHHHHHHHHHHHHHHHHH!!!!!!!!"
	time.sleep(2)
	clear()
	print "OHH NOO! MARIO the house is falling apart!! WHAT IS HAPPENING!?!?!?\nQUICKLY RUN AND GET OUT OF THE HOUSE!\nPick one item from the house to take with you: "
	item_house=raw_input()
	clear()
	print "MWWAAAAHHHAHAHAAAAHHHHHH!!!!!!!!!!"
	time.sleep(1)
	print "OOHH NOO!!!! NOT BOWSER!!"
	time.sleep(2)
	print "YESS it is me, the mighty and powerful Bowser!! I am here to not only destroy you mario, but to destroy the whole world!!!! MWWWWAAHHAHAHAHAHHHHHHHH!!"
	time.sleep(3)
	print "I aM hUngRy fOr soMeTHinG tO eAT!!! gIVe mE youR %s" %(item_house)
	time.sleep(1)
	print "Press A to give it to him and B to say no"
	A_B=raw_input()
	if A_B=="A":
		global strike1
		global y_n1
		global powerup
		global X_Y
		print "I aLwaYS knEw yoU wEre wEAK!! HAHAHA!!"
		time.sleep(2)
		print "NoW NOt onLy wiLl I TaKE yoUR %s, bUT aLSo, I wiLl TAke yOur gIRl!!" %(item_house)
		time.sleep(2)
		print "Please Mario save me! Fight for me!"
		time.sleep(2)
		print "How would you like to first strike Bowser?"
		strike1=raw_input()
		print "I'm coming Peach! (Mario strikes Bowser with a %s)" %(strike1)
		time.sleep(2)
		clear()
		print "%s does 0 damage" %(strike1)
		time.sleep(2)
		clear()
		print "MWAHAHA. dO yoU reaLlY wanT TO fIghT me??!?"
		print "Yes or no?"
		y_n1=raw_input()
		clear()
		print "SSMMAAACCCCCKKKKKKKKKKKKKKKK!!!!!!!!!!!!!"
		time.sleep(2)
		clear()
		print "......................Two Days Later......................"
		time.sleep(2)
		clear()
		time.sleep(2)
		print "Mario?... Are you awake?"
		print "Oh Mario! Thank god you are awake! :)\nThe world needs your help!"
		time.sleep(2)
		print "Where.... Where am I?"
		time.sleep(2)
		print "Don't you remember?"
		time.sleep(2)
		print "Bowser came to earth and not only took kidnapped Peach, but also wants to destroy the world!"
		time.sleep(3)
		print "Well are you gonna help us?"
		respond()
		print "You know what, the answer doesn't even matter. Of course you will!"
		time.sleep(2)
		print "You have to journey through the Forest Maze and then the Staircase to Doom in order to get to Bowser and his castle in the sky."
		time.sleep(3)
		print "Here are 3 of the 5 Earth saving stars. In order to save the world, you will need to get all 5."
		time.sleep(2)
		print "Now I can give you one power up to help you on your journey. Which power up do you want to take?"
		time.sleep(2)
		print "Hit F for Fire Mario, S for Star Mario, W for Wing Mario"
		powerup=raw_input()
		if powerup=="F":
			print "Good Choice! That is a HOT item at our store ;)"
			time.sleep(2)
			print "'Fire Mario' will help you in your fight against Bowser by allowing you to hit him with fireballs"
			powerup=['Fire Mario']			
			time.sleep(3)
		elif powerup=="S":
			print "Good Choice! This is the BRIGHTEST item at our store ;)"
			time.sleep(2)
			print "'Star Mario' will help you in your fight against Bowser by keeping you invincible from his attacks for a period of time"
			powerup=['Star Mario']
			time.sleep(3)
		elif powerup=="W":
			print "Good Choice! This is the HIGHEST item on our shelves ;)"
			time.sleep(2)
			print "'Wing Mario' will help you in your fight against Bowser by allowing you to fly over him to either attack him or defend yourself"
			powerup=['Wing Mario']
			time.sleep(3)
		print "Now that you have choosen %s as your weapon, you are ready to fight! Go off and save the world! May the odds be ever in your favor!" %(powerup)
		time.sleep(4)
		clear()
		print "Would you like to continue? Press RETURN to go into the forest."
		respond()
		clear()
		print "**********IN THE FOREST MAZE**********"
		time.sleep(2)
		clear()
		print "How do you feel Mario?"
		emotion=raw_input()
		print "Why do you feel %s?" %(emotion)
		emotion1=raw_input()
		print "Reaallllllly??? Well do you know who I am???"
		respond()
		print "I AM THE GHOST OF THE FOREST MAZE!!!!"
		time.sleep(2)
		print "No one shall pass my mythical maze without going through me first!"
		time.sleep(2)
		print "NOW mArIo... you have two choices, you can try to get by me and die, or you can flee and I will haunt you forever!!!"
		time.sleep(2)
		print "Press X to fight and Y to flee"
		X_Y=str(raw_input())
	 	if X_Y=="X":
			print "Interesting choice Mario... so I guess you are prepared to die!"
			time.sleep(2)
			print "Let the fighting begin!!!"
			time.sleep(2)
			clear()
			diceGame('Ghost')
		elif X_Y=="Y":
			print "So you want to be haunted... well then...."
			time.sleep(2)
			clear()
			print "RUNNNNNNNNNNN"
			time.sleep(2)
			clear()
			print "Mario has peed his pants and now has to go back home. Press RETURN to try again and CTRL-C to quit"
			respond()
			start()
		else:
			print "I'm sorry, try again!"
			start()
		clear()
		print "I can't believe you beat me!"
		time.sleep(2)
		print "Take your damn star and leave!!!!!"
		time.sleep(2)
		print "\nCongratulations Mario, You Now Have 4 Stars! Next You Must Face The Terrible Tower Guard To The Staircase Of Doom"
		time.sleep(4)
		clear()
		print "********AT THE STAIRCASE OF DOOM*******"
		print "Good Evening Mario.... I have been waiting a very long time to fight you!"
		time.sleep(3)
		print "There will be NO getting around me... so... what are you waiting for?? Let's fight!!!"
		print "Press X to fight and Y to flee"
		X_Y2=str(raw_input())
		if X_Y2=="X":
			print "Let us indulge in a little game I like to call THE TYPING GAME! MWAHAHAH"
			time.sleep(4)
			typing()
		elif X_Y2=="Y":
			print "Fine Mario! Run like a little boy, I will just set you on fire!!!"
			time.sleep(2)
			print "BUUUUUUUUUUUUURRRRRRRRRRRRRRRRRRRRRRRRNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN"
			time.sleep(2)
			clear()
			print "I'm sorry, try again!"
			time.sleep(2)
			clear()
			start()
		clear()
		print "OMG I guess I must let you go and continue on your journey :'-("
		time.sleep(3)
		print "Say Goodbye to the tower guard:"
		gbye=raw_input()
		print "F@%& YOU MARIO! I WILL GET REVENGE!"
		time.sleep(3)
		clear()
		print "Congratulations Mario!\n You have received all 5 stars and have saved the world!!! HORRRAYYYY!!!!"
		time.sleep(3)
		print "Now go get Peach from Bowser's castle!"
		time.sleep (3)
		clear()
		print "**********BOWSER'S CASTLE**********"
		clear()
		print "WHAt? hOW iS thIs poSibLe!!!! I thOugHt I KiLLed yoU!?!?!?!?"
		time.sleep(2)
		print "Respond to Bowser:"
		respond()
		print "Well you are not getting Peach back!"
		time.sleep(2)
		print "(Press RETURN to take out your %s and use it to kill Bowser)" %(powerup)
		respond()
		print "Die Bowser!"
		time.sleep(1)
		print "NooOooOOooooOOOOOoOOo!!!!!!!"
		time.sleep(2)
		clear()
		print "......................................................."
		time.sleep(1)
		print "......................................................."
		time.sleep(1)
		clear()
		print "You did it Mario! You saved me AND the world!"
		time.sleep(3)
		print "How about a big kiss?"
		time.sleep(2)
		clear()
		print "YOU WIN!!!!!!!"
		time.sleep(10)
		clear()
	elif A_B=="B":
		global insult
		print "NO?!?!?!?!?!?!?!"
		time.sleep(1)
		print "HoW daRe yoU DiSRespeCt mY authORity!!!!"
		time.sleep(2)
		print "Now insult him: "
		insult=raw_input()
		print "WHAT?!?! THAT'S IT!!! You aRE doNe Mario!!!"
		time.sleep(2)
		print "Nooooo Mario!!!"
		time.sleep(1)
		print "**********munching noises**********"
		clear()
		print "Nice try, but you have died.\nWould you like to restart (Press RETURN to continue and CTRL-C to quit)?"
		cont()
		start()
	else:
		print "Sorry... try again!"
		start()
elif player=="l":
	global item_house
	global A_B
	print "Wow Luigi..."
	time.sleep(1)
	print "Look out the window"
	time.sleep(2)
	print "What a beautiful night! I can see almost every single star in the sky!"
	time.sleep(2)
	print "Respond to Daisy: "
	respond()
	print "Now try to make her laugh: "
	respond()
	print "Hahahaha, oh Luigi, how you have your way with words!"
	time.sleep(3)
	clear()
	print "RRRRRRRRRRAAGGHHRRRHHAHGGHHRRR"
	time.sleep(1)
	print ".\n.\n.\n.\n."
	time.sleep (2)
	clear()
	print "."
	time.sleep(1)
	print ".."
	time.sleep(1)
	print "..."
	time.sleep(1)
	print "..........................................."
	time.sleep(1)
	clear()
	print "Luigi..... What was that? :("
	time.sleep(1)
	print "What do you think happened? "
	respond()
	print "hmmmmmmmmmmm.. Whatever it was probably nothing.."
	time.sleep(2)
	clear()
	print "BAAAAAAAAANNNNNGGGG BOOOOOOOOMMMMMM!\nGRRRRRRRRRRRRRRRRRRRRRRRRRAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAHHHHHHHHHHHHHHHHHHHHHHH!!!!!!!!"
	time.sleep(2)
	clear()
	print "OHH NOO! Luigi the house is falling apart!! WHAT IS HAPPENING!?!?!?\nQUICKLY RUN AND GET OUT OF THE HOUSE!\nPick one item from the house to take with you: "
	item_house=raw_input()
	clear()
	print "MWWAAAAHHHAHAHAAAAHHHHHH!!!!!!!!!!"
	time.sleep(1)
	print "OOHH NOO!!!! NOT BOWSER!!"
	time.sleep(2)
	print "YESS it is me, the mighty and powerful Bowser!! I am here to not only destroy you Luigi, but to destroy the whole world!!!! MWWWWAAHHAHAHAHAHHHHHHHH!!"
	time.sleep(3)
	print "I aM hUngRy fOr soMeTHinG tO eAT!!! gIVe mE youR %s" %(item_house)
	time.sleep(1)
	print "Press A to give it to him and B to say no"
	A_B=raw_input()
	if A_B=="A":
		global strike1
		global y_n1
		global powerup
		global X_Y
		print "I aLwaYS knEw yoU wEre wEAK!! HAHAHA!!"
		time.sleep(2)
		print "NoW NOt onLy wiLl I TaKE yoUR %s, bUT aLSo, I wiLl TAke yOur gIRl!!" %(item_house)
		time.sleep(2)
		print "Please Luigi save me! Fight for me!"
		time.sleep(2)
		print "How would you like to first strike Bowser?"
		strike1=raw_input()
		print "I'm coming Daisy! (Luigi strikes Bowser with a %s)" %(strike1)
		time.sleep(2)
		clear()
		print "%s does 0 damage" %(strike1)
		time.sleep(2)
		clear()
		print "MWAHAHA. dO yoU reaLlY wanT TO fIghT me??!?"
		print "Yes or no?"
		y_n1=raw_input()
		clear()
		print "SSMMAAACCCCCKKKKKKKKKKKKKKKK!!!!!!!!!!!!!"
		time.sleep(2)
		clear()
		print "......................Two Days Later......................"
		time.sleep(2)
		clear()
		time.sleep(2)
		print "Luigi?... Are you awake?"
		print "Oh Luigi! Thank god you are awake! :)\nThe world needs your help!"
		time.sleep(2)
		print "Where.... Where am I?"
		time.sleep(2)
		print "Don't you remember?"
		time.sleep(2)
		print "Bowser came to earth and not only took kidnapped Daisy, but also wants to destroy the world!"
		time.sleep(3)
		print "Well are you gonna help us?"
		respond()
		print "You know what, the answer doesn't even matter. Of course you will!"
		time.sleep(2)
		print "You have to journey through the Forest Maze and then the Staircase to Doom in order to get to Bowser and his castle in the sky."
		time.sleep(3)
		print "Here are 3 of the 5 Earth saving stars. In order to save the world, you will need to get all 5."
		time.sleep(2)
		print "Now I can give you one power up to help you on your journey. Which power up do you want to take?"
		time.sleep(2)
		print "Hit F for Fire Luigi, S for Star Luigi, W for Wing Luigi"
		powerup=raw_input()
		if powerup=="F":
			print "Good Choice! That is a HOT item at our store ;)"
			time.sleep(2)
			print "'Fire Luigi' will help you in your fight against Bowser by allowing you to hit him with fireballs"
			powerup=['Fire Luigi']			
			time.sleep(3)
		elif powerup=="S":
			print "Good Choice! This is the BRIGHTEST item at our store ;)"
			time.sleep(2)
			print "'Star Luigi' will help you in your fight against Bowser by keeping you invincible from his attacks for a period of time"
			powerup=['Star Luigi']
			time.sleep(3)
		elif powerup=="W":
			print "Good Choice! This is the HIGHEST item on our shelves ;)"
			time.sleep(2)
			print "'Wing Luigi' will help you in your fight against Bowser by allowing you to fly over him to either attack him or defend yourself"
			powerup=['Wing Luigi']
			time.sleep(3)
		print "Now that you have choosen %s as your weapon, you are ready to fight! Go off and save the world! May the odds be ever in your favor!" %(powerup)
		time.sleep(4)
		clear()
		print "Would you like to continue? Press RETURN to go into the forest."
		respond()
		clear()
		print "**********IN THE FOREST MAZE**********"
		time.sleep(2)
		clear()
		print "How do you feel Luigi?"
		emotion=raw_input()
		print "Why do you feel %s?" %(emotion)
		emotion1=raw_input()
		print "Reaallllllly??? Well do you know who I am???"
		respond()
		print "I AM THE GHOST OF THE FOREST MAZE!!!!"
		time.sleep(2)
		print "No one shall pass my mythical maze without going through me first!"
		time.sleep(2)
		print "NOW Luigi... you have two choices, you can try to get by me and die, or you can flee and I will haunt you forever!!!"
		time.sleep(2)
		print "Press X to fight and Y to flee"
		X_Y=str(raw_input())
	 	if X_Y=="X":
			print "Interesting choice Luigi... so I guess you are prepared to die!"
			time.sleep(2)
			print "Let the fighting begin!!!"
			time.sleep(2)
			clear()
			diceGame('Ghost')
		elif X_Y=="Y":
			print "So you want to be haunted... well then...."
			time.sleep(2)
			clear()
			print "RUNNNNNNNNNNN"
			time.sleep(2)
			clear()
			print "Luigi has peed his pants and now has to go back home. Press RETURN to try again and CTRL-C to quit"
			respond()
			start()
		else:
			print "I'm sorry, try again!"
			start()
		clear()
		print "I can't believe you beat me!"
		time.sleep(2)
		print "Take your damn star and leave!!!!!"
		time.sleep(2)
		print "\nCongratulations Luigi, You Now Have 4 Stars! Next You Must Face The Terrible Tower Guard To The Staircase Of Doom"
		time.sleep(4)
		clear()
		print "********AT THE STAIRCASE OF DOOM*******"
		print "Good Evening Luigi.... I have been waiting a very long time to fight you!"
		time.sleep(3)
		print "There will be NO getting around me... so... what are you waiting for?? Let's fight!!!"
		print "Press X to fight and Y to flee"
		X_Y2=str(raw_input())
		if X_Y2=="X":
			print "Let us indulge in a little game I like to call THE TYPING GAME! MWAHAHAH"
			time.sleep(4)
			typing()
		elif X_Y2=="Y":
			print "Fine Luigi! Run like a little boy, I will just set you on fire!!!"
			time.sleep(2)
			print "BUUUUUUUUUUUUURRRRRRRRRRRRRRRRRRRRRRRRNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN"
			time.sleep(2)
			clear()
			print "I'm sorry, try again!"
			time.sleep(2)
			clear()
			start()
		clear()
		print "OMG I guess I must let you go and continue on your journey :'-("
		time.sleep(3)
		print "Say Goodbye to the tower guard:"
		gbye=raw_input()
		print "F@%& YOU Luigi! I WILL GET REVENGE!"
		time.sleep(3)
		clear()
		print "Congratulations Luigi!\n You have received all 5 stars and have saved the world!!! HORRRAYYYY!!!!"
		time.sleep(3)
		print "Now go get Daisy from Bowser's castle!"
		time.sleep (3)
		clear()
		print "**********BOWSER'S CASTLE**********"
		clear()
		print "WHAt? hOW iS thIs poSibLe!!!! I thOugHt I KiLLed yoU!?!?!?!?"
		time.sleep(2)
		print "Respond to Bowser:"
		respond()
		print "Well you are not getting Daisy back!"
		time.sleep(2)
		print "(Press RETURN to take out your %s and use it to kill Bowser)" %(powerup)
		respond()
		print "Die Bowser!"
		time.sleep(1)
		print "NooOooOOooooOOOOOoOOo!!!!!!!"
		time.sleep(2)
		clear()
		print "......................................................."
		time.sleep(1)
		print "......................................................."
		time.sleep(1)
		clear()
		print "You did it Luigi! You saved me AND the world!"
		time.sleep(3)
		print "How about a big kiss?"
		time.sleep(2)
		clear()
		print "YOU WIN!!!!!!!"
		time.sleep(10)
		clear()
	elif A_B=="B":
		global insult
		print "NO?!?!?!?!?!?!?!"
		time.sleep(1)
		print "HoW daRe yoU DiSRespeCt mY authORity!!!!"
		time.sleep(2)
		print "Now insult him: "
		insult=raw_input()
		print "WHAT?!?! THAT'S IT!!! You aRE doNe Luigi!!!"
		time.sleep(2)
		print "Nooooo Luigi!!!"
		time.sleep(1)
		print "**********munching noises**********"
		clear()
		print "Nice try, but you have died.\nWould you like to restart (Press RETURN to continue and CTRL-C to quit)?"
		cont()
		start()
	else:
		print "Sorry... try again!"
		start()
else:
	start()
