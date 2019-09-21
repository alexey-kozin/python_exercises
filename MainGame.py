from Live import print_banner , welcome , input_name , load_game
from game1 import g1
from game2 import g2
from game3 import g3

def main():
    
    print_banner()
    
    user_name = input_name()
    
    if 'Q' == user_name:
        return
    
    welcome( user_name )

    while True :
        sel = load_game()
        if "1" == sel :
            g1()
        elif "2" == sel :
            g2()
        elif "3" == sel :
            g3()
        elif "3" == sel:
            return
        elif "Q" == sel:
            return

    #color_helper()


if __name__ == '__main__':
    main()
    