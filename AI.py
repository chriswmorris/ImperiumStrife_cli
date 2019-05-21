#!/usr/bin/env python3

import time
import random
import Inventory as inv
import UserMoves as moves


# This is where the AI's logic is stored.


def EatFood(aiplayer):

	percent = random.randint(5,15)/100

	if aiplayer == 2:
		eatamount = inv.Player2Soldiers * percent
		eaten = round(eatamount)
		inv.Player2Food -= eaten
		
	if aiplayer == 3:
		eatamount = inv.Player3Soldiers * percent
		eaten = round(eatamount)
		inv.Player3Food -= eaten

	if aiplayer == 4:
		eatamount = inv.Player4Soldiers * percent
		eaten = round(eatamount)
		inv.Player4Food -= eaten

	if aiplayer == 5:
		eatamount = inv.Player5Soldiers * percent
		eaten = round(eatamount)
		inv.Player5Food -= eaten
	

	print("The AI's soldiers ate " + str(eaten) + " food this turn")



def FoodCheck(aiplayer):

	if aiplayer == 2:
		soldierleaves = inv.Player2Soldiers - inv.Player2Food
		if inv.Player2Soldiers > inv.Player2Food:
			inv.Player2Soldiers -=soldierleaves
			print(str(soldierleaves) + " left their army because they didn't have enough food!")

	if aiplayer == 3:
		soldierleaves = inv.Player3Soldiers - inv.Player3Food
		if inv.Player3Soldiers > inv.Player3Food:
			inv.Player3Soldiers -=soldierleaves
			print(str(soldierleaves) + " left their army because they didn't have enough food!")

		
	if aiplayer == 4:
		soldierleaves = inv.Player4Soldiers - inv.Player4Food
		if inv.Player4Soldiers > inv.Player4Food:
			inv.Player4Soldiers -=soldierleaves
			print(str(soldierleaves) + " left their army because they didn't have enough food!")


	if aiplayer == 5:
		soldierleaves = inv.Player5Soldiers - inv.Player5Food
		if inv.Player5Soldiers > inv.Player5Food:
			inv.Player5Soldiers -=soldierleaves
			print(str(soldierleaves) + " left their army because they didn't have enough food!")



def StartWar(player):
	
	# This is when the AI chooses to invade to start a war

	battlelist = []


	if inv.Player1Lost == False:
		battlelist.append(1)

	if inv.Player2Lost == False:
		battlelist.append(2)

	if inv.Player3Lost == False:
		battlelist.append(3)

	if inv.Player4Lost == False:
		battlelist.append(4)

	if inv.Player5Lost == False:
		battlelist.append(5)

	if player == 1:
		battlelist.remove(1)

	if player == 2:
		battlelist.remove(2)

	if player == 3:
		battlelist.remove(3)

	if player == 4:
		battlelist.remove(4)

	if player == 5:
		battlelist.remove(5)


	invade = random.choice(battlelist)		

	if invade == 1:
		print("Initiating War with you!")
		moves.Attacked(ai=player)
			
	if invade == 2:
		print("Initiating War with the Frugalis Republic!")
		AIWar(invadeplayer = 2, invader=player)
			

	if invade == 3:
		print("Initiating War with the Dutchy of Alea!")
		AIWar(invadeplayer = 3, invader=player)
				

	if invade == 4:
		print("Initiating War with Imperium Malum!")
		AIWar(invadeplayer = 4, invader=player)
				
	if invade == 5:
		print("Initiating War with Imbecile Kingdom!")
		AIWar(invadeplayer = 5, invader=player)
			


