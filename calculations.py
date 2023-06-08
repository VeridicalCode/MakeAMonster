
# DEFENSIVE PROPERTIES

# monster health
def calculateHealth(CR, partySize):
    """Determines target health based on CR, then adjusts for
    party size"""
    
    # PHB monsters assume a party size of 4; monsters will
    #  live too long or too briefly if HP is not adjusted
    playerRatio = partySize/4
    healthArray = []
    finalHealth = 15

    # very fiddly at less than 1
    if (CR < 1):
        match CR:
            case 0.125:
                finalHealth = 9
            case 0.25:
                finalHealth = 15
            case 0.5:
                finalHealth = 24
            case _:
                finalHealth = 3
    elif (1 <= CR < 8):
        finalHealth = 15 * (CR + 1) * playerRatio
    else:
        finalHealth = 15 * CR * playerRatio

    # now determine swing. HP must be an integer; rounding down
    #   is fine, this isn't an exact science
    healthArray.append(int(finalHealth * 0.5))
    healthArray.append(int(finalHealth))
    healthArray.append(int(finalHealth * 1.5))

    # and spit it back out
    return healthArray

# armor class
def calculateArmor(CR):
    '''Determines target AC as a function of
    target challenge rating'''
    if (CR < 0.25):
        finalAC = 12
    elif (0.25 <= CR <= 1):
        finalAC = 13
    else:
        finalAC = 13 + CR / 2

    # still don't want fractions or decimals
    return int(finalAC)

# saving throw bonus
def calculateSave(CR):
    '''Determines saving throw bonuses
    as a function of target CR'''
    if (CR < 0.5):
        finalSave = 2
    elif (0.5 <= CR <= 1):
        finalSave = 3
    else:
        finalSave = 3 + 0.5 * CR

    # as ever, no fractions or decimals
    return int(finalSave)

# OFFENSIVE PROPERTIES

# attack bonus
def calculateAttack(CR):
    '''Determines target attack roll bonus
    as a function of target CR'''
    if (CR < 0.5):
        finalAttk = 3
    elif (0.5 <= CR <= 1):
        finalAttk = 4
    else:
        finalAttk = 4 + 0.5 * CR
    
    return int(finalAttk)

# offensive save DC
def calculateDC(CR):
    '''Determines target DC for spells and
    special abilities based on target CR'''
    if (CR < 0.5):
        finalDC = 10
    elif (0.5 <= CR <= 1):
        finalDC = 11
    else:
        finalDC = 11 + 0.5 * CR

    return int(finalDC)

# damage per round
def calculateDPR(CR):
    '''Determines target DPR for a monster based
    on CR. Returns an array; 2nd slot is base DPR,
    1st and 3rd represent +/-50% wiggle room, and
    4th entry is damage of a recharging nuke'''
    DPRArray = []
    finalDPR = 11

    # unsurprisingly, just as fiddly as health
    if (CR < 1):
        match CR:
            case 0.125:
                finalDPR = 3
            case 0.25:
                finalDPR = 5
            case 0.5:
                finalDPR = 8
            case _:
                finalDPR = 10
    elif (1 <= CR < 8):
        finalDPR = 5 * (CR + 1)
    else:
        finalDPR = 5 * CR

    # now determine swing, same as health. note
    # the first value is also AoE value
    DPRArray.append(int(finalDPR * 0.5))
    DPRArray.append(int(finalDPR))
    DPRArray.append(int(finalDPR * 1.5))
    # and add "limited use" value
    DPRArray.append(int(finalDPR * 4))

    # and spit it back out
    return DPRArray
