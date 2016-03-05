import random
score = 0
#answer with yes or no
response = raw_input("Your score is " + str(score) + ". Do you want more points? ") 

while response == "yes":
	points = random.uniform(0.0,3.0)
	score = score + points
	#need this condition because if score is >9, cannot show this message
	#essentially first comparing the new score with 9 to determine to show below message or not
	if score < 9: 
		response = raw_input("Your score is " + str(score) + ". Do you want more points? ")
	elif score == 9:
		print("Your score is " + str(score) + ". You win!")
		exit() #won't have the infinite loop
	else:
		print("Your score is " + str(score) + ". Since it is over 9, you lose!")
		exit() #won't have the infinite loop

if response != "yes": #no
	if score == 9:
		print("Your score is " + str(score) + ". You win!")
	elif score < 9:
		print("Your score is " + str(score) + ". Not bad, at least you didn\'t go over 9!")
	#don't need "if score > 9:" because as soon as score is > 9, the "You lose" message 
	#will show and the program will end. Will then never get to this part. 