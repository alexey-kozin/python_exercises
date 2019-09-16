
import re

class bc:
    HEADER  = '\033[95m'
    OKBLUE  = '\033[94m'
    OKGREEN = '\033[92m'
    GREEN36 = '\033[36m'    
    WARNING = '\033[93m'
    ZIAN    = '\033[95m'    
    FAIL    = '\033[91m'
    ENDC    = '\033[0m'
    BOLD    = '\033[1m'
    UNDERLINE = '\033[4m'



def color_helper():
#!/usr/bin/python

	print "\\033[XXm"
	
	for i in range(30,37+1):
	    print "\033[%dm%d\t\t\033[%dm%d" % (i,i,i+60,i+60);
	
	print "\033[39m\\033[39m - Reset colour"
	print "\\033[2K - Clear Line"
	print "\\033[<L>;<C>H OR \\033[<L>;<C>f puts the cursor at line L and column C."
	print "\\033[<N>A Move the cursor up N lines"
	print "\\033[<N>B Move the cursor down N lines"
	print "\\033[<N>C Move the cursor forward N columns"
	print "\\033[<N>D Move the cursor backward N columns"
	print "\\033[2J Clear the screen, move to (0,0)"
	print "\\033[K Erase to end of line"
	print "\\033[s Save cursor position"
	print "\\033[u Restore cursor position"
	print " "
	print "\\033[4m  Underline on"
	print "\\033[24m Underline off"
	print "\\033[1m  Bold on"
	print "\\033[21m Bold off"
	
	
	
def input_name():
	
	while True :
	
		print("Please enter user name : 1 word/1-12 ASCII characters/'Q' for quit")
		
		n = raw_input();
		
		if len(n) < 1 or len(n) > 12 :
			print("wrong length")
			continue
		
		na = n.split()	
		if len(na) > 1 :
			print("more than one word")
			continue
		
		if not n.isalpha() :	
			print("not all ASCII characters")
			continue
					
		return n	


#def select_game():
    
#    while True :
        
        
        
    
    
    