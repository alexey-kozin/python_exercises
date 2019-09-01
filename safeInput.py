import msvcrt

def base_input( prompt , typeStr , cbk ):

    while True:
        if msvcrt.kbhit() and msvcrt.getch().decode() == chr(27):
            break
        ret = input(prompt)
        try:
            ret = cbk(ret)
        except:
            print('\033[91m' + "invalid input of "+typeStr+" : " + '\033[0m' + " try again or Esc to exit.")
            continue
        break
    return ret

def get_int( prompt ):
    def cast( n ):
        return int(n)
    return base_input( prompt , "int" , cast )

def get_word( prompt ):
    def cast( n ):
        if not n.isalpha():
            raise
        return n
    return base_input( prompt , "word" , cast )

def get_string( prompt ):
    def cast( n ):
        words = n.split()
        length = len(words)
        for i in range(length):
            if not words[i].isalpha():
                raise
        return n
    return base_input( prompt , "word" , cast )

