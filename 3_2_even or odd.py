n = int (input ('enter a number: ')) #set n to be the number entered by the user
r = n % 2 #set r to be the remainder when n is divided by 2
if r == 0: #if the remainder is equal to 0, then print 'even'
    print ('n is even')
else: #if the remainder is not equal to 0, then print 'odd'
    print (' n is odd')
