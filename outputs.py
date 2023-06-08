def printWelcome():
    print("Welcome to the Monster Builder!\n")

def printInputVerify(num, CR):
    print("Calculating data for", num, "players, given a target CR of", CR, ".\n")
    # TODO: low CRs should be input and output as fraction strings, and converted
    #       behind the scenes.


# defensive stats
def printMonsterHealth(hp):
    print("HEALTH")
    print(f"Your monster should have about {hp[1]} hit points.")
    print("You can safely adjust this by up to 50% in either direction:")
    print(f"as little as {hp[0]} or as much as {hp[2]}.")
    print("  If you expect your monster to avoid significant damage (IE,")
    print("through features like evasion or resistances), reduce its HP")
    print("by that amount.\n")

def printMonsterAC(ac):
    print("ARMOR CLASS:")
    print(f"Your monster should have an AC of {ac}.")
    print("You can adjust this by ±3; in particular, if you adjust the")
    print("hit points, consider bumping the AC a corresponding amount in")
    print("the opposite direction.\n")

def printMonsterSave(sv):
    print("SAVING THROW BONUS:")
    print("Pick 1-4 strong saves for your monster, based on concept.")
    print(f"Your monster should have a +{sv} bonus to those saves.\n")

# offensive stats
def printMonsterAttk(attk):
    print("ATTACK BONUS:")
    print(f"Your monster should have a +{attk} bonus to attack rolls.\n")

def printMonsterDC(dc):
    print("SAVE DC:")
    print("If your monster forces a saving throw, it should be against")
    print(f"a DC of {dc}.\n")

def printMonsterDPR(dmg):
    print("DAMAGE:")
    print(f"Your monster's max damage for one round should be about {dmg[1]}.")
    print(f"You can ajust this to as little as {dmg[0]} or as much as {dmg[2]}.")
    print("Any auras, lair abilities, and opportunity attacks should also deal")
    print("about this much damage. If your monster has multiattack, divide")
    print("the damage across its attacks.")
    print("   Any special actions that will only be used once or twice in a")
    print(f"combat encounter can deal as much as {dmg[3]} damage. An AoE")
    print(f"ability should deal about {dmg[0]} damage. If you adjust the base")
    print("damage, these numbers can be adjusted accordingly (4x and half,")
    print("respectively).")

# CR 0 is weird, and goes straight to print with no math
def printForCRzero():
    '''CR zero is static, this goes straight to Print()'''
    print("At CR 0, a monster should have <5 hit points, an armor")
    print("class between 10 and 12, +1 to its best saves, +2 to")
    print("any attack rolls, and a saving throw DC of 9 for any")
    print("spells or special abilities. Its damage per round should")
    print("not exceed 3, and can be as low as 1.")

# recap
def printAllMonsters(monstArray):
    for i in range(len(monstArray)):
        '''doesn't store or print CR zero'''
        print(f"\nMonster {i+1}:")
        print(f"AC {monstArray[i][0]}, save +{monstArray[i][1]}, hp {monstArray[i][2]}")
        print(f"Attk +{monstArray[i][3]}, DC {monstArray[i][4]}, DPR {monstArray[i][5]}")
