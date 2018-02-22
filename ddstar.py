# Dungeons and Dragons Stat Dice Roller
# @nAZklX on Twitter
# All files including modules are coded by nAZklX unless specified otherwise.
# Version n, I'm bad at numbers

import random
import text
import info
import time
import DDSTARv2_0_0
x = 0
y = 1
z = 2
race = ()
races = ['Dragonborn','Dwarf','Hill-Dwarf','Mountain-Dwarf','Elf','High-Elf','Wood-Elf','Drow','Gnome','Forest-Gnome','Rock-Gnome','Deep-Gnome','Half-Elf','Half-Orc','Halfling','Lightfoot-Halfling','Stout-Halfling','Human','Tiefling']
# Asks if user wants auto-addition to ability scores

print("What Would You Like To Do?")
print("1. Get Information about Races and Subraces")
print("2. Use The Roller WITHOUT Races.")
print("3. Use The Roller WITH Races.")
print(text.Bold + "4. Exit" + text.End)
absca = input('')



dinfo = 'y'

if absca == '4':
    exit()
    pass
else:
    pass
if absca == '1':
    print("Pick a race to learn more about(Subraces, Bonuses, etc.)")
    print('1. Dragonborn')
    print('2. Dwarf')
    print('3. Elf')
    print('4. Gnome')
    print('5. Half-Elf')
    print('6. Half-Orc')
    print('7. Halfling')
    print('8. Human')
    print('9. Tiefling')
    print('10. Exit')
    learn = input('')
    if learn == '1':
        print(info.Dragonborn)
        dinfo = 'n'
        time.sleep(10)
        exec('DDSTARv2_0_0')
        pass
    if learn == '2':
        print(info.Dwarf)
        print("Info About Subraces? (y/n)")
        dsub = input('')
        if dsub == 'y':
            print("1. Hill Dwarf")
            print("2. Mountain Dwarf")
            dsubc = input('')
            if dsubc == '1':
                print(info.hillDwarf)
                dinfo = 'n'
                time.sleep(10)
                exec('DDSTARv2_0_0')
            if dsubc == '2':
                print(info.mountainDwarf)
                dinfo = 'n'
                time.sleep(10)
                exec('DDSTARv2_0_0')
            else:
                pass
        else:
            pass
        dinfo = 'n'
        time.sleep(10)
        exec('DDSTARv2_0_0')
        pass
    if learn == '3':
        print(info.Elf)
        print("Info About Subraces? (y/n)")
        dsub = input('')
        if dsub == 'y':
            print("1. High Elf")
            print("2. Wood Elf")
            dsubc = input('')
            if dsubc == '1':
                print(info.highElf)
                dinfo = 'n'
                time.sleep(10)
                exec('DDSTARv2_0_0')
            if dsubc == '2':
                print(info.woodElf)
                dinfo = 'n'
                time.sleep(10)
                exec('DDSTARv2_0_0')
            else:
                pass
        else:
            pass
        dinfo = 'n'
        time.sleep(10)
        exec('DDSTARv2_0_0')
        pass
    if learn == '4':
        print(info.Gnome)
        print("Info About Subraces? (y/n)")
        dsub = input('')
        if dsub == 'y':
            print("1. Deep Gnome")
            print("2. Forest Gnome")
            print("3. Rock Gnome")
            dsubc = input('')
            if dsubc == '1':
                print(info.deepGnome)
                dinfo = 'n'
                time.sleep(10)
                exec('DDSTARv2_0_0')
            if dsubc == '2':
                print(info.forestGnome)
                dinfo = 'n'
                time.sleep(10)
                exec('DDSTARv2_0_0')
            if dsubc == '3':
                print(info.rockGnome)
                dinfo = 'n'
                time.sleep(10)
                exec('DDSTARv2_0_0')
            else:
                pass
        else:
            pass
        dinfo = 'n'
        time.sleep(10)
        exec('DDSTARv2_0_0')
        pass
    if learn == '5':
        print(info.halfElf)
        dinfo = 'n'
        time.sleep(10)
        exec('DDSTARv2_0_0')
        pass
    if learn == '6':
        print(info.halfOrc)
        dinfo = 'n'
        time.sleep(10)
        exec('DDSTARv2_0_0')
        pass
    if learn == '7':
        print(info.Halfling)
        print("Info About Subraces? (y/n)")
        dsub = input('')
        if dsub == 'y':
            print("1. Lightfoot Halfling")
            print("2. Stout Halfling")
            dsubc = input('')
            if dsubc == '1':
                print(info.lightfootHalfling)
                dinfo = 'n'
                time.sleep(10)
                exec('DDSTARv2_0_0')
            if dsubc == '2':
                print(info.stoutHalfling)
                dinfo = 'n'
                time.sleep(10)
                exec('DDSTARv2_0_0')
            else:
                pass
        else:
            pass
        dinfo = 'n'
        time.sleep(10)
        exec('DDSTARv2_0_0')
        pass
    if learn == '8':
        print(info.Human)
        dinfo = 'n'
        time.sleep(10)
        exec('DDSTARv2_0_0')
        pass
    if learn == '9':
        print(info.Tiefling)
        dinfo = 'n'
        time.sleep(10)
        exec('DDSTARv2_0_0')
        pass
    if learn == '10':
        exit()
        pass
    else:
        pass
