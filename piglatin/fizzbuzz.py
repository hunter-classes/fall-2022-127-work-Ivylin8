number = 1 #starts printing at 1
while number <=100: #print less than or equal to 100
    print(number) #prints number
    number = number + 1 #takes current number and add 1
    
    if number % 3 == 0 and number % 5 == 0:
        print('fizzbuzz')
    elif number % 3 == 0: #elif (if else)
            print ('fizz')
    elif number % 5 == 0:
            print ('buzz')
      
        
    
    