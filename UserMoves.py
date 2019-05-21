#!/usr/bin/env python3

import random
import time
import Inventory as inv


# This is the moves that the user can make


def EatFood():
	percent = random.randint(5,15)/100
	eatamount = inv.Player1Soldiers * percent
	eaten = round(eatamount)
	inv.Player1Food -= eaten
	print("Your soldiers ate " + str(eaten) + " food this turn")


def FoodCheck():
	soldierleaves = inv.Player1Soldiers - inv.Player1Food
	if inv.Player1Soldiers > inv.Player1Food:
		inv.Player1Soldiers -=soldierleaves
		print(str(soldierleaves) + " left your army because you didn't have enough food!")


def AddFood():
	inv.Player1Food += 30
	print()
	print("Your Kingdom just farmed 30 food! (+30 Food)")
	print("You now have " + str(inv.Player1Food) +  " Food!")
	print()

		
def AddSoldiers():
	inv.Player1Soldiers += 30
	print()
	print("Your Kingdom just recuited 30 Soldiers! (+30 Soliders)")
	print("You now have " + str(inv.Player1Soldiers) + " Soldiers")
	print()


def Gamble():

	#Basically the user gets 5-35 food and 5-35 soldiers

	randfood = random.randint(5,35)
	randsoldiers = random.randint(5,35)
	totals = randfood + randsoldiers
	print()
	print("You go to the pub and try your hand at a game of dice...")
	print("At the table sits prominent Lords and Barons from far off lands.")
	print()

	if totals == 10:
		print("You gambled and lost big to Lord Al Kaholic!")
		print("You got " + str(randfood) + " food and " + str(randsoldiers) + " soliders.")

	if 11 <= totals <= 20:
		print("You gambled and lost to Lord Jussfar Ted.")
		print("You got " + str(randfood) + " food and " + str(randsoldiers) + " soliders.")

	if 21 <= totals <= 30:
		print("You gambled and lost when you diced agianst Lord Ben Dover.")
		print("You got " + str(randfood) + " food and " + str(randsoldiers) + " soliders.")

	if 31 <= totals <= 40:
		print("You did okay when you diced agianst Baron Neu Trall.")
		print("You got " + str(randfood) + " food and " + str(randsoldiers) + " soliders.")

	if 41 <= totals <= 50:
		print("You did well when you diced agianst Baron Pierre Pants.")
		print("You got " + str(randfood) + " food and " + str(randsoldiers) + " soliders.")

	if 51 <= totals <= 59:
		print("You did very well at the tables! Lord Moe Ronn could not keep up!")
		print("You got " + str(randfood) + " food and " + str(randsoldiers) + " soliders.")

	if 60 <= totals <= 69:
		print("You did excellent at the tables! Lord Suhm L. Ebuht said he has never seen such skill!")
		print("You got " + str(randfood) + " food and " + str(randsoldiers) + " soliders.")

	if totals == 70:
		print("DANG!! YOU DID EXTREMELY WELL! Everyone in the pub cheers and you earned a plaque with your name on it!")
		print("You got " + str(randfood) + " food and " + str(randsoldiers) + " soliders.")

	inv.Player1Food += randfood
	inv.Player1Soldiers += randsoldiers
	print()


