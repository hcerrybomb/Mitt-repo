stringVariable = "hello world!"     #a string type variable, string values will alway be enclosed in quotes, 
                                    #you can also directly put strings in print() command
                                    
stringVariableTwo = "25"            #another string type variable

integerVariable = 25                #a integer type variable, integer (aka whole number) variables are not enclosed in quotes, 
                                    #and have the mathematical value of the number you assign the variable
                                    
integerVariableTwo = 45             #antother integer type variable

floatVariable = 15.5                #a float type variable, same as an integer type variable except it doesnt have
                                    #to be a whole number, can have decimals

if stringVariableTwo == "25":       #IGNORE THIS LINW, only focus on the print functions, the if, try and except 
                                    #are only there to show errors
    try:                            #IGNORE THIS LINE
                                    #we use the + operator to add variables together, for example variable + variable
        print("\nnow lets see what happens when we add the string variables together: ",stringVariable + stringVariableTwo)
        
        print("\nnow lets see what happens when we add the number variables together: ",integerVariable + integerVariableTwo)

        print("\nnow lets see what happens when we add a string variable and a number variable together: ")
        print(stringVariableTwo + integerVariable)
    except:                         #IGNORE THIS LINE
        import sys                  #IGNORE THIS LINE
        print("\nExpected error : ",sys.exc_info(),"occurred")

        print("\nas we can see, we got an error, why is that?")

print("\nto give a little hint, with the type() command we can easily find the type of variables")

print("\nthe type of stringVariableTwo is: ",type(stringVariableTwo))

print("\nthe type of integerVariable is: ",type(integerVariable))