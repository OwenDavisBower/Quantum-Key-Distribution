import random

# Settings
numTries = 300
eavesdropper = True
showLists = False
showStats = True

# Stats
sameScheme = 0
sameBit = 0
sameBitSameScheme = 0

schemes = ['H/V', 'A/D']

alice = []
bob = []

aSchemesStr = ''
bSchemesStr = ''

aBitsStr = ''
bBitsStr = ''

for i in range(numTries):
	# Generate random scheme and bit for Alice
	aScheme = random.choice(schemes)
	aBit = random.getrandbits(1)
	# Generate random scheme for Bob
	bScheme = random.choice(schemes)

	# If Bob chooses the same scheme as Alice, Bob's bit is the same as Alice's.
	if aScheme == bScheme:
		# Keep track of how many times we get the same scheme
		if showStats:
			sameScheme += 1

		if (eavesdropper & (random.random() < 0.5)):
			bBit = random.getrandbits(1)
		else:
			bBit = aBit

		if showStats & (aBit == bBit):
			sameBitSameScheme += 1
	else:
		# Otherwise, Bob gets a random bit.
		bBit = random.getrandbits(1)

	if showStats & (aBit == bBit):
		sameBit += 1

	alice.append((aScheme, aBit))
	bob.append((bScheme, bBit))

	if showLists:
		aSchemesStr += '|' + aScheme
		bSchemesStr += '|' + bScheme

		aBitsStr += "| " + str(aBit) + " "
		bBitsStr += "| " + str(bBit) + " "



# print(alice)
# print(bob)

if showLists:
	print("\nAlice: ")
	print(aSchemesStr)
	print(aBitsStr)
	print("\nBob: ")
	print(bSchemesStr)
	print(bBitsStr)
	print ("\n")

if showStats:
	print("Same Scheme: " + str(round(sameScheme / numTries * 100, 2)) + "%")
	print("Same Bit: " + str(round(sameBit / numTries * 100, 2)) + "%")
	print("Same Bit for Same Scheme: " + str(round(sameBitSameScheme / sameScheme * 100, 2)) + "%")

print("\n")
