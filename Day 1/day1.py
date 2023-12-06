def calibrationSum():
    total = 0
    file = open("/Users/danielyang/VSCodeProjects/Advent of Code 2023/Advent-of-Code-2023/Day 1/test.txt", "r")
    
    for value in file:
        firstNum = -1
        lastNum = 0
        for letter in range(len(value)):
            if firstNum == -1 and value[letter].isdigit() == True:
                firstNum = value[letter]
            elif value[letter].isdigit() == True:
                lastNum = value[letter] 
                
        if lastNum == 0:
            lastNum = int(str(firstNum) + str(firstNum))
            
        print("TOTAL")
        total = int(firstNum) + int(lastNum)
        # total = total + int(firstNum) + int(lastNum)
        continue
        
    print(total)
    file.close()
    
def main():
    calibrationSum()

if __name__ == "__main__":
    main()