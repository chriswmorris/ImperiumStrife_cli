#!/usr/bin/env python3

import random


#This class stores the inventory for the players 


#=========PLAYER 1=========
global Player1Food
global Player1Soldiers
global Player1Heroes
global Player1Spies
global Player1Land 
global Player1Lost
global Player1Win


Player1Food = 30
Player1Soldiers = 10
Player1Heroes = 0
Player1Spies = 0
Player1Land = 1
Player1Lost = False
Player1Win = False

#=========PLAYER 2=========

global Player2Food
global Player2Soldiers
global Player2Heroes
global Player2Spies
global Player2Land 
global Player2Lost
global Player2Win

Player2Food = 30
Player2Soldiers = 10
Player2Heroes = 0
Player2Spies = 0
Player2Land = 1
Player2Lost = False
Player2Win = False

#=========PLAYER 3=========
global Player3Food
global Player3Soldiers
global Player3Heroes
global Player3Spies
global Player3Land 
global Player3Lost
global Player5Win

Player3Food = 30
Player3Soldiers = 10
Player3Heroes = 0
Player3Spies = 0
Player3Land = 1
Player3Lost = False
Player3Win = False

#=========PLAYER 4=========
global Player4Food
global Player4Soldiers
global Player4Heroes
global Player4Spies
global Player4Land 
global Player4Lost
global Player4Win

Player4Food = 30
Player4Soldiers = 10
Player4Heroes = 0
Player4Spies = 0
Player4Land = 1
Player4Lost = False
Player4Win = False

#=========PLAYER 5=========

global Player5Food
global Player5Soldiers
global Player5Heroes
global Player5Spies
global Player5Land 
global Player5Lost
global Player5Win

Player5Food = 30
Player5Soldiers = 10
Player5Heroes = 0
Player5Spies = 0
Player5Land = 1
Player5Lost = False
Player5Win = False


def Player1Inventory():

	print("===============Your Inventory===========")
	print("||                                     ||")
	print("|| Food || Soldiers || Heroes || Spies ||")
	print("||-------------------------------------||")
	print("||  " + str(Player1Food) + "        " + str(Player1Soldiers) + "         " + str(Player1Heroes) + "         " + str(Player1Spies) + "   ||")
	print("||                                     ||")
	print("||                                     ||")
	print("========================================")

def Player2Inventory():
	print("Player2's Inventory")
	print("Food: " + str(Player2Food))
	print("Soldiers: " + str(Player2Soldiers))
	print("Heroes: " + str(Player2Heroes))
	print("Spies: " + str(Player2Spies))
	print()
	
def Player3Inventory():
	print("Player3's Inventory")
	print("Food: " + str(Player3Food))
	print("Soldiers: " + str(Player3Soldiers))
	print("Heroes: " + str(Player3Heroes))
	print("Spies: " + str(Player3Spies))
	print()

def Player4Inventory():

	print("Player4's Inventory")
	print("Food: " + str(Player4Food))
	print("Soldiers: " + str(Player4Soldiers))
	print("Heroes: " + str(Player4Heroes))
	print("Spies: " + str(Player4Spies))
	print()

def Player5Inventory():

	print("Player5's Inventory")
	print("Food: " + str(Player5Food))
	print("Soldiers: " + str(Player5Soldiers))
	print("Heroes: " + str(Player5Heroes))
	print("Spies: " + str(Player5Spies))
	print()