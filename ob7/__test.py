def tester(num, xlist):

    for number in xlist:
        print("ERRORTEST: ", number)
        
        if num == number:

            return number
        

    return None

print(tester("LOL", [1, 2, 3]))