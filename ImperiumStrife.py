#!/usr/bin/env python3

#=====================================================
#
# Imperium Strife
#
#=====================================================
#
#
#@version	0 
#@link		https://github.com/chriswmorris/
#@authors	Chris Morris

import sys
import random
import time
import Inventory as inv
import UserMoves as moves
import AI as ai




def KingdomCreate():
	global playername
	# This sets the player's name
	print("Welcome to Imperium Strife")
	print("By Chris Morris")
	print("github.com/chriswmorris/")
	print()
	print("================================================")
	print("Please choose a name for your Kingdom: ")
	print()
	playername = input("Name: ")
	if not playername:
		playername = "Player1"
	print()
	print("Your Kingdom's Name: " + playername )
	print()
	print("================================================")


def Order():
	global playerturns
	#This determines the order
	print()
	playerturns = ["Player1(You)","Player2(AI)","Player3(AI)","Player4(AI)","Player5(AI)"]
	random.shuffle(playerturns)
	prettyturns = ', '.join(playerturns)
	print("Randomly chose the turn order. The order is....")
	print()
	print(prettyturns)
	print()
	print("================================================")

def PlayerTurn():

	menu = (""" 

MENU	

1) Invade!
2) Choose a card
3) Obtain 30 Soldiers
4) Obtain 30 Food
5) Gamble at the Pub
6) Help

Type in the number 1-6 
		""")

	helpchoice = ("""
=================================================
Invade:	Fight the enemy of your choosing! Heroes 
	and Spies can be played here.

Choose a card: Choose a card by random. Each card 
	has a chance of gaining or losing Food and 
	Soldiers. You can also obtain Spies and Heroes.

Gamble at the Pub: Chance to gain 5-30 Food and
	5-30 Soldiers

=================================================
		""")

	print("====" + playername + "====")
	print("So it's your turn!")
	moves.EatFood()
	print()
	inv.Player1Inventory()
	print("What do you want to do, " + playername +"?")
	

	while True:
		print(menu)
		move = input("Selection: ")
		if not move:
			break

		if move == "1":
			print("Are you sure you want to start a war?")
			warchoice = input("y/n? ")

			if warchoice == "y":
				moves.FoodCheck()
				moves.StartWar()
				input("Press [ENTER] to end turn")
				break

			else:
				break

		if move == "2":
			moves.Cards()
			moves.FoodCheck()
			input("Press [ENTER] to end turn")
			break
		if move == "3":
			moves.AddSoldiers()
			moves.FoodCheck()
			input("Press [ENTER] to end turn")
			break

		if move == "4":
			moves.AddFood()
			moves.FoodCheck()
			input("Press [ENTER] to end turn")
			break

		if move == "5":
			moves.Gamble()
			moves.FoodCheck()
			input("Press [ENTER] to end turn")
			break

		if move == "6":
			print(helpchoice)
			input("Press [ENTER] to continue")



def Player2Turn():

	print("====Frugalis Republic====")
	print("So it's the AI's turn")
	ai.EatFood(aiplayer=2)
	print()
	inv.Player2Inventory()
	ai.P2Move()
	ai.FoodCheck(aiplayer=2)
	input("Press [ENTER] to continue")
	

def Player3Turn():

	print("====Dutchy of Alea====")
	print("So it's the AI's turn")
	ai.EatFood(aiplayer=3)
	print()
	inv.Player3Inventory()
	ai.P3Move()
	ai.FoodCheck(aiplayer=3)
	input("Press [ENTER] to continue")
	

def Player4Turn():
	print("====Imperium Malum====")
	print("So it's the AI's turn")
	ai.EatFood(aiplayer=4)
	print()
	inv.Player4Inventory()
	ai.P4Move()
	ai.FoodCheck(aiplayer=4)
	input("Press [ENTER] to continue")
	

def Player5Turn():
	print("====Imbecile Kingdom====")
	print("So it's the AI's turn")
	ai.EatFood(aiplayer=5)
	print()
	inv.Player5Inventory()
	ai.P5Move()
	ai.FoodCheck(aiplayer=5)
	input("Press [ENTER] to continue")


def WinChecker():

# Player 1 Win

	if inv.Player1Lost == False:
		if inv.Player2Lost == True:
			if inv.Player3Lost == True:
				if inv.Player4Lost == True:
					if inv.Player5Lost == True:
						inv.Player1Win = True

# Player 2 Win

	if inv.Player2Lost == False:
		if inv.Player1Lost == True:
			if inv.Player3Lost == True:
				if inv.Player4Lost == True:
					if inv.Player5Lost == True:
						inv.Player2Win = True


# Player 3 Win

	if inv.Player3Lost == False:
		if inv.Player2Lost == True:
			if inv.Player1Lost == True:
				if inv.Player4Lost == True:
					if inv.Player5Lost == True:
						inv.Player3Win = True

# Player 4 Win

	if inv.Player4Lost == False:
		if inv.Player2Lost == True:
			if inv.Player1Lost == True:
				if inv.Player3Lost == True:
					if inv.Player5Lost == True:
						inv.Player4Win = True

# Player 5 Win

	if inv.Player5Lost == False:
		if inv.Player2Lost == True:
			if inv.Player1Lost == True:
				if inv.Player3Lost == True:
					if inv.Player4Lost == True:
						inv.Player5Win = True



def Win(player):

	if player == 1:
		print("Congrats! You Win!")
		sys.exit(0)
	
	if player == 2:
		print("The Frugalis Republic has Won!")
		sys.exit(0)

	if player == 3:
		print("The Dutchy of Alea has Won!")
		sys.exit(0)

	if player == 4:
		print("The Imperium Malum has Won!")
		sys.exit(0)

	if player == 5:
		print("The Imbecile Kingdom has Won!")
		sys.exit(0)


#==========MAIN FUNCTION============

def main():
	KingdomCreate()
	Order()

	while True:
		for turn in playerturns:

			WinChecker()

			if inv.Player1Win == True:
				Win(player=1)

			if inv.Player2Win == True:
				Win(player=2)

			if inv.Player3Win == True:
				Win(player=3)

			if inv.Player4Win == True:
				Win(player=4)

			if inv.Player5Win == True:
				Win(player=5)

			print()
			print("It's " + turn + "'s Turn")
			print()

			if turn == "Player1(You)":
				if inv.Player1Lost == True:
					print(playername + " has lost so their turn is skipped.")
					pass
				if inv.Player1Lost == False:
					PlayerTurn()	

			if turn == "Player2(AI)":
				if inv.Player2Lost == True:
					print("Frugalis Republic has lost so their turn is skipped.")
					pass

				if inv.Player2Lost == False:
					Player2Turn()
			

			if turn == "Player3(AI)":
				if inv.Player3Lost == True:
					print("The Dutchy of Alea has lost so their turn is skipped.")
					pass

				if inv.Player3Lost == False:
					Player3Turn()				

			if turn == "Player4(AI)":
				if inv.Player4Lost == True:
					print("The Imperium Malum has lost so their turn is skipped.")
					pass

				if inv.Player4Lost == False:
					Player4Turn()	


			if turn == "Player5(AI)":
				if inv.Player5Lost == True:
					print("The Imbecile Kingdom has lost so their turn is skipped.")
					pass

				if inv.Player5Lost == False:
					Player5Turn()	

			

if __name__ == '__main__':
	main()