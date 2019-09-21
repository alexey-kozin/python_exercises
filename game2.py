import pyfiglet
from utilites import bc , input_from_array
import randompy

def print_g2_banner():
	print(bc.OKBLUE)
	print(pyfiglet.figlet_format("Guess Game"))
	print(bc.ENDC)

def generate_number( difficulty ):
	return randompy.integer( 0, int(difficulty))

def compare_results( secret_number , user_sel ):

	if secret_number == int( user_sel ):
		print( " Secret number : %d , your number %s . You win!" % ( secret_number , user_sel ) )
	else:
		print( " Secret number : %d , your number %s . Computer win :(" % ( secret_number , user_sel ) )

def g2():

	base = 0

	choise_array = []
	user_prompt_string_pattern ="Please enter number between "

	print_g2_banner()

	while True:
		difficulty = input_from_array( "Please enter difficulty level 1 - 5 , Q for quit : ", [ "1" , "2" , "3" , "4" , "5"  , "Q"] )
		if "Q" == difficulty :
			return
		else:
			break


	for i in range( int(difficulty)+1 ):
		choise_array.append( str(i) )
	choise_array.append("Q")


	user_prompt = user_prompt_string_pattern+choise_array[0]+" and "+choise_array[len(choise_array)-2]+" , Q for quit : "
	while True:
		secret_number = generate_number(difficulty)
		user_sel = input_from_array( user_prompt , choise_array )
		if "Q" == user_sel :
			return
		else:
			compare_results( secret_number , user_sel )

	print("===============END OF GAME===============")