else:
    pass

if absca == '3':
    print("What is your Race?")
    print("Dragonborn, Dwarf, Elf, Gnome, Half-Elf, Half-Orc, Halfling, Human, or Tiefling")
    race = input('')
    pass
else:
    pass

# Asks user for Sub-Races if wanted.
if absca == '3':
    if race == 'Dwarf':
        print('Would you like to be one of the subraces of Dwarf? (y/n)')
        subrace = input('')
        if subrace == 'y':
            print("'Hill-Dwarf' or 'Mountain-Dwarf?'")
            race = input('')
            sabsca = True
            pass
        else:
            pass
    if race == 'Elf':
        print('Would you like to be one of the subrace of Elf? (y/n)')
        subrace = input('')
        if subrace == 'y':
            print("'High-Elf', 'Wood-Elf', or 'Drow'")
            race = input('')
            sabsca = True
            pass
        else:
            pass
    if race == 'Gnome':
        print('Would you like to be one of the subraces of Gnome? (y/n)')
        subrace = input('')
        if subrace == 'y':
            print("'Forest-Gnome', 'Rock-Gnome', 'Deep-Gnome'")
            race = input('')
            sabsca = True
            pass
        else:
            pass
    if race == 'Halfling':
        print('Would you like to be one of the subraces of Halfling? (y/n)')
        subrace = input('')
        if subrace == 'y':
            print("'Lightfoot-Halfling' or 'Stout-Halfling'")
            race = input('')
            sabsca = True
            pass
        else:
            pass
    else:
        pass
else:
    pass

# Disclaimer: Support for Human choice between all +1 stats or getting +1 to any two ability scores, a free skill proficiency, and a free feat is not available in this version.
# Cont.: Humans automatically get +1 to all scores.
# Cont.: Sub-Races are not supported in this version.
if dinfo == 'y':
    print("Your Rolls are:")
    pass
else:
    pass

# Makes a list which includes 4 random numbers 1-6.
# Prints the stat label, the total(minus the lowest number), and the list of the 4 different rolls.
# Strength
if dinfo == 'y':
    RL1 = random.sample(range(1,6), 4)
    RL11 = (sum(RL1)-min(RL1))
    pass
else:
    pass
if absca == '3':
    if race == 'Dragonborn':
        RL11 = (sum(RL1)-min(RL1)+2)
        pass
    if race == 'Half-Orc':
        RL11 = (sum(RL1)-min(RL1)+2)
        pass
    if race == 'Human':
        RL11 = (sum(RL1)-min(RL1)+1)
        pass
    if race == 'Mountain-Dwarf':
        RL11 = (sum(RL1)-min(RL1)+2)
    pass
