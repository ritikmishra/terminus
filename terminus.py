from trantor import *
import os


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


clear()

print("""
            ----------------------------------------------------
                             TERMINUS (Alpha I)
                        An extension for Anacreon 3
            By Imperator (anacreonlib framework by Ritik Mishra)
            ----------------------------------------------------
    """)


def imperialMenu():
    print("""
    Welcome, Dread Sovereign.
    The """+empireName+""" consists of """+str(getSovStat('worlds', empireName))+""" worlds with a total population of """+str(int(getSovStat('population', empireName)/1000))+""" billion.
    The average efficiency of the Empire is """+str(int(getAvgEfficiency(empireName)))+""" % and its military force consists of """+str(getSovStat('fleets', empireName))+""" fleets.
    """)

    action = input("""
    The Ministries in service to the Imperial Throne are:

        [1] The Ministry of War
        [2] The Ministry of Commerce
        [3] The Ministry of Diplomacy
        [4] The Ministry of Intelligence

    (Input the number corresponding to the desired action, or any other value to exit)

    Awaiting command: """)

    if action == '1':
        ministryOfWar()
    elif action == '2':
        ministryOfCommerce()
    elif action == '3':
        ministryOfDiplomacy()
    elif action == '4':
        ministryOfIntelligence()
    else:
        clear()
        exit()


def ministryOfWar():
    clear()
    action = input("""
        The Imperial Ministry of War
        ----------------------------

        Available orders:

            [1] Consolidate all fleets over a world
            [2] Reinforce a world with fleets from shipyards
            [3] Deploy a fleet with standing orders (coming soon)

        Order: """)
    if action == '1':
        refresh()
        clear()
        world = input("""
        Over which world shall we merge all orbiting fleets?
        World: """)
        mergeFleet = input("""
        To which fleet over """+world+""" shall we merge all the others?
        Fleet: """)
        transfer = input("""
        Shall we also send the newly combined fleet down to """+world+"""?
            [1] Yes
            [2] No
        Response: """)
        print('\n\tFleet orders are being relayed. Please wait...\n')
        try:
            mergeFleets(world, mergeFleet, transfer)
        except (NameError, ValueError):
            input("""
            ERROR: Unable to locate object with that name!
            Press Enter to continue...""")
            ministryOfWar()
        input('\nPress Enter to return to the Ministry menu...')
        ministryOfWar()
    elif action == '2':
        refresh()
        clear()
        desig = input("""
        From which of our shipyards shall we deploy reinforcements?
            [1] Jumpship yards
            [2] Starship yards
            [3] Ramjet yards
        Shipyard: """)
        dest = input("""
        To which world shall we deploy reinforcements?
        World: """)
        print('\n\tFleet orders are being relayed. Please wait...\n')
        try:
            reinforceWorld(desig, dest)
        except (NameError, ValueError):
            input("""
            ERROR: Unable to locate object with that name!
            Press Enter to continue...""")
            ministryOfWar()
        input('\nPress Enter to return to the Ministry menu...')
        ministryOfWar()
    elif action == '3':
        refresh()
        clear()
        input('\nPress Enter to return to the Ministry menu...')

        ministryOfWar()
    else:
        clear()
        imperialMenu()