def AIWar(invadeplayer, invader):
	# This is when the AI has chosen an AI to invade
	# If they chose to invade Player 1, they'll call "Attacked()" in UserMoves.py


	if invader == 2:
		invadersoldiers = inv.Player2Soldiers 
		invaderheroes = inv.Player2Heroes
		invaderspies = inv.Player2Spies
		invaderland = inv.Player2Land
		invaderloss = inv.Player2Lost

	if invader == 3:
		invadersoldiers = inv.Player3Soldiers
		invaderheroes = inv.Player3Heroes
		invaderspies = inv.Player3Spies
		invaderland = inv.Player3Land
		invaderloss = inv.Player3Lost

	if invader == 4:
		invadersoldiers = inv.Player4Soldiers
		invaderheroes = inv.Player4Heroes
		invaderspies = inv.Player4Spies
		invaderland = inv.Player4Land
		invaderloss = inv.Player4Lost
	
	if invader == 5:
		invadersoldiers = inv.Player5Soldiers
		invaderheroes = inv.Player5Heroes
		invaderspies = inv.Player5Spies
		invaderland = inv.Player5Land
		invaderloss = inv.Player5Lost

	if invadeplayer == 1:
		moves.Attacked()

	if invadeplayer == 2:
		enemysoldiers = inv.Player2Soldiers 
		enemyheroes = inv.Player2Heroes
		enemyspies = inv.Player2Spies
		enemyland = inv.Player2Land
		enemyloss = inv.Player2Lost

	if invadeplayer == 3:
		enemysoldiers = inv.Player3Soldiers
		enemyheroes = inv.Player3Heroes
		enemyspies = inv.Player3Spies
		enemyland = inv.Player3Land
		enemyloss = inv.Player3Lost

	if invadeplayer == 4:
		enemysoldiers = inv.Player4Soldiers
		enemyheroes = inv.Player4Heroes
		enemyspies = inv.Player4Spies
		enemyland = inv.Player4Land
		enemyloss = inv.Player4Lost
	
	if invadeplayer == 5:
		enemysoldiers = inv.Player5Soldiers
		enemyheroes = inv.Player5Heroes
		enemyspies = inv.Player5Spies
		enemyland = inv.Player5Land
		enemyloss = inv.Player5Lost



	#Calculate invader power level!
	#Soliders + (Soliders * (Number of heroes * .10)) == p1power
	#p1power - (Soldiers * (Number of ai spies * .10)) == totalp1power

	print()
	print("Now calculating army power...")
	print()

	heropercent = invaderheroes * .10
	heromult =  invadersoldiers * heropercent
	p1power = invadersoldiers + heromult 
	
	spypercent = enemyspies * .10
	spymult = invadersoldiers * spypercent
	
	totalinvaderpower = p1power - spymult
	totalinvaderpower = round(totalinvaderpower)

	invaderlandbonus = invaderland * 10

	print("Since they reside on " + str(invaderland) + " land(s), they are entitled to a +"+ str(invaderlandbonus) + " soldier bonus!")

	totalinvaderpower = totalinvaderpower + invaderlandbonus
	print("Their total power: " + str(totalinvaderpower))
	print()


	#Calculate enemy power level

	enemyhpercent = enemyheroes * .10
	enemyhmult = enemysoldiers * enemyhpercent
	enemypower = enemysoldiers + enemyhmult

	enemyspypercent = invaderspies * .10
	enemyspymult = enemysoldiers * enemyspypercent

	totalenemypower = enemypower - enemyspymult
	totalenemypower = round(totalenemypower)

	enemylandbonus = enemyland * 10

	print("Since the enemy resides on " + str(enemyland) + " land(s), they are entitled to a +"+ str(enemylandbonus) + " soldier bonus!" )

	totalenemypower = totalenemypower + enemylandbonus

	print("Their enemy's total power: " + str(totalenemypower))

	print()
	input("Press [Enter] to start their war!")

	###########START AI WAR

	print()
	invaderroll = random.randint(1,12) * 2
	enemyroll = random.randint(1,12) * 2

	invaderluck = invaderroll/100
	enemyluck = enemyroll/100

	print("They rolled a " + str(invaderroll) + " out of 24.")
	print("Their luck for the war: +" + str(invaderluck) + "%")
	print("Their enemy rolled a " + str(enemyroll) + " out of 24.")
	print("Their enemy's luck for the war: +" + str(enemyluck) + "%")
	print()
	time.sleep(2)
	

	totalinvaderluck = totalinvaderpower * invaderluck
	totalinvaderpower =  totalinvaderpower + totalinvaderluck
	totalinvaderpower = round(totalinvaderpower)

	totalenemyluck = totalenemypower * enemyluck
	totalenemypower = totalenemypower + totalenemyluck
	totalenemypower = round(totalenemypower)


	############ END OF WAR

	if totalinvaderpower > totalenemypower:
		print("They win!")
		print("Their army had: " + str(totalinvaderpower) + ". While their enemy had: " + str(totalenemypower))

		if invadeplayer == 2:
			inv.Player2Lost = True

		if invadeplayer == 3:
			inv.Player3Lost = True

		if invadeplayer == 4:
			inv.Player4Lost = True

		if invadeplayer == 5:
			inv.Player5Lost = True

		if invader == 2:
			inv.Player2Land +=1

		if invader == 3:
			inv.Player3Land +=1

		if invader == 4:
			inv.Player4Land +=1

		if invader == 5:
			inv.Player5Land =+1

	if totalinvaderpower < totalenemypower:
		print("They lost!")
		print("Their army had: " + str(totalinvaderpower) + ". While their enemy had: " + str(totalenemypower))

		if invader == 2:
			inv.Player2Lost = True

		if invader == 3:
			inv.Player3Lost = True

		if invader == 4:
			inv.Player4Lost = True

		if invader == 5:
			inv.Player5Lost = True

		if invadeplayer == 2:
			inv.Player2Land +=1

		if invadeplayer == 3:
			inv.Player3Land +=1

		if invadeplayer == 4:
			inv.Player4Land +=1

		if invadeplayer == 5:
			inv.Player5Land =+1


	if totalinvaderpower == totalenemypower:
		print("It's a tie!")
		print("Their army had: " + str(totalinvaderpower) + ". While their enemy had: " + str(totalenemypower))
		print("Nobody wins nor loses! Turn skipped!")
	