else:
    pass
if dinfo == 'y':
    print("STR:",RL11,RL1)
    pass
else:
    pass


# Dexterity
if dinfo == 'y':
    RL2 = random.sample(range(1,6),4)
    RL22 = (sum(RL2)-min(RL2))
    pass
else:
    pass
if absca == '3':
    if race == 'Elf':
        RL22 = (sum(RL2)-min(RL2)+2)
        pass
    if race == 'Halfling':
        RL22 = (sum(RL2)-min(RL2)+2)
        pass
    if race == 'Human':
        RL22 = (sum(RL2)-min(RL2)+1)
        pass
    if race == 'Deep-Gnome':
        RL22 = (sum(RL2)-min(RL2)+1)
        pass
    if race == 'Forest-Gnome':
        RL22 = (sum(RL2)-min(RL2)+1)
        pass
    pass
else:
    pass
if dinfo == 'y':
    print("DEX:",RL22,RL2)
    pass
else:
    pass


# Constitution
if dinfo == 'y':
    RL3 = random.sample(range(1,6),4)
    RL33 = (sum(RL2)-min(RL2))
    pass
else:
    pass
if absca == '3':
    if race == 'Dwarf':
        RL33 = (sum(RL3)-min(RL3)+2)
        pass
    if race == 'Half-Orc':
        RL33 = (sum(RL3)-min(RL3)+1)
        pass
    if race == 'Human':
        RL33 = (sum(RL3)-min(RL3)+1)
        pass
    if race == 'Rock-Gnome':
        RL33 = (sum(RL3)-min(RL3)+1)
        pass
    if race == 'Stout-Halfling':
        RL33 = (sum(RL3)-min(RL3)+1)
        pass
    pass
else:
    pass
if dinfo == 'y':
    print("CON:",RL33,RL3)
    pass
else:
    pass


# Intelligence
if dinfo == 'y':
    RL4 = random.sample(range(1,6),4)
    RL44 = (sum(RL4)-min(RL4))
    pass
else:
    pass
if absca == '3':
    if race == 'Gnome':
        RL44 = (sum(RL4)-min(RL4)+2)
        pass
    if race == 'Tiefling':
        RL44 = (sum(RL4)-min(RL4)+1)
        pass
    if race == 'Human':
        RL44 = (sum(RL4)-min(RL4)+1)
        pass
    if race == 'High-Elf':
        RL44 = (sum(RL4)-min(RL4)+1)
        pass
    pass
else:
    pass
if dinfo == 'y':
    print("INT:",RL44,RL4)
    pass
else:
    pass


# Wisdom
if dinfo == 'y':
    RL5 = random.sample(range(1,6),4)
    RL55 = (sum(RL5)-min(RL5))
    pass
else:
    pass
if absca == '3':
    if race == 'Human':
        RL55 = (sum(RL5)-min(RL5)+1)
        pass
    if race == 'Hill-Dwarf':
        RL55 = (sum(RL5)-min(RL5)+1)
        pass
    if race == "Wood-Elf":
        RL55 = (sum(RL5)-min(RL5)+1)
        pass
    pass
else:
    pass
if dinfo == 'y':
    print("WIS:",RL55,RL5)
    pass
else:
    pass


# Charisma
if dinfo == 'y':
    RL6 = random.sample(range(1,6),4)
    RL66 = (sum(RL6)-min(RL6))
    pass
else:
    pass
if absca == '3':
    if race == 'Dragonborn':
        RL66 = (sum(RL6)-min(RL6)+1)
        pass
    if race == 'Half-Elf':
        RL66 = (sum(RL6)-min(RL6)+2)
        pass
    if race == 'Tiefling':
        RL66 = (sum(RL6)-min(RL6)+2)
        pass
    if race == 'Human':
        RL66 = (sum(RL6)-min(RL6)+1)
        pass
    if race == 'Drow':
        RL66 = (sum(RL6)-min(RL6)+1)
        pass
    if race == 'Lightfoot-Halfling':
        RL66 = (sum(RL6)-min(RL6)+1)
    pass
