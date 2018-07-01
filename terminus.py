from trantor import *
import os


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


clear()

print('''
            ----------------------------------------------------
                             TERMINUS (Alpha I)
                        An extension for Anacreon 3
            By Imperator (anacreonlib framework by Ritik Mishra)
            ----------------------------------------------------
    ''')


def imperialMenu():
    print('''
    Welcome, Dread Sovereign.
    The '''+empireName+''' consists of '''+str(getSovStat('worlds', empireName))+''' worlds with a total population of '''+str(int(getSovStat('population', empireName)/1000))+''' billion.
    The average efficiency of the Empire is '''+str(int(getAvgEfficiency(empireName)))+''' % and its military force consists of '''+str(getSovStat('fleets', empireName))+''' fleets.
    ''')

    action = input('''
    The Ministries in service to the Imperial Throne are:

        [1] The Ministry of War
        [2] The Ministry of Commerce
        [3] The Ministry of Diplomacy
        [4] The Ministry of Intelligence

    (Input the number corresponding to the desired action, or any other value to exit)
    Awaiting command: ''')

    if action == '1':
        ministryOfWar()
    if action == '2':
        ministryOfCommerce()
    if action == '3':
        ministryOfDiplomacy()
    if action == '4':
        ministryOfIntelligence()
    else:
        exit()


def ministryOfWar():
    clear()
    action = input('''
        The Imperial Ministry of War
        ----------------------------
        Available orders:

            [1] Consolidate all fleets over a world
            [2] Reinforce a world with fleets from shipyards

        Order: ''')
    if action == '1':
        clear()
        world = input('''
        Over which world shall we merge all orbiting fleets?
        World: ''')
        mergeFleet = input('''
        To which fleet over '''+world+''' shall we merge all the others?
        Fleet: ''')
        transfer = input('''
        Shall we also send the newly combined fleet down to '''+world+'''?
            [1] Yes
            [2] No
        Response: ''')
        mergeFleets(world, mergeFleet, transfer)
        input('\nPress Enter to return to the Ministry menu...')
        refresh()
        ministryOfWar()
    if action == '2':
        clear()
        desig = input('''
        From which of our shipyards shall we deploy reinforcements?
            [1] Jumpship yards
            [2] Starship yards
            [3] Ramjet yards
        Shipyard: ''')
        dest = input('''
        To which world shall we deploy reinforcements?
        World: ''')
        print('\n')
        reinforceWorld(desig, dest)
        input('\nPress Enter to return to the Ministry menu...')
        refresh()
        ministryOfWar()
    else:
        clear()
        imperialMenu()


def ministryOfCommerce():
    clear()
    action = input('''
        The Imperial Ministry of Commerce
        ---------------------------------
        Available orders:

            [1] Purchase fleets from a Trader World

        Order: ''')
    if action == '1':
        clear()
        src = input('''
        From which Trader World shall we issue a Purchase Order?
        World: ''')
        print('\n\tWhat class of ships shall we purchase from '+src+'?\n')
        getShipNames()
        ship = input('\n\t\tShip Class: ')
        qty = input('''
        How many of these ships shall we purchase?
        Number of Ships: ''')
        dest = input('''
        To which world shall we deploy this new Trade Union Fleet?
        World: ''')
        buyFleet(src, int(ship)-1, int(qty), dest)
        input('\nPress Enter to return to the Ministry menu...')
        refresh()
        ministryOfCommerce()
    else:
        clear()
        imperialMenu()


def ministryOfDiplomacy():
    clear()
    action = input('''
        The Imperial Ministry of Diplomacy
        ----------------------------------
        Available orders:

            [1] Transfer fleet to a non-Imperial world
            [2] Send a message to all Sovereigns

        Order: ''')
    if action == '1':
        clear()
        fleet = input('''
        What is the name of the Fleet to be transferred?
        It will be transferred to the world it is orbiting.
        Fleet: ''')
        transferFleet(fleet)
        input('\nPress Enter to return to the Ministry menu...')
        refresh()
        ministryOfDiplomacy()
    if action == '2':
        clear()
        msg = input('''
        What message shall we send to all the other Sovereigns?
        Message: ''')
        msgAllSovs(msg)
        input('\nPress Enter to return to the Ministry menu...')
        ministryOfDiplomacy()
    else:
        clear()
        imperialMenu()


def ministryOfIntelligence():
    clear()
    action = input('''
        The Imperial Ministry of Intelligence
        -------------------------------------
        Available orders:

            [1] Dismiss all notifications (coming soon)
            [2] Display a list of all active Sovereigns
            [3] Display the valid Rivals of our Empire

        Response: ''')
    if action == '1':
        clear()
        dismissAllMsg()
        input('\nPress Enter to return to the Ministry menu...')
        ministryOfIntelligence()
    if action == '2':
        clear()
        print('''
            Here is a list of all the Sovereigns in the Galaxy
            ordered on the basis of their relative [Imperial Mights]:
            ''')
        showAllSovs()
        input('\nPress Enter to return to the Ministry menu...')
        ministryOfIntelligence()
    if action == '3':
        clear()
        print('''
            Here are the Sovereigns between 50 % and 200 % of our [Imperial Might],
            which can be attacked without opposition from our people:

            Any marked with [!] are potential threats to the Empire.
            They are more powerful than us, but can attack us
            without opposition from their people.
            ''')
        showRivals()
        input('\nPress Enter to return to the Ministry menu...')
        ministryOfIntelligence()
    else:
        clear()
        imperialMenu()


imperialMenu()
