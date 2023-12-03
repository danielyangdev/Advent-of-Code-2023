def calibrationSum(fileName = "test.txt"):
    total = 0
    file = open(fileName, "r")
    # file = open("Advent-of-Code-2023/Day_1/input.txt")
    
    
    for value in file:
        print(value)
    

    file.close()
    
def main():
    calibrationSum()

if __name__ == "__main__":
    main()