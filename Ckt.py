print("what is the CktNum")
cktNum = input()

remainder = int(cktNum)%6
print("Remainder is " , remainder)

if int(cktNum) < 6: 
    remainder = int(cktNum)
    print("ckt num was less than 6 ")
    print(" remainder is ", remainder)



def answer (remainder):
    if remainder == 0 or remainder == 5:
        return "Blue"
    elif remainder == 1 or remainder == 2:
        return "Black"
    elif remainder == 3 or remainder == 4:
        return "Red"
    else:
        return "error u dumb"

print(answer(remainder))

    