# *****************************************************************************
# Author:           Mars Getsoian
# Lab:              6 - Input validation
# Date:             5/22/2023
# Description:      This program calculates balanced in-game properties
#                    for a 5th edition D&D monster, based on formulas
#                    back-engineered by the Blog of Holding, using
#                    the number of players and avg player level provided.
# Input:            1 integer (numPlayers), 1 float (avgLvL)
# Output:           three integers (AC, HP, Save Bonus)
# Sources:          Lab 6 walkthru & replit, Blog of Holding
# *****************************************************************************

# SAMPLE RUN:
# Welcome to the Monster Builder!
# 
# How many players in the party?
# 3
# What challenge rating do you want the monster to have?
# 6
# Calculating data for 3 players, given a target CR of 6.0 .
# 
# HEALTH
# Your monster should have about 78 hit points.
# You can safely adjust this by up to 50% in either direction:
# as little as 39 or as much as 118.
#   If you expect your monster to avoid significant damage (IE,
# through features like evasion or resistances), reduce its HP
# by that amount.
# 
# ARMOR CLASS:
# Your monster should have an AC of 16.
# You can adjust this by ±3; in particular, if you adjust the
# hit points, consider bumping the AC a corresponding amount in
# the opposite direction.
# 
# SAVING THROW BONUS:
# Pick 1-4 strong saves for your monster, based on concept.
# Your monster should have a +6 bonus to those saves.
# 
# ATTACK BONUS:
# Your monster should have a +7 bonus to attack rolls.
# 
# SAVE DC:
# If your monster forces a saving throw, it should be against
# a DC of 14.
# 
# DAMAGE:
# Your monster's max damage for one round should be about 35.
# You can ajust this to as little as 17 or as much as 52.
# Any auras, lair abilities, and opportunity attacks should also deal
# about this much damage. If your monster has multiattack, divide
# the damage across its attacks.
#    Any special actions that will only be used once or twice in a
# combat encounter can deal as much as 140 damage. An AoE
# ability should deal about 17 damage. If you adjust the base
# damage, these numbers can be adjusted accordingly (4x and half,
# respectively).
# 
# Would you like to see a list of all monsters so far? (y/n)
# n
# Would you like to make another monster? (y/n)

# include
import calculations as calc
import inputs as prompt
import outputs as post

# code body
def main():
    # variables
    numPlayers = 4
    avgLvl = 1
    repeat = 'y'
    list = 'n'
    monstArray = []

    # welcome user and find out how many players are present
    #   (we can assume numPlayers will remain constant for a given
    #   run and ask outside the loop)
    post.printWelcome()
    numPlayers = prompt.getPartySize()

    while repeat == 'y':
        # get the CR
        avgLvl = prompt.getTargetCR()

        # remind the DM what they input
        post.printInputVerify(numPlayers, avgLvl)

        # CR zero has its own thing
        if avgLvl == 0:
            post.printForCRzero()

        # do the math (do the monster math)
        else:
            targetHealth = calc.calculateHealth(avgLvl, numPlayers)
            targetAC = calc.calculateArmor(avgLvl)
            targetSave = calc.calculateSave(avgLvl)
            targetAttk = calc.calculateAttack(avgLvl)
            targetDC = calc.calculateDC(avgLvl)
            targetDMG = calc.calculateDPR(avgLvl)

            # and print the math (it's a tabletop smash)
            post.printMonsterHealth(targetHealth)
            post.printMonsterAC(targetAC)
            post.printMonsterSave(targetSave)
            post.printMonsterAttk(targetAttk)
            post.printMonsterDC(targetDC)
            post.printMonsterDPR(targetDMG)

            # store the monster
            newMon = [targetAC, targetSave, targetHealth[1], targetAttk, targetDC, targetDMG[1]]
            monstArray.append(newMon)

        #prompt for list or loop
        list = prompt.promptForList()
        if list == 'y':
            post.printAllMonsters(monstArray)        
        repeat = prompt.promptForExit()
    
# run the thing
main()