n = 0  #variable to store the number entered by the user 

sum = 0  #variable to store sum of numbers

count = 0  #variable to count input numbers

#loop until the value of n is not -1

while n != -1:

    #input for the value of the number 

    n = int(input("Enter a number (-1 to quit): "))

    #if n is not -1 add n to the sum and increase the count by 1

    if n != -1:

        sum = sum + n

        count = count + 1

#print sum/count which is the required value of the average of numbers

print("The average of numbers is ", sum/count)