def Cards():

	#The player chooses a card. There will be a possible 15 cards.

	roll = random.randint(1,15)

	print(str(roll))

	herolist = ("Achilles","Gandalf","Hercules","Thor","Aragorn","Legolas","Dumbledore","Jack Sparrow","Odysseus","Perseus","Theseus",
		"Julius Caesar","Alexander the Great","Trajan","Augustus","Hannibal Barca", "St. Joan of Ark", "Charlemagne", "Lancelot", "Robin Hood", "William Wallace")

	hero = random.choice(herolist)

	if roll == 1:
		inv.Player1Spies += 1
		print("Your Intelligence Agency successfully placed a spy in the enemy ranks!")
		print("You got a Spy!")
		print("You now have " + str(inv.Player1Spies) + " Spies.")

	if roll == 2:
		inv.Player1Spies += 1
		print("A Soldier from the enemy's army has took up your cause!")
		print("You got a Spy!")
		print("You now have " + str(inv.Player1Spies) + " Spies.")

	if roll == 3:
		inv.Player1Heroes += 1
		print("The Hero: " + hero + " has joined your campaign!")
		print("You got a Hero!")

	if roll == 4:
		inv.Player1Heroes += 1
		print("The Hero: " + hero + " believes in your cause and joins your army!")
		print("You got a Hero!")

	if roll == 5:
		inv.Player1Soldiers += 50
		print("You save a local village from Bandits. 50 men from the village take up your cause!")
		print("You got 50 Soldiers!")

	if roll == 6:
		inv.Player1Food += 50
		print("A local village thanks you for saving them from Raiders. They give you food.")
		print("You got 50 Food!")

	if roll == 7:
		inv.Player1Soldiers += 100
		print("Soldiers from an enemy army defect to your side!")
		print("You got 100 Soldiers!")

	if roll == 8:
		inv.Player1Food += 100
		print("Your loyal subjects have bountiful harvest!")
		print("You got 100 Food!")

	if roll == 9:
		plague = inv.Player1Soldiers * .20
		ploss = round(plague)
		inv.Player1Soldiers -= ploss
		print("Some soldiers in your army get the plague.")
		print(str(ploss) + " soldiers die from it.")
		
	if roll == 10:
		locusts = inv.Player1Food * .20
		lloss = round(locusts)
		inv.Player1Food -= lloss
		print("Some locusts eat your subjects' crops!")
		print("You lose " + str(lloss) + " food.")

	if roll == 11:
		badplague = inv.Player1Soldiers * .60
		badploss = round(badplague)
		inv.Player1Soldiers -= badploss
		print("A bad plague runs rampant in your army's camp.")
		print(str(badploss) + " soldiers die from it.")

	if roll == 12:
		badlocusts = inv.Player1Food * .60
		badlloss = round(badlocusts)
		inv.Player1Food -= badlloss
		print("A horde of locusts eat your subjects' crops!")
		print("You lose " + str(badlloss) + " food.")

	if roll == 13:
		inv.Player1Food +=30
		inv.Player1Soldiers -=30
		print("30 soldiers decide to quit and move to a farm.")
		print("You gain 30 food but lose 30 soldiers")

	if roll == 14:
		inv.Player1Food -= 30
		inv.Player1Soldiers += 30
		print("You host a feast for your army. Some farmers join just cause they want to join the feast!")
		print("You lose 30 food but gain 30 soldiers.")

	if roll == 15:
		inv.Player1Heroes += 1
		inv.Player1Spies += 1
		print("The famous hero " + hero + " has volunteered to join your army!")
		print("The enemy loses morale and you gain a spy!")
		print("You got a hero and a spy!!!")


def StartWar():
		#This is when the player initializes war with any of the AI
		# 
		#How it works:
		#
		# Get Player's soldier number
		# Get AI enemy's soldier number
		#
		# Ask player if they want to use spies or heros 
		#	If so, calculate bonuses
		#
		# Then AI will always add in spies and heroes
		#
		# Hero Calculations:
		#
		# Soliders + (Soliders * (Number of heroes * .10)) == p1power
		# Soldiers + (Soldiers * (Number of heroes * .10)) == aipower
		#
		# Spy Calculators:
		#
		# p1power - (Soldiers * (Number of ai spies * .10)) == totalp1power
		# aipower - (Soldiers * Number of p1 spies * .10)) == totalaipower
		#
		# Player1 rolls 1-12 == p1luck
		# AI rolls 1-12 == ailuck
		#
		# Battles will be like this:
		# 
		# (totalp1power + (p1luck*2)) * (Player1Land * .1) = p1army
		# (totalaipower + (ailuck*2)) * (Ailand * .1) = aiarmy
		#
		# Bigger number army wins between p1 and ai army
		# 
		# The loser loses indefinetly, the winner gets their land
		
	war = True

	while war:
		print("Who would you like to invade?")
		print()
		print("1) Frugalis Republic (Green) - Player2")
		print("2) Dutchy of Alea (Yellow) - Player3")
		print("3) Imperium Malum (Black) - Player4")
		print("4) Imbecile Kingdom (Orange) - Player5")
		print()


		invade = input("Selection: ")

		if invade == "1":
			if inv.Player2Lost == True:
				print("They already lost! Choose another")
				pass

			if inv.Player2Lost == False:
				print("Initiating War with the Frugalis Republic!")
				War(invade = 2)
				break

		if invade == "2":
			if inv.Player3Lost == True:
				print("They already lost! Choose another")
				pass

			if inv.Player3Lost == False:
				print("Initiating War with the Dutchy of Alea!")
				War(invade = 3)
				break

		if invade == "3":
			if inv.Player4Lost == True:
				print("They already lost! Choose another")
				pass

			if inv.Player4Lost == False:
				print("Initiating War with Imperium Malum!")
				War(invade = 4)
				break

		if invade == "4":
			if inv.Player5Lost == True:
				print("They already lost! Choose another")
				pass

			if inv.Player5Lost == False:
				print("Initiating War with Imbecile Kingdom!")
				War(invade = 5)
				break
						

	