#######################################################

#AI CHOICES

# 2: Frugalis Republic (Likes to stockpile)
# 3: Dutchy of Alea (Likes to gamble)
# 4: Imperium Malum (Aggressive)
# 5: Imbecile Kingdom (Random)



def P2Move():	
	# 2: Frugalis Republic (Likes to stockpile)

	# Invade!(1)
	# Choose a card (2)
	# Obtain 30 Soldiers(3,4,5)
	# Obtain 30 Food (6,7,8)
	# Gamble at the Pub (9,10)

	roll = random.randint(1,10)

	if roll == 1:
		print("Invade!")
		StartWar(player=2)

	if roll == 2:
		print("The Frugalis Republic decided to draw a card... ")
		card = random.randint(1,15)
		
		if card == 1:
			inv.Player2Spies += 1
			print("They got a Spy!")
			print("They now have " + str(inv.Player2Spies) + " Spies.")

		if card == 2:
			inv.Player2Spies += 1
			print("They got a Spy!")
			print("They now have " + str(inv.Player2Spies) + " Spies.")

		if card == 3:
			inv.Player2Heroes += 1
			print("They got a Hero!")
			print("They now have " + str(inv.Player2Heroes) + " Heroes.")

		if card == 4:
			inv.Player2Heroes += 1
			print("They got a Hero!")
			print("They now have " + str(inv.Player2Heroes) + " Heroes.")

		if card == 5:
			inv.Player2Soldiers += 50
			print("They saved a local village from Bandits. 50 men from the village take up their cause!")
			print("They got 50 Soldiers!")

		if card == 6:
			inv.Player2Food += 50
			print("A local village thanks them for saving them from Raiders. They give Tthem food.")
			print("They got 50 Food!")

		if card == 7:
			inv.Player2Soldiers += 100
			print("Soldiers from an enemy army defect to their side!")
			print("They got 100 Soldiers!")

		if card == 8:
			inv.Player2Food += 100
			print("Their loyal subjects have bountiful harvest!")
			print("They got 100 Food!")

		if card == 9:
			plague = inv.Player2Soldiers * .20
			ploss = round(plague)
			inv.Player2Soldiers -= ploss
			print("Some soldiers in their army get the plague.")
			print(str(ploss) + " soldiers die from it.")
			
		if card == 10:
			locusts = inv.Player2Food * .20
			lloss = round(locusts)
			inv.Player2Food -= lloss
			print("Some locusts eat their subjects' crops!")
			print("They lose " + str(lloss) + " food.")

		if card == 11:
			badplague = inv.Player2Soldiers * .60
			badploss = round(badplague)
			inv.Player2Soldiers -= badploss
			print("A bad plague runs rampant in their army's camp.")
			print(str(badploss) + " soldiers die from it.")

		if card == 12:
			badlocusts = inv.Player2Food * .60
			badlloss = round(badlocusts)
			inv.Player2Food -= badlloss
			print("A horde of locusts eat their subjects' crops!")
			print("They lose " + str(badlloss) + " food.")

		if card == 13:
			inv.Player2Food +=30
			inv.Player2Soldiers -=30
			print("30 soldiers decide to quit and move to a farm.")
			print("They gain 30 food but lose 30 soldiers")

		if card == 14:
			inv.Player2Food -= 30
			inv.Player2Soldiers += 30
			print("They host a feast for their army. Some farmers join just cause they want to join the feast!")
			print("They lose 30 food but gain 30 soldiers.")

		if card == 15:
			inv.Player2Heroes += 1
			inv.Player2Spies += 1
			print("They got a hero and a spy!!!")

	if roll in range(3,6):
		inv.Player2Soldiers += 30
		print()
		print("Frugalis Republic just recuited 30 Soldiers! (+30 Soldiers)")
		print("They now have " + str(inv.Player2Soldiers) +  " Soldiers!")
		print()

	if roll in range(6,9):
		inv.Player2Food += 30
		print()
		print("Frugalis Republic just farmed 30 Food! (+30 Food)")
		print("They now have " + str(inv.Player2Food) +  " Food!")
		print()

	if roll in range(9,11):
		#Basically the user gets 5-35 food and 5-35 soldiers
		randfood = random.randint(5,35)
		randsoldiers = random.randint(5,35)
		totals = randfood + randsoldiers
		print()
		print("A Lord from the Frugalis Republic went to a pub and try their hand at a game of dice...")
		print("At the table sits prominent Lords and Barons from far off lands.")
		print()
		if totals == 10:
			print("They gambled and lost big to Lord Al Kaholic!")
			print("They got " + str(randfood) + " food and " + str(randsoldiers) + " soliders.")

		if 11 <= totals <= 20:
			print("They gambled and lost to Lord Jussfar Ted.")
			print("They got " + str(randfood) + " food and " + str(randsoldiers) + " soliders.")

		if 21 <= totals <= 30:
			print("They gambled and lost when they diced agianst Lord Ben Dover.")
			print("They got " + str(randfood) + " food and " + str(randsoldiers) + " soliders.")

		if 31 <= totals <= 40:
			print("They did okay when they diced agianst Baron Neu Trall.")
			print("They got " + str(randfood) + " food and " + str(randsoldiers) + " soliders.")

		if 41 <= totals <= 50:
			print("They did well when They diced agianst Baron Pierre Pants.")
			print("They got " + str(randfood) + " food and " + str(randsoldiers) + " soliders.")

		if 51 <= totals <= 59:
			print("They did very well at the tables! Lord Moe Ronn could not keep up!")
			print("They got " + str(randfood) + " food and " + str(randsoldiers) + " soliders.")

		if 60 <= totals <= 69:
			print("They did excellent at the tables! Lord Suhm L. Ebuht said he has never seen such skill!")
			print("They got " + str(randfood) + " food and " + str(randsoldiers) + " soliders.")

		if totals == 70:
			print("DANG!! They DID EXTREMELY WELL! Everyone in the pub cheers and they earned a plaque with Theyr name on it!")
			print("They got " + str(randfood) + " food and " + str(randsoldiers) + " soliders.")

		inv.Player2Food += randfood
		inv.Player2Soldiers += randsoldiers
		print()



