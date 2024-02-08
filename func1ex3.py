def solve(numheads, numlegs):
    rabbit=(numlegs-numheads*2)//2
    chicken = numheads - rabbit
    print("there are"+str(rabbit)+"rabbits and "+str(chicken)+"chikens")
solve(35, 94)