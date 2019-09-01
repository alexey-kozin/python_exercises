from safeInput import get_int
from safeInput import get_word
from safeInput import get_string

def main():
    name = get_word("Please input your name : ")
    age  = get_int("please input your age :  ")

    print( name , age )


if __name__ == '__main__':
    main()



