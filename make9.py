import random
score = 0
response = raw_input("Your score is " + str(score) + ". Do you want more points? ") #answer with yes or no

while response == "yes":
	points = random.uniform(0.0,3.0)
	score = score + points
	response = raw_input("Your score is " + str(score) + ". Do you want more points? ")

if score == 9:
	print("Your score is " + str(score) + ". You win!")
elif score < 9:
	print("Your score is " + str(score) + ". Not bad, at least you didn\'t go over 9!")
elif score > 9:
	print("Your score is " + str(score) + ". You lose!")
	

#Planning:
#score = 0
#loop pick number (random) 
# Your score is new random number + previous number(score). Do you want more points? answer with yes or no
#when yes, then repeat the two previous hashtags. - this is in a loop

#when no, then say whether you win if = 9 and you lose when greater than 9 and not bad if it is less than 9

	