def ministryOfCommerce():
    clear()
    action = input("""
        The Imperial Ministry of Commerce
        ---------------------------------

        Available orders:

            [1] Purchase fleets from a Trader World
            [2] Create trade routes which import 100% of demand (coming soon)
            [3] Build spaceports on all Imperial worlds

        Order: """)
    if action == '1':
        refresh()
        clear()
        src = input("""
        From which Trader World shall we issue a Purchase Order?
        World: """)
        print("""
        What class of ships shall we purchase from """+src+"""?
        (The Empire has """+str(getFunds())+""" aes funds in reserve)
        """)
        getShipsForSale()
        ship = input('\n\tShip Class: ')
        qty = input("""
        How many of these ships shall we purchase?
        Number of Ships: """)
        dest = input("""
        To which world shall we deploy this new Trade Union Fleet?
        World: """)
        try:
            buyFleet(src, int(ship)-1, int(qty), dest)
        except (NameError, ValueError):
            input("""
            ERROR: Unable to locate object with that name!
            Press Enter to continue...""")
            ministryOfCommerce()
        input('\nPress Enter to return to the Ministry menu...')
        ministryOfCommerce()
    if action == '2':
        refresh()
        clear()
        input('\nPress Enter to return to the Ministry menu...')
        ministryOfCommerce()
    if action == '3':
        refresh()
        clear()
        print('\tRelaying construction orders. Please wait...\n')
        buildSpaceports()
        input('\nPress Enter to return to the Ministry menu...')
        ministryOfCommerce()
    else:
        clear()
        imperialMenu()


def ministryOfDiplomacy():
    clear()
    action = input("""
        The Imperial Ministry of Diplomacy
        ----------------------------------

        Available orders:

            [1] Transfer fleet to a non-Imperial world or fleet
            [2] Dispatch diplomatic envoys to all Sovereign Capitals
            [3] Send a message to all Sovereigns

        Order: """)
    if action == '1':
        refresh()
        clear()
        gift = input("""
        What is the name of the Fleet to be transferred?
        Fleet: """)
        fleet = input("""
        Where shall we transfer this fleet?
            [1] The world it is orbiting
            [2] Another fleet (input its name below)
        Response: """)
        print('\n\tFleet orders are being relayed. Please wait...\n')
        try:
            transferFleet(gift, fleet)
        except (NameError, ValueError):
            input("""
            ERROR: Unable to locate object with that name!
            Press Enter to continue...""")
        input('\nPress Enter to return to the Ministry menu...')
        ministryOfDiplomacy()
    elif action == '2':
        refresh()
        clear()
        src = input("""
        From which world shall we dispatch envoys?
        World: """)
        qty = input("""
        How many explorer vessels shall we assign to each envoy fleet from """+src+"""?
        Number: """)
        print('\n\tFleet orders are being relayed. Please wait...\n')
        try:
            sendDiplomats(src, int(qty))
        except (NameError, ValueError):
            input("""
            ERROR: Unable to locate object with that name!
            Press Enter to continue...""")
        input('\nPress Enter to return to the Ministry menu...')
        ministryOfDiplomacy()
    elif action == '3':
        refresh()
        clear()
        msg = input("""
        What message shall we send to all the other Sovereigns?
        Message: """)
        msgAllSovs(msg)
        input('\nPress Enter to return to the Ministry menu...')
        ministryOfDiplomacy()
    else:
        clear()
        imperialMenu()


def ministryOfIntelligence():
    clear()
    action = input("""
        The Imperial Ministry of Intelligence
        -------------------------------------

        Available orders:

            [1] Dismiss all notifications
            [2] Display a list of all active Sovereigns
            [3] Display the valid Rivals of our Empire

        Order: """)
    if action == '1':
        refresh()
        clear()
        dismissAllMsg()
        print('\n\t All messages and notifications dismissed.')
        input('\nPress Enter to return to the Ministry menu...')
        ministryOfIntelligence()
    elif action == '2':
        refresh()
        clear()
        print("""
            Here is a list of all the Sovereigns in the Galaxy
            ordered on the basis of their relative [Imperial Mights]:
            """)
        showAllSovs()
        input('\nPress Enter to return to the Ministry menu...')
        ministryOfIntelligence()
    elif action == '3':
        refresh()
        clear()
        print("""
            Here are the Sovereigns between 50 % and 200 % of our [Imperial Might],
            which can be attacked without opposition from our people:

            Any marked with [!] are potential threats to the Empire.
            They are more powerful than us, but can attack us
            without opposition from their people.
            """)
        showRivals()
        input('\nPress Enter to return to the Ministry menu...')
        ministryOfIntelligence()
    else:
        clear()
        imperialMenu()


imperialMenu()
