from Live import print_banner , welcome , input_name


def main():
    
    print_banner()
    
    user_name = input_name()
    
    if 'Q' == user_name:
        return
    
    welcome( user_name )

    while True :
        sel = load_game()
        if "1" == sel :
            print ("Game1")
        elif "2" == sel :
            print ("Game2")
        elif "3" == sel :
            print ("Game3")
        elif "3" == sel:
            return



            
            

        

    #color_helper()


if __name__ == '__main__':
    main()
    