def War(invade):

	if invade == 2:
		aisoldiers = inv.Player2Soldiers 
		aiheroes = inv.Player2Heroes
		aispies = inv.Player2Spies
		ailand = inv.Player2Land
		ailoss = inv.Player2Lost

	if invade == 3:
		aisoldiers = inv.Player3Soldiers
		aiheroes = inv.Player3Heroes
		aispies = inv.Player3Spies
		ailand = inv.Player3Land
		ailoss = inv.Player3Lost

	if invade == 4:
		aisoldiers = inv.Player4Soldiers
		aiheroes = inv.Player4Heroes
		aispies = inv.Player4Spies
		ailand = inv.Player4Land
		ailoss = inv.Player4Lost
	
	if invade == 5:
		aisoldiers = inv.Player5Soldiers
		aiheroes = inv.Player5Heroes
		aispies = inv.Player5Spies
		ailand = inv.Player5Land
		ailoss = inv.Player5Lost

	usersoldiers = inv.Player1Soldiers
	userland = inv.Player1Land	

	print()

	askh = True
	while askh:

		if inv.Player1Heroes >= 1:
			print("Would you like to use any Heroes?")
			heroes = input("y/n: ")
			if heroes == "y":
				print("How many? You have " + str(inv.Player1Heroes) + " Heroes.")
				hnumber = int(input("Answer: "))

				if hnumber > inv.Player1Heroes:
					print("You don't have that many Heroes!")
					askh = True	

				if hnumber <= inv.Player1Heroes:
					userheroes = hnumber
					inv.Player1Heroes -= hnumber
					print("You are going to use " + str(userheroes) + " Hero(es)")
					print("You have " + str(inv.Player1Heroes) + " Hero(es) left.")
					askh = False

			else:
				userheroes = 0
				askh = False	
				

		if inv.Player1Heroes == 0:
			userheroes = 0
			askh = False

	asks = True
	while asks:

		if inv.Player1Spies >= 1:
			print("Would you like to use any Spies?")
			spies = input("y/n: ")
			if spies == "y":
				print("How many? You have " + str(inv.Player1Spies) + " Spies.")
				snumber = int(input("Answer: "))

				if snumber > inv.Player1Spies:
					print("You don't have that many Heroes!")
					asks = True	

				if snumber <= inv.Player1Spies:
					userspies = snumber
					inv.Player1Spies -= snumber
					print("You are going to use " + str(userspies) + " Spy(s)")
					print("You have " + str(inv.Player1Spies) + " spies left.")
					asks = False

				else:
					asks = True

			else:
				userspies = 0
				asks = False	
				

		if inv.Player1Spies == 0:
			userspies = 0
			asks = False


	#Calculate user's power level!
	#Soliders + (Soliders * (Number of heroes * .10)) == p1power
	#p1power - (Soldiers * (Number of ai spies * .10)) == totalp1power

	print()
	print("Now calculating army power...")
	print()

	heropercent = userheroes * .10
	heromult =  usersoldiers * heropercent
	p1power = usersoldiers + heromult 
	
	spypercent = aispies * .10
	spymult = usersoldiers * spypercent
	
	totaluserpower = p1power - spymult
	totaluserpower = round(totaluserpower)

	userlandbonus = userland * 10


	print("Since you reside on " + str(userland) + " land(s), you are entitled to a +"+ str(userlandbonus) + " soldier bonus!")

	totaluserpower = totaluserpower + userlandbonus
	print("Your total power: " + str(totaluserpower))
	print()


	#Calculate ai's power level
	#Soldiers + (Soldiers * (Number of heroes * .10)) == aipowers
	#aipower - (Soldiers * Number of p1 spies * .10)) == totalaipower

	aihpercent = aiheroes * .10
	aihmult = aisoldiers * aihpercent
	aipower = aisoldiers + aihmult

	aispypercent = userspies * .10
	aispymult = aisoldiers * aispypercent

	totalaipower = aipower - aispymult
	totalaipower = round(totalaipower)

	ailandbonus = ailand * 10


	print("Since the enemy resides on " + str(ailand) + " land(s), they are entitled to a +"+ str(ailandbonus) + " soldier bonus!" )

	totalaipower = totalaipower + ailandbonus

	print("Your enemy's total power: " + str(totalaipower))

	print()
	input("Press [Enter] to start the war!")

	# START WAR

	print()
	userroll = random.randint(1,12) * 2
	enemyroll = random.randint(1,12) * 2

	userluck = userroll/100
	enemyluck = enemyroll/100

	print("You rolled a " + str(userroll) + " out of 24.")
	print("Your luck for the war: +" + str(userluck) + "%")
	print("The enemy rolled a " + str(enemyroll) + " out of 24.")
	print("Your enemy's luck for the war: +" + str(enemyluck) + "%")
	print()
	time.sleep(2)
	print("Your army prepares its cavalry while the enemy strings their bows!")
	time.sleep(1)
	print("Your archers wait for the signal... and attack!")
	time.sleep(1)
	print("The enemy's knights and your knights square off! You hear the steel swords clash....")
	time.sleep(1)
	print("Arrows flood the sky!")
	time.sleep(1)
	print("The dust settles! The victor steps out of the dust...")

		
	totaluserluck = totaluserpower * userluck
	totaluserluckfinal = totaluserluck + totaluserpower

	totalailuck = totalaipower * enemyluck
	totalailuckfinal = totalaipower + totalailuck


	totaluserpower = totaluserpower + totaluserluckfinal
	totaluserpower = round(totaluserpower)

	totalaipower = totalaipower + totalailuckfinal
	totalaipower = round(totalaipower)

	if totaluserpower > totalaipower:
		print("You win!")
		print("Your army had: " + str(totaluserpower) + ". While the enemy had: " + str(totalaipower))
		inv.Player1Land += 1

		if invade == 2:
			inv.Player2Lost = True

		if invade == 3:
			inv.Player3Lost = True

		if invade == 4:
			inv.Player4Lost = True

		if invade == 5:
			inv.Player5Lost = True


	if totaluserpower < totalaipower:
		print("You lost!")
		print("Your army had: " + str(totaluserpower) + ". While the enemy had: " + str(totalaipower))
		inv.Player1Lost = True

		if invade == 2:
			inv.Player2Land +=1

		if invade == 3:
			inv.Player3Land +=1

		if invade == 4:
			inv.Player4Land +=1

		if invade == 5:
			inv.Player5Land +=1

	if totaluserpower == totalaipower:
		print("It's a tie!")
		print("Your army had: " + str(totaluserpower) + ". While the enemy had: " + str(totalaipower))
		print("Nobody wins nor loses! Turn skipped!")



def Attacked(ai):
	# This is when the AI wants to declare war on you!

	if ai == 2:
		War(invade=2)


	if ai == 3:
		War(invade=3)


	if ai == 4:
		War(invade=4)

	
	if ai == 5:
		War(invade=5)
	