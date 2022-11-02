import random
from time import sleep
playerinput = None
def space_indent():
    print('\n' * 40)
def get_playerinput():
    return str(input('Action: ').upper().strip())
def attack(attackerdamage, defenderhealth, defenderdefense):
    actualdmg = round((1 - (defenderdefense // 100)) * attackerdamage)
    return defenderhealth - actualdmg
def run_caves(playerdamage, playerhealth, playerdefense, playercoins):
    bigrock_stats = {'Health': 3, 'Defense': 5, 'Damage': 1, 'GoldDrop': '1-5'}
    creepingspider_stats = {'Health': 4, 'Defense': 0, 'Damage': 1.5, 'GoldDrop': '2-6'}
    armedskeleton_stats = {'Health': 2, 'Defense': 0, 'Damage': 3, 'GoldDrop': '2-7'}
    ridicouslyhumongousearthworm_stats = {'Health': 20, 'Defense': 10, 'Damage': 5, 'GoldDrop': '15-30', 'Intro': 'The earth begins to shake...'}
    Bosses = ['Ridicously Humongous Earth Worm']
    boss_stats = {Bosses[0]: ridicouslyhumongousearthworm_stats}
    Enemies = ['Big Rock', 'Creeping Spider', 'Armed Skeleton']
    enemy_stats = {Enemies[0]: bigrock_stats, Enemies[1]: creepingspider_stats, Enemies[2]: armedskeleton_stats}
    enemymoves = ['Attack']
    retreat = 'a'
    totalearned = 0
    space_indent()
    print('Entering the caves...')
    for i in range(10):
        enemy = random.choice(Enemies)
        space_indent()
        print(f'A {enemy} spawned!')
        print(f'{(enemy_stats[enemy])}\n'.replace('{', '').replace('}', '').replace(' ', '').replace(',', '\n').replace('\'', ''))
        estats = enemy_stats[enemy].copy()
        while int(estats['Health']) > 0 and playerhealth > 0:
            print('\n\nYour Move:\na. Attack')
            choice = str(input('Choice: ').upper())
            space_indent()
            if choice == 'A':
                ehealth = attack(playerdamage, estats["Health"], estats["Defense"])
                estats['Health'] = ehealth
                print(f'{enemy}:\n{estats}\n'.replace('{', '').replace('}', '').replace(' ', '').replace(',', '\n').replace('\'', ''))
            emove = random.choice(enemymoves)
            if emove == enemymoves[0]:
                print(f'{enemy} Attacks!')
                playerhealth = attack(estats["Damage"], playerhealth, playerdefense)
                print(f'Player Stats:\nHealth: {playerhealth}\nDefense: {playerdefense}\nDamage: {playerdamage}')
        else:
            if playerhealth > 0 and estats['Health'] <= 0: 
                space_indent()
                print(f'Player Stats:\nHealth: {playerhealth}\nDefense: {playerdefense}\nDamage: {playerdamage}')
                goldearned = random.randint(int((estats["GoldDrop"])[0]), int((estats["GoldDrop"])[2]))
                print(f'\n\nResults:\nGold Dropped: {goldearned}')
                totalearned += goldearned
                playercoins += goldearned
            else:
                space_indent()
                print('You Lost!')
                print(f'Death Fees: -{round(totalearned * 0.8)} from {totalearned} earned.')
                totalearned -= round(totalearned * 0.8)
                sleep(5)
                break
            print(f'Total coins: {playercoins}')
            print('Would you like to retreat?\n')
            while retreat != 'YES' and retreat != 'NO':
                retreat = str(input('Yes or No: ').upper())
            if retreat == "YES":
                break
            elif retreat == "NO":
                pass
    if retreat != 'YES':
        spawnboss = random.choice(Bosses)
        space_indent()
        print((boss_stats[spawnboss])['Intro'])
        bstats = boss_stats[spawnboss].copy()
        print(f'{spawnboss}:\nHealth: {bstats["Health"]}\nDefense: {bstats["Defense"]}\nDamage: {bstats["Damage"]}\nGoldDrop: {bstats["GoldDrop"]}\n')
        while int(bstats['Health']) > 0 and playerhealth > 0:
                print('\n\nYour Move:\na. Attack')
                choice = str(input('Choice: ').upper())
                space_indent()
                if choice == 'A':
                    bhealth = attack(playerdamage, bstats["Health"], bstats["Defense"])
                    bstats['Health'] = bhealth
                    print(f'{spawnboss}:\nHealth: {bstats["Health"]}\nDefense: {bstats["Defense"]}\nDamage: {bstats["Damage"]}\nGoldDrop: {bstats["GoldDrop"]}\n')
                bmove = random.choice(enemymoves)
                if bmove == enemymoves[0]:
                    print(f'{spawnboss} Attacks!')
                    playerhealth = attack(bstats["Damage"], playerhealth, playerdefense)
                    print(f'Player Stats:\nHealth: {playerhealth}\nDefense: {playerdefense}\nDamage: {playerdamage}')
        else:
            if playerhealth > 0 and bstats['Health'] < 0:
                space_indent()
                print(f'Player Stats:\nHealth: {playerhealth}\nDefense: {playerdefense}\nDamage: {playerdamage}')
                goldearned = random.randint(int((bstats["GoldDrop"])[0]), int((bstats["GoldDrop"])[2]))
                print(f'\n\nResults:\nGold Dropped: {goldearned}')
                totalearned += goldearned
                playercoins += goldearned
                print(f'Total coins: {playercoins}')
                sleep(5)
            else:
                space_indent()
                print('You Lost!')
                print(f'Death Fees: -{round(totalearned * 0.8)} from {totalearned} earned.')
                totalearned -= round(totalearned * 0.8)
                sleep(5)
    return totalearned, playerhealth

Fists = {'Name': 'Fists', 'Damage': 1, 'Value': 0}
WoodBlade = {'Name': 'Wood Blade', 'Damage': 2, 'Value': 10}
IronBlade = {'Name': 'Iron Blade', 'Damage': 5, 'Value': 80}
weaponshop = {'Wood Blade': WoodBlade, 'Iron Blade': IronBlade}
player_health = 100
player_coins = 10
player_damage = 0
player_defense = 0
playerweapons = [Fists]

notenough = False

space_indent()
print('Welcome to BitFighter!\n\n')
print('Type \'help\' for list of actions.')
playerinput = get_playerinput()
while True:
    if playerinput == 'QUIT' or playerinput == 'EXIT':
        space_indent()
        print('Exitting...')
        break
    elif playerinput == 'HELP':
        space_indent()
        print('Not done')
        playerinput = get_playerinput()
    elif playerinput == 'EQUIP':
        space_indent()
        print('Choose Option:\na. Weapons\n')
        chose = str(input('Choice: ').upper().strip())
        if chose == 'A':
            ownedweapons = []
            for weapon in playerweapons:
                ownedweapons.append(weapon['Name'])
            print(f'Type weapon to equip:\n{ownedweapons}\n'.replace('[', '').replace(']', '').replace('\'', '').replace(', ','\n'))
            weaponchoice = str(input('Choice: '))
            if weaponchoice in playerweapons:
                print('Equipped!')
        playerinput = get_playerinput()
    elif playerinput == 'FIGHT':
        print('Choose dungeon:\na. Caves')
        choice = str(input('Choice: ').upper())
        if choice == 'A':
            if player_health > 0:
                results = run_caves(player_damage, player_health, player_defense, player_coins)
                (totalearned, playerhealth) = results
                player_health = playerhealth
                if player_health < 0:
                    player_health = 0
                player_coins += totalearned
                space_indent()
                playerinput = get_playerinput()
            else:
                space_indent()
                print('Health too low!')
                playerinput = get_playerinput()
    elif playerinput == 'STATS':
        ownedweapons = []
        for weapon in playerweapons:
            ownedweapons.append(weapon['Name'])
        print(f'Health: {player_health}\nDefense: {player_defense}\nDamage: {player_damage}\nCoins: {player_coins}\nOwned Weapons: {ownedweapons}\n'.replace('[', '').replace(']', '').replace('\'', ''))
        playerinput = get_playerinput()
    elif playerinput == 'STORE':
        space_indent()
        if notenough == True:
            notenough = False
            print('Not enough coins!\n\n')
        print('Choose service:\na. Weapons\n')
        storechoice = str(input('Choice: ').upper())
        if storechoice == 'A':
            space_indent()
            print('Type Weapon Name to Buy or Type Cancel to exit menu.\n\n')
            for item in weaponshop:
                print(f'{item}:\n{weaponshop[item]}\n'.replace('{', '').replace('}', '').replace('Value', 'Price').replace('\'', '').replace(', ', '\n').replace(':', ' Stats', 1).replace(f'Name: {item}', ' ').replace('\n ', ''))
            choice2 = str(input('Choice: ').upper())
            if choice2 == 'CANCEL':
                pass
            elif choice2 == 'WOODBLADE' or 'WOOD BLADE':
                if player_coins >= WoodBlade['Value']:
                    player_coins -= WoodBlade['Value']
                    print('Bought!')
                    playerweapons.append(WoodBlade)
                else:
                    notenough = True
                    continue
            else:
                continue
            playerinput = get_playerinput()
        else:
            continue
    else:
        print('Not an action. Type \'help\' for list of actions.')
        playerinput = get_playerinput()