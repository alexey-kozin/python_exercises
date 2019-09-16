import pyfiglet
from utilites import color_helper , input_name , bc

def print_banner():
    banner = pyfiglet.figlet_format("World Of Games")
    print(banner)

def welcome( name ):
    name = str(bc.BOLD)+str(bc.UNDERLINE)+name+str(bc.ENDC)
    print("")
    print("Hello %s and welcome to the World of Games(WoG)." % name )
    print("Here you can find many cool games to play.")
    print("")

def load_game():
    
    print("Please choose a game to play:")
    print("1."+bc.GREEN36+bc.BOLD+" Memory Game "+bc.ENDC+"- a sequence of numbers will appear for 1 second and you have to guess it back")
    print("2."+bc.OKBLUE+bc.BOLD+" Guess Game "+bc.ENDC+"- guess a number and see if you chose like the computer")
    print("3."+bc.ZIAN+bc.BOLD+" Weather Roulette "+bc.ENDC+"- guess the current temperature currently in Jerusalem")
    print(bc.FAIL+bc.BOLD+"Q"+bc.ENDC+" For Exit")

    try:
        sel = str( input("shut : ") )
        if len( sel ) != 1 :        
            raise Exception('Incorrect input')
        if ( sel != '1' ) and ( sel != '2' ) and ( sel != '3' ) and ( sel != 'Q' ):
            raise Exception('Incorrect input')
        
    except Exception as e :
        print( e )
        return None
    except BaseException as e :
        print( e )
        return None
    
    
    return sel
        
    

def main():
    
    print_banner()
    
    user_name = input_name()
    
    if 'Q' == user_name:
        return
    
    welcome( user_name )

    
#    while None == ( sel = load_game() ):

            
            
            }
        

    #color_helper()


if __name__ == '__main__':
    main()
    