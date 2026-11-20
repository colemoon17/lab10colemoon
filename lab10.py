# Problem-solving practice 2 (competition / LeetCode style) - a step up in difficulty.
#
# Most of these are natural fits for a STACK or a QUEUE (this week's data structures).
#
# For EACH problem, work out your problem-solving OUTLINE first - restate the problem,
# try a small example by hand, and sketch your approach - BEFORE you write or generate
# any code. You may use an AI assistant to help implement your plan (see the README),
# but do the thinking first.
#
# Do not rename the functions - the tests use these names.


def eval_rpn(tokens):
    # Outline (write your plan here first):
    #   loop through each item
    #   if the value is a number, add to stack
    #   if its an operator, take the top 2 numbers and combine using the operator
    # do this by checking string of the operator and using if else

    stack = []
    for item in tokens:
        if not item in "+-/*":
            # add num to stack
            stack.append(int(item))
        else:
            # print(stack)
            # check operator
            if item == '+':
                stack.append(stack.pop() + stack.pop())
            elif item == '-':
                stack.append(stack.pop() - stack.pop())
            elif item == '*':
                stack.append(stack.pop() * stack.pop())
            elif item == '/':
                numA = stack.pop()
                numB = stack.pop()
                # print(numB // numA)
                stack.append(int(numB / numA))

            # print(stack)

    return stack.pop()


def decode_string(s):
    # Outline:
    #   go through list
    #   if the char is numeric, keep track of it + potential earlier digits (i.e. recognize 10 as 10 and not 1 + 0)
    #   keep track of repeat count and current string until a bracket opens
    #   when a bracket opens, add current string and count to stacks
    #   reset the current string and count and keep tracking
    #   when a bracket closes, take current string and top of count stack, add the string count# of times to previous string
    stringstack = []
    countstack = []

    currentStr = ""
    currentCount = 0
    
    for char in s:
        if char.isnumeric():
            currentCount *= 10
            currentCount += int(char)
        elif char == '[':
            stringstack.append(currentStr)
            countstack.append(currentCount)

            currentStr = ""
            currentCount = 0
        elif char == ']':
            lastCount = countstack.pop()
            lastString = stringstack.pop()

            currentStr = lastString + currentStr * lastCount
        else:
            currentStr += char

    return currentStr

def daily_temperatures(temps):
    # Outline:
    #   add each day to a stack
    #   when a new temp is added, check it against every other
    #   if the temp is higher, remove the other temp
    stack = []
    output = []

    for i in range(len(temps)):
        output.append(0)

    for temp in temps:
        stack.append(temp)
        for dayToCheck in stack:
            if dayToCheck != None:
                if temp > dayToCheck:
                    output[stack.index(dayToCheck)] = stack.index(temp) - stack.index(dayToCheck)
                    stack[stack.index(dayToCheck)] = None

    return output


    





def num_islands(grid):   # Part 4 - stretch (optional)
    # Outline:
    #   ...
    # TODO: `grid` is a list of equal-length strings of "1" (land) and "0" (water).
    #   Count the islands - groups of "1"s connected up/down/left/right (not diagonally).
    #   Example: ["11000","11000","00100","00011"]  ->  3
    pass


def main():
    # Optional scratch space - try your functions here, then run: python lab10.py
    # print(eval_rpn(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))   # 9
    pass


if __name__ == "__main__":
    main()
