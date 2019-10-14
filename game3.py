import pyfiglet
from utilites import bc , input_from_array
import randompy

def print_g3_banner():
	print(bc.ZIAN)
	print(pyfiglet.figlet_format("Currency Roulette"))
	print(bc.ENDC)

def request_currency_data():
	#url = 'https://api.exchangerate-api.com/v4/latest/USD'
	#response = requests.get(url)

	#1USD = X*Schekel
	return randompy.integer( 362 , 412 )/100

def get_money_interval( difficulty ):
	curent_cr = request_currency_data()
	min_cr = curent_cr - ( 5 - difficulty )
	max_cr = curent_cr + ( 5 - difficulty )
	return { "cur" : curent_cr, "min" : min_cr , "max" : max_cr }


def get_guess_from_user():
	return input("please entere your exchange rate :")

def check_user_input( cr , ur ):
	if ur >= cr["min"] and ur <= cr["max"] :
		print("You win!:)")
		return True
	else:
		print("You lost!:(")
		return False

def play( difficulty ):
	cr = get_money_interval( difficulty )
	ur = get_guess_from_user();
	if 'Q' == ur:
		return None
	else:
		try:
			ur = float(ur)
		except Exception as e:
			print("Incorrect user input")
			return None
		return check_user_input( cr , ur )




def g3():
	print_g3_banner()
	while True:
		difficulty = input_from_array( "Please enter difficulty level 1 - 5 , Q for quit : ", [ "1" , "2" , "3" , "4" , "5"  , "Q"] )
		if "Q" == difficulty :
			return
		else:
			break
	ret = play( int(difficulty) )

	print("===============END OF GAME===============")
