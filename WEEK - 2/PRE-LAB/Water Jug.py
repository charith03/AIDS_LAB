from collections import defaultdict
jug1=int(input("Enter jug1 capacity:"))
jug2=int(input("Enter jug2 capacity:"))
aim1=int(input("Enter aim:"))
visited = defaultdict(lambda: False)
def waterJugSolver(amt1, amt2):
        if (amt1 == aim1 and amt2 == 0) or (amt2 == aim1 and amt1 == 0):
                print(amt1, amt2)
                return True
        if visited[(amt1, amt2)] == False:
                print(amt1, amt2)
                visited[(amt1, amt2)] = True
                return (waterJugSolver(0, amt2) or waterJugSolver(amt1, 0) or waterJugSolver(jug1, amt2) or
                waterJugSolver(amt1, jug2) or waterJugSolver(amt1 + min(amt2, (jug1-amt1)),amt2 - min(amt2, (jug1-amt1))) or
                waterJugSolver(amt1 - min(amt1, (jug2-amt2)),amt2 + min(amt1, (jug2-amt2))))
        else:
                return False

print("Steps: ")
waterJugSolver(0,0)