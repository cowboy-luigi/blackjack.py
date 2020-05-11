
import random

suits = ['♠', '♥', '♦', '♣']
faces = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']

roundsWon = 0
roundsLost = 0

player = []
dealer = []

def checkforaces(hand):
	value = 0
	for i in hand:
		if i == '♠A' or i == '♥A' or i == '♦A' or i == '♣A':
			value += 10
	return value

def getcardvalue(card):
	s = list(card)
	s.pop(0)
	if s[0] == '1':
		value = 10
	elif s[0] == 'A':
		value = 11
	elif s[0] == 'J' or s[0] == 'Q' or s[0] == 'K':
		value = 10
	else:
		value = int(s[0])
	
	return value

def evaluatecards(hand):
	total = 0
	j = 0
	for i in hand:
		total += getcardvalue(hand[j])
		j += 1
	return total

def displaycards():
	print("Player cards:")
	for i in player:
		print(i + ', ', end = '')
	print("\nDealer cards:")
	for i in dealer:
		print(i + ', ', end = '')
	print()

def makedeck(num):
	deck = []
	x = 1
	while x <= num:
		x += 1
		for s in suits:
			for f in faces:
				deck.append(s+f)
	return deck 

print("       /\\")
print("     .'  `.")
print("    '      `.")
print(" .'          `.")
print("{              }")
print(" ~-...-||-...-~")
print("       ||")
print("      '--`")

print("Blackjack.py")

print("Using standard instance of 8 decks: Player v. House")
print("===================================================\n\n")

cards = makedeck(1)
shuffler = random.randint(1,100)

for i in range(0,shuffler):
	random.shuffle(cards)
	
roundnum = 1

while len(cards) > 6:
	choiceHS = ''

	roundover = False
	
	playertotal = 0
	dealertotal = 0
	
	print("Round "+ str(roundnum) + ":\n")

	player.append(cards.pop())
	dealer.append(cards.pop())

	while roundover == False:
		
		roundover = False
		
		player.append(cards.pop())
		if evaluatecards(dealer) < 17:
			dealer.append(cards.pop())

		displaycards()
		
		print("\nPlayer total: " + str(evaluatecards(player)))
		
		if evaluatecards(player) > 21:
			roundover = True
			print("Bust!")
		elif evaluatecards(player) == 21:
			roundover = True
			print("Blackjack!")
		
		playertotal = evaluatecards(player)
		
		print("Dealer total: " + str(evaluatecards(dealer)))
		
		if evaluatecards(dealer) > 21:
			roundover = True
			print("Bust!")
		elif evaluatecards(dealer) == 21:
			roundover = True
			print("Blackjack!")
			
		dealertotal = evaluatecards(dealer)	
			
		if roundover == False:
			choiceHS = input("\nHit or Stand? (h/s)\n")
			
			if choiceHS == 's':
				print("\nPlayer total: " + str(playertotal))
				while evaluatecards(dealer) < 17:
					dealer.append(cards.pop())
				
				dealertotal = evaluatecards(dealer)
				
				print("Dealer total: " + str(dealertotal))
				
				roundover = True
				
		
	
	if playertotal == dealertotal:
		print("\nTie!")
	elif playertotal == 21:
		print("\nYou win!")
		roundsWon += 1
	elif dealertotal == 21:
		print("\nYou lose...")
		roundsLost += 1
	elif playertotal > 21:
		print("\nYou lose...")
		roundsLost += 1
	elif dealertotal > 21:
		print("\nYou win!")
		roundsWon += 1
	elif playertotal > dealertotal:
		print("\nYou win!")
		roundsWon += 1
	else:
		print("\nYou lose...")
		roundsLost += 1
	print("===================")
	
	roundnum += 1
	
	dealer = []
	player = []
	
	
	
print("No more cards")
