import pyfiglet
from utilites import bc , input_from_array
import randompy
import time
import re

def print_g1_banner():
	print(bc.GREEN36)
	print(pyfiglet.figlet_format("Memory Game"))
	print(bc.ENDC)


def generate_seuence( difficulty ):
	arr = []
	for i in range( int(difficulty) ):
		arr.append( randompy.integer( 1 , 101 ) )
	return arr

def compare_seuences( secret_sequence , user_input ):
	#secret_sequence - array
	#user_input - sring
	try:
		 user_sequence = [int(i) for i in user_input.split(" ")]
	except Exception as e:
		print("Incorrect user input")
		return
	if secret_sequence == user_sequence:
		print( "You win!:)")
	else:
		print("You lost!:(")

def g1():

	print_g1_banner()

	while True:
		difficulty = input_from_array( "Please enter difficulty level 1 - 5 , Q for quit : ", [ "1" , "2" , "3" , "4" , "5"  , "Q"] )
		if "Q" == difficulty :
			return
		else:
			break

	while True:
		user_input = ""
		secret_sequence = generate_seuence(difficulty)
		for i in secret_sequence :
			print( i, end = " ")
		time.sleep( 0.7 )
		print("", end="\r")

		user_input = input( "Please repeat sequence , Q for quit : ")
		if "Q" == user_input :
			return
		else:
			compare_seuences( secret_sequence , re.sub('\s+', ' ', user_input).strip()  )


	print("===============END OF GAME===============")

