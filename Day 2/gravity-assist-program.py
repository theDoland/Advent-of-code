OPCODE_LENGTH = 4
TARGET_NUM = 19690720

def handleIntcode(intcodeList, index):
    in_pos_1 = intcodeList[index + 1]
    in_pos_2 = intcodeList[index + 2]
    output_pos = intcodeList[index + 3]

    if intcodeList[index] == 1:
        additionOpcode(intcodeList, in_pos_1, in_pos_2, output_pos)
    elif intcodeList[index] == 2:
        multiplicationOpcode(intcodeList, in_pos_1, in_pos_2, output_pos)
    else:
        raise ValueError(f'Error, intcode at index is not a valid intcode: {intcodeList[index]}')
        
def additionOpcode(intcodeList, in_pos_1, in_pos_2, output_pos):
    intcodeList[output_pos] = intcodeList[in_pos_1] + intcodeList[in_pos_2]

def multiplicationOpcode(intcodeList, in_pos_1, in_pos_2, output_pos):
    intcodeList[output_pos] = intcodeList[in_pos_1] * intcodeList[in_pos_2]

def main():
    intcodeFile = open("input.txt", "r")
    originalIntcodeList = list(map(int, intcodeFile.readline().split(",")))

    for x in range(0, 100):
        for y in range(0, 100):
            intcodeList = originalIntcodeList[:]
            intcodeList[1] = x
            intcodeList[2] = y

            for index in range(0, len(intcodeList), OPCODE_LENGTH):
                if intcodeList[index] == 99:
                    break
                handleIntcode(intcodeList, index)
            
            if intcodeList[0] == TARGET_NUM:
                print(f'Noun is: {x}, Verb is: {y}, \n Value of 100 * {x} + {y} is: {100 * x + y}')
                exit()

if __name__ == "__main__":
    main()