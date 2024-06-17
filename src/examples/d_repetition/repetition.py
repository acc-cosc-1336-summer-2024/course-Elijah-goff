def test_config():
    return True

def display_numbers(num):
    
    indx = 0
    while(indx < num):#boolean expression 
        print(indx, indx > num, indx + 1) #indx + 1
        indx = indx + 1 #statement that makes boolean expression false

#sum_of_squares(3) 1*1 2*2 3*3 = 14

def sum_of_squares(num):
    sum = 0
    i = 0

    while(i <= num):#boolean expression
        sum = sum + i + i
    #statement that makes boolean expression false  

        return sum
    
def display_numbers_for(num):

    for val in range(0, num + 1):
        print(val)    

def while_nested_loop(num):
    i = 0

    while(i < num):
        print('Waiting for inner loop')

        j + 0
        while(j < num):
            print('\t inner loop')
            j += 1

    i += 1    