def P3Move():
	# 3: Dutchy of Alea (Likes to gamble)

	# Invade!(1)
	# Choose a card (2,3,4)
	# Obtain 30 Soldiers(5)
	# Obtain 30 Food (6,7)
	# Gamble at the Pub (8,9,10)

	roll = random.randint(1,10)

	if roll == 1:
		print("Invade!")
		StartWar(player=3)

	if roll in range(2,5):
		print("The Dutchy of Alea decided to draw a card... ")
		card = random.randint(1,15)
		
		if card == 1:
			inv.Player3Spies += 1
			print("They got a Spy!")
			print("They now have " + str(inv.Player3Spies) + " Spies.")

		if card == 2:
			inv.Player3Spies += 1
			print("They got a Spy!")
			print("They now have " + str(inv.Player3Spies) + " Spies.")

		if card == 3:
			inv.Player3Heroes += 1
			print("They got a Hero!")
			print("They now have " + str(inv.Player3Heroes) + " Heroes.")

		if card == 4:
			inv.Player3Heroes += 1
			print("They got a Hero!")
			print("They now have " + str(inv.Player3Heroes) + " Heroes.")

		if card == 5:
			inv.Player3Soldiers += 50
			print("They saved a local village from Bandits. 50 men from the village take up their cause!")
			print("They got 50 Soldiers!")

		if card == 6:
			inv.Player3Food += 50
			print("A local village thanks them for saving them from Raiders. They give Tthem food.")
			print("They got 50 Food!")

		if card == 7:
			inv.Player3Soldiers += 100
			print("Soldiers from an enemy army defect to their side!")
			print("They got 100 Soldiers!")

		if card == 8:
			inv.Player3Food += 100
			print("Their loyal subjects have bountiful harvest!")
			print("They got 100 Food!")

		if card == 9:
			plague = inv.Player3Soldiers * .20
			ploss = round(plague)
			inv.Player3Soldiers -= ploss
			print("Some soldiers in their army get the plague.")
			print(str(ploss) + " soldiers die from it.")
			
		if card == 10:
			locusts = inv.Player3Food * .20
			lloss = round(locusts)
			inv.Player3Food -= lloss
			print("Some locusts eat their subjects' crops!")
			print("They lose " + str(lloss) + " food.")

		if card == 11:
			badplague = inv.Player3Soldiers * .60
			badploss = round(badplague)
			inv.Player3Soldiers -= badploss
			print("A bad plague runs rampant in their army's camp.")
			print(str(badploss) + " soldiers die from it.")

		if card == 12:
			badlocusts = inv.Player3Food * .60
			badlloss = round(badlocusts)
			inv.Player3Food -= badlloss
			print("A horde of locusts eat their subjects' crops!")
			print("They lose " + str(badlloss) + " food.")

		if card == 13:
			inv.Player3Food +=30
			inv.Player3Soldiers -=30
			print("30 soldiers decide to quit and move to a farm.")
			print("They gain 30 food but lose 30 soldiers")

		if card == 14:
			inv.Player3Food -= 30
			inv.Player3Soldiers += 30
			print("They host a feast for their army. Some farmers join just cause they want to join the feast!")
			print("They lose 30 food but gain 30 soldiers.")

		if card == 15:
			inv.Player3Heroes += 1
			inv.Player3Spies += 1
			print("They got a hero and a spy!!!")

	if roll == 5:
		inv.Player3Soldiers += 30
		print()
		print("Dutchy of Alea just recuited 30 Soldiers! (+30 Soldiers)")
		print("They now have " + str(inv.Player3Soldiers) +  " Soldiers!")
		print()


	if roll in range(6,8):
		inv.Player3Food += 30
		print()
		print("Dutchy of Alea just farmed 30 Food! (+30 Food)")
		print("They now have " + str(inv.Player3Food) +  " Food!")
		print()

	if roll in range(8,11):
		#Basically the user gets 5-35 food and 5-35 soldiers
		randfood = random.randint(5,35)
		randsoldiers = random.randint(5,35)
		totals = randfood + randsoldiers
		print()
		print("A Lord from the Dutchy of Alea went to a pub and try their hand at a game of dice...")
		print("At the table sits prominent Lords and Barons from far off lands.")
		print()
		if totals == 10:
			print("They gambled and lost big to Lord Al Kaholic!")
			print("They got " + str(randfood) + " food and " + str(randsoldiers) + " soliders.")

		if 11 <= totals <= 20:
			print("They gambled and lost to Lord Jussfar Ted.")
			print("They got " + str(randfood) + " food and " + str(randsoldiers) + " soliders.")

		if 21 <= totals <= 30:
			print("They gambled and lost when they diced agianst Lord Ben Dover.")
			print("They got " + str(randfood) + " food and " + str(randsoldiers) + " soliders.")

		if 31 <= totals <= 40:
			print("They did okay when they diced agianst Baron Neu Trall.")
			print("They got " + str(randfood) + " food and " + str(randsoldiers) + " soliders.")

		if 41 <= totals <= 50:
			print("They did well when They diced agianst Baron Pierre Pants.")
			print("They got " + str(randfood) + " food and " + str(randsoldiers) + " soliders.")

		if 51 <= totals <= 59:
			print("They did very well at the tables! Lord Moe Ronn could not keep up!")
			print("They got " + str(randfood) + " food and " + str(randsoldiers) + " soliders.")

		if 60 <= totals <= 69:
			print("They did excellent at the tables! Lord Suhm L. Ebuht said he has never seen such skill!")
			print("They got " + str(randfood) + " food and " + str(randsoldiers) + " soliders.")

		if totals == 70:
			print("DANG!! They DID EXTREMELY WELL! Everyone in the pub cheers and they earned a plaque with Theyr name on it!")
			print("They got " + str(randfood) + " food and " + str(randsoldiers) + " soliders.")

		inv.Player3Food += randfood
		inv.Player3Soldiers += randsoldiers
		print()