else:
    pass
if dinfo == 'y':
    print("CHA:",(sum(RL6)-min(RL6)),RL6)
    pass
else:
    pass
# Notifies user if additions to totals occurred due to race.
if absca == '3':
    if race == 'Dragonborn':
        print(text.Bold + text.Green + 'Dragonborn gets +1 to Charisma & +2 to Strength and has been added to the total(s).', text.End)
        pass
    if race == 'Dwarf':
        print(text.Bold + text.Green + 'Dwarf gets +2 to Strength and has been added to the total(s).', text.End)
        pass
    if race == 'Elf':
        print(text.Bold + text.Green + 'Elf gets +2 to Dexterity and has been added to the total(s).', text.End)
        pass
    if race == 'Gnome':
        print(text.Bold + text.Green + 'Gnome gets +2 to Intelligence and has been added to the total(s).', text.End)
        pass
    if race == 'Half-Orc':
        print(text.Bold + text.Green + 'Half-Orc gets +2 to Strength & +1 to Constitution and has been added to the total(s).', text.End)
        pass
    if race == 'Halfling':
        print(text.Bold + text.Green + 'Halfling gets +2 to Dexterity and has been added to the total(s).', text.End)
        pass
    if race == 'Human':
        print(text.Bold + text.Green + 'Halfling gets +1 to ALL STATS and has been added to the total(s).', text.End)
        pass
    if race == 'Tiefling':
        print(text.Bold + text.Green + 'Tiefling gets +2 to Charisma & +1 to Intelligence and has been added to the total(s).', text.End)
        pass
    if sabsca == True:
        if race == 'High-Elf':
            print(text.Bold + text.Green + 'High-Elf gets +1 to Intelligence and has been added to the total(s).',
                  text.End)
            pass
        if race == 'Wood-Elf':
            print(text.Bold + text.Green + 'Wood-Elf gets +1 to Wisdom and has been added to the total(s).', text.End)
            pass
        if race == 'Deep-Gnome':
            print(text.Bold + text.Green + 'Deep-Gnome gets +1 to Dexterity and has been added to the total(s).',
                  text.End)
            pass
        if race == 'Forest-Gnome':
            print(text.Bold + text.Green + 'Forest-Gnome gets +1 to Dexterity and has been added to the total(s).',
                  text.End)
            pass
        if race == 'Rock-Gnome':
            print(text.Bold + text.Green + 'Rock-Gnome gets +1 to Constitution and has been added to the total(s).',
                  text.End)
            pass
        if race == 'Lightfoot-Halfling':
            print(text.Bold + text.Green + 'Lightfoot-Halfling gets +1 to Charisma and has been added to the total(s).',
                  text.End)
            pass
        if race == 'Stout-Halfling':
            print(text.Bold + text.Green + 'Stout-Halfling gets +1 to Constitution and has been added to the total(s).',
                  text.End)
        if race == 'Hill-Dwarf':
            print(text.Bold + text.Green + 'Hill-Dwarf gets +1 to Wisdom and has been added to the total(s).', text.End)
            pass
        if race == 'Mountain-Dwarf':
            print(text.Bold + text.Green + 'Mountain-Dwarf gets +2 to Strength and has been added to the total(s).', text.End)
            pass
        if race == 'Half-Elf':
            print(text.Bold + text.Green + 'Half-Elf gets +2 to Charisma and has been added to the total(s).', text.End)
            pass
        if race == 'Drow':
            print(text.Bold + text.Green + 'Drow gets +1 to Charisma and has been added to the total(s).', text.End)
            pass
        pass
    else:
        pass
    pass
else:
    pass

# Confirms that the race given is usable for accurate additions to stats.
if absca == '3':
    if race in races:
        pass
    else:
        print(text.Bold + text.Green + "Rolls/Totals may be inaccurate due misspelling of race/input of race not listed.", text.End)
        print ("Race Given:" + text.Red + text.Bold, race, text.End)
    pass
else:
    pass
