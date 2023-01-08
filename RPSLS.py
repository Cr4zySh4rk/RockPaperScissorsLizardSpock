import random, os, time
title = '''

██████╗░░█████╗░░█████╗░██╗░░██╗
██╔══██╗██╔══██╗██╔══██╗██║░██╔╝
██████╔╝██║░░██║██║░░╚═╝█████═╝░
██╔══██╗██║░░██║██║░░██╗██╔═██╗░
██║░░██║╚█████╔╝╚█████╔╝██║░╚██╗
╚═╝░░╚═╝░╚════╝░░╚════╝░╚═╝░░╚═╝

██████╗░░█████╗░██████╗░███████╗██████╗░
██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗
██████╔╝███████║██████╔╝█████╗░░██████╔╝
██╔═══╝░██╔══██║██╔═══╝░██╔══╝░░██╔══██╗
██║░░░░░██║░░██║██║░░░░░███████╗██║░░██║
╚═╝░░░░░╚═╝░░╚═╝╚═╝░░░░░╚══════╝╚═╝░░╚═╝

░██████╗░█████╗░██╗░██████╗░██████╗░█████╗░██████╗░░██████╗
██╔════╝██╔══██╗██║██╔════╝██╔════╝██╔══██╗██╔══██╗██╔════╝
╚█████╗░██║░░╚═╝██║╚█████╗░╚█████╗░██║░░██║██████╔╝╚█████╗░
░╚═══██╗██║░░██╗██║░╚═══██╗░╚═══██╗██║░░██║██╔══██╗░╚═══██╗
██████╔╝╚█████╔╝██║██████╔╝██████╔╝╚█████╔╝██║░░██║██████╔╝
╚═════╝░░╚════╝░╚═╝╚═════╝░╚═════╝░░╚════╝░╚═╝░░╚═╝╚═════╝░

By Adithya Manjunath (github.com/Cr4zySh4rk/RockPaperScissorsLizardSpock)
'''
print(title)

def clrscr():
    os.system('clear')

def thinking(string):
    string = list(string)
    for char in string:
        time.sleep(0.075)
        print(char, end="")

def mode():
    print('\n######################## [SELECT MODE] ########################')
    print("\n[1] Classic (Rock-Paper-Scissors)")
    print("[2] Advanced (Rock-Paper-Scissors-Lizard-Spock)")
    print("[3] Snake-Water-Gun")
    print("[4] Lady-Hunter-Tiger")
    try:
        choice=int(input("\nEnter choice : "))
    except:
        print("Fatal Input Error!")
        quit()
    
    if(choice==1):
        return 1
    
    elif(choice==2):
        return 2
    
    elif (choice==3):
        return 3
    
    elif (choice==4):
        return 4
    
    else:
        return -1