def P4Move():
	# 4: Imperium Malum (Aggressive)

	# Invade!(1,2,3)
	# Choose a card (4)
	# Obtain 30 Soldiers(5,6)
	# Obtain 30 Food (7,8,9)
	# Gamble at the Pub (10)

	roll = random.randint(1,10)

	if roll in range(1,4):
		print("Invade!")
		StartWar(player=4)

	if roll == 4:
		print("The Imperium Malum decided to draw a card... ")
		card = random.randint(1,15)
		
		if card == 1:
			inv.Player4Spies += 1
			print("They got a Spy!")
			print("They now have " + str(inv.Player4Spies) + " Spies.")

		if card == 2:
			inv.Player4Spies += 1
			print("They got a Spy!")
			print("They now have " + str(inv.Player4Spies) + " Spies.")

		if card == 3:
			inv.Player4Heroes += 1
			print("They got a Hero!")
			print("They now have " + str(inv.Player4Heroes) + " Heroes.")

		if card == 4:
			inv.Player4Heroes += 1
			print("They got a Hero!")
			print("They now have " + str(inv.Player4Heroes) + " Heroes.")

		if card == 5:
			inv.Player4Soldiers += 50
			print("They saved a local village from Bandits. 50 men from the village take up their cause!")
			print("They got 50 Soldiers!")

		if card == 6:
			inv.Player4Food += 50
			print("A local village thanks them for saving them from Raiders. They give Tthem food.")
			print("They got 50 Food!")

		if card == 7:
			inv.Player4Soldiers += 100
			print("Soldiers from an enemy army defect to their side!")
			print("They got 100 Soldiers!")

		if card == 8:
			inv.Player4Food += 100
			print("Their loyal subjects have bountiful harvest!")
			print("They got 100 Food!")

		if card == 9:
			plague = inv.Player4Soldiers * .20
			ploss = round(plague)
			inv.Player4Soldiers -= ploss
			print("Some soldiers in their army get the plague.")
			print(str(ploss) + " soldiers die from it.")
			
		if card == 10:
			locusts = inv.Player4Food * .20
			lloss = round(locusts)
			inv.Player4Food -= lloss
			print("Some locusts eat their subjects' crops!")
			print("They lose " + str(lloss) + " food.")

		if card == 11:
			badplague = inv.Player4Soldiers * .60
			badploss = round(badplague)
			inv.Player4Soldiers -= badploss
			print("A bad plague runs rampant in their army's camp.")
			print(str(badploss) + " soldiers die from it.")

		if card == 12:
			badlocusts = inv.Player4Food * .60
			badlloss = round(badlocusts)
			inv.Player4Food -= badlloss
			print("A horde of locusts eat their subjects' crops!")
			print("They lose " + str(badlloss) + " food.")

		if card == 13:
			inv.Player4Food +=30
			inv.Player4Soldiers -=30
			print("30 soldiers decide to quit and move to a farm.")
			print("They gain 30 food but lose 30 soldiers")

		if card == 14:
			inv.Player4Food -= 30
			inv.Player4Soldiers += 30
			print("They host a feast for their army. Some farmers join just cause they want to join the feast!")
			print("They lose 30 food but gain 30 soldiers.")

		if card == 15:
			inv.Player4Heroes += 1
			inv.Player4Spies += 1
			print("They got a hero and a spy!!!")

	if roll in range(5,7):
		inv.Player4Soldiers += 30
		print()
		print("Imperium Malum just recuited 30 Soldiers! (+30 Soldiers)")
		print("They now have " + str(inv.Player4Soldiers) +  " Soldiers!")
		print()

	if roll in range(7,10):
		inv.Player4Food += 30
		print()
		print("Imperium Malum just farmed 30 Food! (+30 Food)")
		print("They now have " + str(inv.Player4Food) +  " Food!")
		print()

	if roll == 10:
		#Basically the user gets 5-35 food and 5-35 soldiers
		randfood = random.randint(5,35)
		randsoldiers = random.randint(5,35)
		totals = randfood + randsoldiers
		print()
		print("A Lord from the Imperium Malum went to a pub and try their hand at a game of dice...")
		print("At the table sits prominent Lords and Barons from far off lands.")
		print()
		if totals == 10:
			print("They gambled and lost big to Lord Al Kaholic!")
			print("They got " + str(randfood) + " food and " + str(randsoldiers) + " soliders.")

		if 11 <= totals <= 20:
			print("They gambled and lost to Lord Jussfar Ted.")
			print("They got " + str(randfood) + " food and " + str(randsoldiers) + " soliders.")

		if 21 <= totals <= 30:
			print("They gambled and lost when they diced agianst Lord Ben Dover.")
			print("They got " + str(randfood) + " food and " + str(randsoldiers) + " soliders.")

		if 31 <= totals <= 40:
			print("They did okay when they diced agianst Baron Neu Trall.")
			print("They got " + str(randfood) + " food and " + str(randsoldiers) + " soliders.")

		if 41 <= totals <= 50:
			print("They did well when They diced agianst Baron Pierre Pants.")
			print("They got " + str(randfood) + " food and " + str(randsoldiers) + " soliders.")

		if 51 <= totals <= 59:
			print("They did very well at the tables! Lord Moe Ronn could not keep up!")
			print("They got " + str(randfood) + " food and " + str(randsoldiers) + " soliders.")

		if 60 <= totals <= 69:
			print("They did excellent at the tables! Lord Suhm L. Ebuht said he has never seen such skill!")
			print("They got " + str(randfood) + " food and " + str(randsoldiers) + " soliders.")

		if totals == 70:
			print("DANG!! They DID EXTREMELY WELL! Everyone in the pub cheers and they earned a plaque with Theyr name on it!")
			print("They got " + str(randfood) + " food and " + str(randsoldiers) + " soliders.")

		inv.Player4Food += randfood
		inv.Player4Soldiers += randsoldiers
		print()




