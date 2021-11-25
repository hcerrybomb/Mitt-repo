stringVariable = "hello world!"     #a string type variable, string values will alway be enclosed in quotes, 
                                    #you can also directly put strings in print() command
                                    
stringVariableTwo = "25"            #another string type variable

integerVariable = 25                #a integer type variable, integer (aka whole number) variables are not enclosed in quotes, 
                                    #and have the mathematical value of the number you assign the variable
                                    
integerVariableTwo = 45             #antother integer type variable

floatVariable = 15.5                #a float type variable, same as an integer type variable except it doesnt have
                                    #to be a whole number, can have decimals

print("\nnow lets see how else we can use variables")

print("\n we know we can combine string variables by adding them, as such: ",stringVariable+stringVariableTwo)

print("\nhowever we can perform these operations outside of commands")

                                    #you do this as such: 

combinedStringVariable = stringVariable + stringVariableTwo

                                    #as we know we use the  =  operator to declare a variable
                                    #we made a variable that has the combined value of the two other variables
                                    #since they are string variables, we can only add themselves
                                    
print("\nthe two string variables combined is: ",combinedStringVariable)

                                    #we can use this same concept for number variables, except we have a lot more
                                    #possibilities since numbers have math, and we can use all mathematical operators

integersAdded = integerVariable + integerVariableTwo