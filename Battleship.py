import random

# Store all results from prevHit
prevHits = list()

def ShipLogic(round, yourMap, yourHp, enemyHp, p1ShotSeq, p1PrevHit):
    x = random.randint(1,10)
    y = random.randint(1,10)

    # Start recording prevHits after round 1
    if round != 1:
        prevHits.append(p1PrevHit)

    return [x,y]

# Check if the placement matches the previous results
def checkPlacement(prevHits, shotSeq, placement):
    for i in range(len(prevHits)):
        hit = prevHits[i]
        shot = shotSeq[i]
        # Convert shot position to 1D-array index
        index = (shot[0] - 1) * 10 + shot[1] - 1
        cell = placement[index]
        # Check if the cell matches the previous hit
        if(hit and cell != 1):
            return False
        if(not hit and cell != 0):
            return False
    return True