def game():
    clrscr()
    gamemode=mode()
    if(gamemode==1):
        a='''
█▀█ █▀█ █▀▀ █▄▀
█▀▄ █▄█ █▄▄ █░█'''
        b='''
█▀ █▀▀ █ █▀ █▀ █▀█ █▀█ █▀
▄█ █▄▄ █ ▄█ ▄█ █▄█ █▀▄ ▄█'''
        c='''
█▀█ ▄▀█ █▀█ █▀▀ █▀█
█▀▀ █▀█ █▀▀ ██▄ █▀▄'''
        options=[0,a,b,c]
        print("\n<<<<<Your Move>>>>>")
        print("\n[1] Rock")
        print("[2] Scissor")
        print("[3] Paper")
        player=int(input("\nEnter choice : "))
        if (player>3 or player<1):
            print("Invalid choice!")
            quit()
        else:
            print("\nYou chose : ")
            print(options[player])
            print("\n")
            thinking("CPU is thinking ...")
            cpu=random.randint(1,3)
            print("\nCPU chose : ")
            print(options[cpu])
            if (player==cpu):
                print('\nDRAW')
            elif ((player==1 and cpu==2) or (player==2 and cpu==3) or (player==3 and cpu==1)):
                print('\nYOU WON AGAINST CPU')
                return 1
            else:
                print('\nYOU LOST AGAINST CPU')
                print('BETTER LUCK NEXT TIME!')
                return 0

    elif(gamemode==2):
        a='''
█▀█ █▀█ █▀▀ █▄▀
█▀▄ █▄█ █▄▄ █░█'''
        b='''
█▀ █▀▀ █ █▀ █▀ █▀█ █▀█ █▀
▄█ █▄▄ █ ▄█ ▄█ █▄█ █▀▄ ▄█'''
        c='''
█▀█ ▄▀█ █▀█ █▀▀ █▀█
█▀▀ █▀█ █▀▀ ██▄ █▀▄'''
        d='''
█▀ █▀█ █▀█ █▀▀ █▄▀
▄█ █▀▀ █▄█ █▄▄ █░█'''
        e='''
█░░ █ ▀█ ▄▀█ █▀█ █▀▄
█▄▄ █ █▄ █▀█ █▀▄ █▄▀'''
        options=[0,a,b,c,d,e]
        print("\n<<<<<Your Move>>>>>")
        print("\n[1] Rock")
        print("[2] Scissor")
        print("[3] Paper")
        print("[4] Spock")
        print("[5] Lizard")
        player=int(input("\nEnter choice : "))
        if (player>5 or player<1):
            print("Invalid choice!")
            quit()
        else:
            print("\nYou chose : ")
            print(options[player])
            print("\n")
            thinking("CPU is thinking ...")
            cpu=random.randint(1,5)
            print("\nCPU chose : ")
            print(options[cpu])
            if (player==cpu):
                print('\nDRAW')
            elif ( (player==1 and (cpu==2 or cpu==5)) or (player==2 and (cpu==3 or cpu==5)) or (player==3 and (cpu==1 or cpu==4)) or (player==4 and (cpu==1 or cpu==2)) or (player==5 and (cpu==3 or cpu==4)) ):
                print('\nYOU WON AGAINST CPU')
                return 1
            else:
                print('\nYOU LOST AGAINST CPU')
                print('BETTER LUCK NEXT TIME!')
                return 0

    elif(gamemode==3):
        a='''
█▀ █▄░█ ▄▀█ █▄▀ █▀▀
▄█ █░▀█ █▀█ █░█ ██▄'''
        b='''
█░█░█ ▄▀█ ▀█▀ █▀▀ █▀█
▀▄▀▄▀ █▀█ ░█░ ██▄ █▀▄'''
        c='''
█▀▀ █░█ █▄░█
█▄█ █▄█ █░▀█'''
        options=[0,a,b,c]
        print("\n<<<<<Your Move>>>>>")
        print("\n[1] Snake")
        print("[2] Water")
        print("[3] Gun")
        player=int(input("\nEnter choice : "))
        if (player>3 or player<1):
            print("Invalid choice!")
            quit()
        else:
            print("\nYou chose : ")
            print(options[player])
            print("\n")
            thinking("CPU is thinking ...")
            cpu=random.randint(1,3)
            print("\nCPU chose : ")
            print(options[cpu])
            if (player==cpu):
                print('\nDRAW')
            elif ((player==1 and cpu==2) or (player==2 and cpu==3) or (player==3 and cpu==1)):
                print('\nYOU WON AGAINST CPU')
                return 1
            else:
                print('\nYOU LOST AGAINST CPU')
                print('BETTER LUCK NEXT TIME!')
                return 0

    elif(gamemode==4):
        a='''
█░░ ▄▀█ █▀▄ █▄█
█▄▄ █▀█ █▄▀ ░█░'''
        b='''
█░█ █░█ █▄░█ ▀█▀ █▀▀ █▀█
█▀█ █▄█ █░▀█ ░█░ ██▄ █▀▄'''
        c='''
▀█▀ █ █▀▀ █▀▀ █▀█
░█░ █ █▄█ ██▄ █▀▄'''
        options=[0,a,b,c]
        print("\n<<<<<Your Move>>>>>")
        print("\n[1] Lady")
        print("[2] Hunter")
        print("[3] Tiger")
        player=int(input("\nEnter choice : "))
        if (player>3 or player<1):
            print("Invalid choice!")
            quit()
        else:
            print("\nYou chose : ")
            print(options[player])
            print("\n")
            thinking("CPU is thinking ...")
            cpu=random.randint(1,3)
            print("\nCPU chose : ")
            print(options[cpu])
            if (player==cpu):
                print('\nDRAW')
            elif ((player==1 and cpu==2) or (player==2 and cpu==3) or (player==3 and cpu==1)):
                print('\nYOU WON AGAINST CPU')
                return 1
            else:
                print('\nYOU LOST AGAINST CPU')
                print('BETTER LUCK NEXT TIME!')
                return 0

    else:
        print("Invalid mode!")

cscore=0
pscore=0   
while(True):
    print("SCORE : \nCPU : {} | YOU : {}".format(cscore,pscore))
    choice=input('\nPlay? (Y/n) : ')
    if (choice=='Y'or choice=='y' or choice==''):
        result=game()
        if(result==1):
            pscore=pscore + 1
        elif(result==0):
            cscore=cscore + 1
    elif (choice=='N'or choice=='n'):
        print('Quitting Game')
        time.sleep(1.5)
        quit()
    else:
        print("Invalid option!")