OPCODE_LENGTH = 4

def handleIntcode(intcodeList, index):
    if intcodeList[index] == 99:
        print(f'Terminating program, value at position 0 is: {intcodeList[0]}')
        exit()

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
    intcodeList = list(map(int, intcodeFile.readline().split(",")))

    for index in range(0, len(intcodeList), OPCODE_LENGTH):
        handleIntcode(intcodeList, index)

if __name__ == "__main__":
    main()