def P5Move():
	# 5: Imbecile Kingdom (Random)

	# Invade!(1,2)
	# Choose a card (3,4)
	# Obtain 30 Soldiers(5,6)
	# Obtain 30 Food (7,8)
	# Gamble at the Pub (9,10)
	roll = random.randint(1,10)

	if roll in range(1,3):
		print("Invade!")
		StartWar(player=5)

	if roll in range(3,5):
		print("The Imbecile Kingdom decided to draw a card... ")
		card = random.randint(1,15)
		
		if card == 1:
			inv.Player5Spies += 1
			print("They got a Spy!")
			print("They now have " + str(inv.Player5Spies) + " Spies.")

		if card == 2:
			inv.Player5Spies += 1
			print("They got a Spy!")
			print("They now have " + str(inv.Player5Spies) + " Spies.")

		if card == 3:
			inv.Player5Heroes += 1
			print("They got a Hero!")
			print("They now have " + str(inv.Player5Heroes) + " Heroes.")

		if card == 4:
			inv.Player5Heroes += 1
			print("They got a Hero!")
			print("They now have " + str(inv.Player5Heroes) + " Heroes.")

		if card == 5:
			inv.Player5Soldiers += 50
			print("They saved a local village from Bandits. 50 men from the village take up their cause!")
			print("They got 50 Soldiers!")

		if card == 6:
			inv.Player5Food += 50
			print("A local village thanks them for saving them from Raiders. They give Tthem food.")
			print("They got 50 Food!")

		if card == 7:
			inv.Player5Soldiers += 100
			print("Soldiers from an enemy army defect to their side!")
			print("They got 100 Soldiers!")

		if card == 8:
			inv.Player5Food += 100
			print("Their loyal subjects have bountiful harvest!")
			print("They got 100 Food!")

		if card == 9:
			plague = inv.Player5Soldiers * .20
			ploss = round(plague)
			inv.Player5Soldiers -= ploss
			print("Some soldiers in their army get the plague.")
			print(str(ploss) + " soldiers die from it.")
			
		if card == 10:
			locusts = inv.Player5Food * .20
			lloss = round(locusts)
			inv.Player5Food -= lloss
			print("Some locusts eat their subjects' crops!")
			print("They lose " + str(lloss) + " food.")

		if card == 11:
			badplague = inv.Player5Soldiers * .60
			badploss = round(badplague)
			inv.Player5Soldiers -= badploss
			print("A bad plague runs rampant in their army's camp.")
			print(str(badploss) + " soldiers die from it.")

		if card == 12:
			badlocusts = inv.Player5Food * .60
			badlloss = round(badlocusts)
			inv.Player5Food -= badlloss
			print("A horde of locusts eat their subjects' crops!")
			print("They lose " + str(badlloss) + " food.")

		if card == 13:
			inv.Player5Food +=30
			inv.Player5Soldiers -=30
			print("30 soldiers decide to quit and move to a farm.")
			print("They gain 30 food but lose 30 soldiers")

		if card == 14:
			inv.Player5Food -= 30
			inv.Player5Soldiers += 30
			print("They host a feast for their army. Some farmers join just cause they want to join the feast!")
			print("They lose 30 food but gain 30 soldiers.")

		if card == 15:
			inv.Player5Heroes += 1
			inv.Player5Spies += 1
			print("They got a hero and a spy!!!")

	if roll in range(5,7):
		inv.Player5Soldiers += 30
		print()
		print("Imbecile Kingdom just recuited 30 Soldiers! (+30 Soldiers)")
		print("They now have " + str(inv.Player5Soldiers) +  " Soldiers!")
		print()

	if roll in range(7,9):
		inv.Player5Food += 30
		print()
		print("Imbecile Kingdom just farmed 30 Food! (+30 Food)")
		print("They now have " + str(inv.Player5Food) +  " Food!")
		print()

	if roll in range(9,11):
		#Basically the user gets 5-35 food and 5-35 soldiers
		randfood = random.randint(5,35)
		randsoldiers = random.randint(5,35)
		totals = randfood + randsoldiers
		print()
		print("A Lord from the Imbecile Kingdom went to a pub and try their hand at a game of dice...")
		print("At the table sits prominent Lords and Barons from far off lands.")
		print()
		if totals == 10:
			print("They gambled and lost big to Lord Al Kaholic!")
			print("They got " + str(randfood) + " food and " + str(randsoldiers) + " soliders.")

		if 11 <= totals <= 20:
			print("They gambled and lost to Lord Jussfar Ted.")
			print("They got " + str(randfood) + " food and " + str(randsoldiers) + " soliders.")

		if 21 <= totals <= 30:
			print("They gambled and lost when they diced agianst Lord Ben Dover.")
			print("They got " + str(randfood) + " food and " + str(randsoldiers) + " soliders.")

		if 31 <= totals <= 40:
			print("They did okay when they diced agianst Baron Neu Trall.")
			print("They got " + str(randfood) + " food and " + str(randsoldiers) + " soliders.")

		if 41 <= totals <= 50:
			print("They did well when They diced agianst Baron Pierre Pants.")
			print("They got " + str(randfood) + " food and " + str(randsoldiers) + " soliders.")

		if 51 <= totals <= 59:
			print("They did very well at the tables! Lord Moe Ronn could not keep up!")
			print("They got " + str(randfood) + " food and " + str(randsoldiers) + " soliders.")

		if 60 <= totals <= 69:
			print("They did excellent at the tables! Lord Suhm L. Ebuht said he has never seen such skill!")
			print("They got " + str(randfood) + " food and " + str(randsoldiers) + " soliders.")

		if totals == 70:
			print("DANG!! They DID EXTREMELY WELL! Everyone in the pub cheers and they earned a plaque with Theyr name on it!")
			print("They got " + str(randfood) + " food and " + str(randsoldiers) + " soliders.")

		inv.Player5Food += randfood
		inv.Player5Soldiers += randsoldiers
		print()