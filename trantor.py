from anacreonlib import Anacreon
import pprint


########## GLOBALS ##########

GAME_ID = 4365595

# get login details from file, or create and save if first time running
open('login', 'a').close()
f = open('login', 'r')
login = f.read()
USERNAME = login.split(' ', 1)[0]
PASSWORD = login.split(' ', 1)[-1]
f.close()
if USERNAME == '' or PASSWORD == '':
    print('Login to Multiverse account')
    USERNAME = input('Username: ')
    PASSWORD = input('Password: ')
    f = open('login', 'w')
    f.write(USERNAME+' '+PASSWORD)
    f.close()

# setup the api handler
api = Anacreon(USERNAME, PASSWORD)
api.gameID = GAME_ID
gameList = api.get_game_list()
gameInfo = api.get_game_info()
api.sovID = gameInfo['userInfo']['sovereignID']
gameObjects = api.get_objects()
for attrib in gameInfo['sovereigns']:
    if attrib['id'] == api.sovID:
        empireName = attrib['name']

# write gameInfo and gameObjects to files for reference
f = open('gameInfo.txt', 'wb')
f.write(pprint.pformat(gameInfo).encode())
f.close()
f = open('gameObjects.txt', 'wb')
f.write(pprint.pformat(gameObjects).encode())
f.close()


########## CORE FUNCTIONS ##########


def refresh():
    '''
    Updates the gameInfo and gameObjects variables with latest data from API
    '''
    gameInfo = api.get_game_info()
    gameObjects = api.get_objects()


def getObjID(objName, objList):
    '''
    Returns an object's ID (int) given its 'objName' (str) and a reference 'objList' (list)
    Format of 'objList' is ['name_1',id_1,'name_2',id_2, ...]
    '''
    for i in range(0, len(objList)):
        if objList[i][0] == objName:
            return objList[i][1]


def getObjName(objID, objList):
    '''
    Returns an object's name (str) given its 'objID' (int) and a reference 'objList' (list)
    Format of 'objList' is ['name_1', id_1, 'name_2', id_2, ...]
    '''
    for i in range(0, len(objList)):
        if objList[i][1] == objID:
            return objList[i][0]


def getScenObj(returnType, objCategory):
    '''
    Returns Scenario Objects (list) belonging to 'objCategory' (str)
    'returnType' (str) specifies format of returned list: 'list','id' or 'name'
    'list' format: ['name_1', id_1, 'name_2', id_2, ...]
    'id' format: [id_1, id_2, ...]
    'name' format: ['name_1', 'name_2', ...]
    '''
    objList = []
    for attrib in gameInfo['scenarioInfo']:
        if 'category' in attrib and attrib['category'] == objCategory:
            if returnType == 'list':
                objList.append([attrib['nameDesc'], attrib['id']])
            elif returnType == 'id':
                objList.append(attrib['id'])
            elif returnType == 'name':
                if 'name' in attrib:
                    objList.append(attrib['name'])
                else:
                    objList.append(attrib['nameDesc'])
    return objList


def getSovList(returnType):
    '''
    Returns (list) of Sovereigns from gameInfo['sovereigns']
    'returnType' (str) specifies format of returned list: 'list','id' or 'name'
    'list' format: ['name_1', id_1, 'name_2', id_2, ...]
    'id' format: [id_1, id_2, ...]
    'name' format: ['name_1', 'name_2', ...]
    '''
    sovList = []
    for attrib in gameInfo['sovereigns']:
        if returnType == 'list':
            sovList.append([attrib['name'], attrib['id']])
        elif returnType == 'id':
            sovList.append(attrib['id'])
        elif returnType == 'name':
            sovList.append(attrib['name'])
    return sovList


def getGameObj(returnType, objClass, sov=None):
    '''
    Returns Game Objects as (list) or (dict) belonging to an 'objClass' (str)
    Optionally return only objects belonging to a Sovereign 'sov'
    'returnType' (str) specifies format of returned list: 'list','id' or 'name'
    'list' format: ['name_1', id_1, 'name_2', id_2, ...]
    'id' format: [id_1, id_2, ...]
    'name' format: ['name_1', 'name_2', ...]
    '''
    def populateData():
        if returnType == 'dict':
            objDict.update({objID: attrib})
        elif returnType == 'list':
            objList.append([attrib['name'], objID])
        elif returnType == 'id':
            objList.append(objID)
        elif returnType == 'name':
            objList.append(attrib['name'])
    objDict = {}
    objList = []
    for objID, attrib in gameObjects.items():
        if 'class' in attrib and attrib['class'] == objClass:
            if not sov == None:
                sovList = getSovList('list')
                if attrib['sovereignID'] == getObjID(sov, sovList):
                    populateData()
            else:
                populateData()
    if returnType == 'dict':
        return objDict
    else:
        return objList


########### UTILITY FUNCTIONS ##########


def getSovStat(stat, sov):
    '''
    Returns statistics (str) of a Sovereign
    'stat' specifies which stat to return: 'fleets','worlds' or 'population'
    '''
    sovData = getSovList('list')
    for attrib in gameInfo['sovereigns']:
        if attrib['id'] == getObjID(sov, sovData):
            return attrib['stats'][stat]


def getAvgEfficiency(sov):
    '''
    Returns the average efficiency (float) of all worlds belonging to 'sov' (str)
    '''
    totalEfficiency = 0
    for objID, attrib in getGameObj('dict', 'world', sov).items():
        totalEfficiency += attrib['efficiency']
    return totalEfficiency/getSovStat('worlds', sov)


def getShipNames():
    '''
    Return and print an alphabetically sorted (list) of ship names
    '''
    numShips = 0
    shipNames = getScenObj('name', 'maneuveringUnit')
    shipNames.sort()
    for ship in shipNames:
        numShips += 1
        print('\t\t['+str(numShips)+'] '+ship)
    return shipNames


########## MINISTRY OF WAR ORDERS ##########


def mergeFleets(world, mergedFleet, transfer):
    '''
    Consolidate all fleets over a 'world' (str) to a single 'mergedFleet' (str)
    Optionally 'transfer' (str) them to the world itself
    '''
    worldID = getObjID(world, getGameObj('list', 'world',))
    mergedFleetID = getObjID(mergedFleet, getGameObj('list', 'fleet',))
    fleetIDList = getGameObj('id', 'fleet', empireName)
    worldData = getGameObj('dict', 'world')
    for fleet in worldData.get(worldID).get('nearObjIDs'):
        if fleet in fleetIDList and not fleet == mergedFleetID:
            api.disband_fleet(fleet, mergedFleetID)
    if transfer == '1':
        api.disband_fleet(mergedFleetID, worldID)
        print('\n\tAll fleets in orbit transferred to '+world+'!')
    else:
        print('\n\tAll fleets in orbit of ' +
              world+' merged with '+mergedFleet+'!')


def reinforceWorld(desig, dest):
    '''
    Reinforce a 'dest' (str) world from all shipyards with designation 'desig' (str)
    User-input 'desig' is mapped to one of 'jumpship yards', 'starship yards' or 'ramjet yards'
    '''
    desigList = getScenObj('list', 'designation')
    worldData = getGameObj('dict', 'world', empireName).items()
    worldList = getGameObj('list', 'world')
    shipIDList = getScenObj('id', 'maneuveringUnit')
    deployFrom = []  # worlds to deploy from
    deployList = []  # ship ids to deploy in format ['name_1',id_1,'name_2',id_2,...]
    if desig == '1':
        desigID = getObjID('jumpship yards', desigList)
    if desig == '2':
        desigID = getObjID('starship yards', desigList)
    if desig == '3':
        desigID = getObjID('ramjet yards', desigList)
    destID = getObjID(dest, worldList)
    for objID, attrib in worldData:
        if attrib['designation'] == desigID:
            deployFrom.append(objID)
        for world in deployFrom:
            # format is [id_1,qty_1,id_2,qty_2,...]
            for ship in attrib['resources'][0::2]:
                if ship in shipIDList and not ship in deployList:
                    # lazily deploys max possible
                    deployList.extend([ship, 999999])
    numDeployed = 0
    for world in deployFrom:
        numDeployed += 1
        api.deploy_fleet(deployList, world)
        api.set_fleet_destination(api.most_recent_fleet(), destID)
        api.rename_object(api.most_recent_fleet(),
                          'Reinforcement Fleet '+str(numDeployed))
        print('\tFleet '+str(numDeployed) +
              ' deployed from '+getObjName(world, worldList))
    if numDeployed == 0:
        print('\n\tAn error has occurred! No fleets were deployed.')
    else:
        print('\n\tOrders for '+str(numDeployed) +
              ' fleets to reinforce '+dest+' relayed successfully!')


########## MINISTRY OF COMMERCE ORDERS ##########

# todo: display max qty available to buy
def buyFleet(src, ship, qty, dest):
    '''
    Purchase some qty (int) of ship (str) from a src (str) Mesophon world
    Deploy this new fleet to dest (str) world
    '''
    worldList = getGameObj('list', 'world')
    shipNames = getScenObj('name', 'maneuveringUnit')
    shipNames.sort()
    srcID = getObjID(src, worldList)
    shipID = getObjID(shipNames[ship], getScenObj('list', 'maneuveringUnit'))
    destID = getObjID(dest, worldList)
    api.buy_item(srcID, shipID, qty)
    print('\n\tTrade order to purchase '+str(qty) +
          ' '+shipNames[ship]+'s relayed successfully!')
    api.set_fleet_destination(api.most_recent_fleet(), destID)
    api.rename_object(api.most_recent_fleet(), 'Trade Union Fleet')
    print('\tTrade Union Fleet en route to '+dest+'.')


def importAllDemands(world):
    '''
    Set a trade hub 'world' (str) to import 100% of demand from each of its suppliers
    '''
    worldList = getGameObj('list', 'world', empireName)
    worldData = getGameObj('dict', 'world', empireName)
    worldID = getObjID(world, worldList)
    # 'imports' is a list in a dict in a list in a dict in a dict
    # format is [id1,%1,id2,%2,...]
    #for route in worldData.get(worldID).get('tradeRoutes'):
        #for i in range(0, route.get('imports')):
        

########## MINISTRY OF DIPLOMACY ORDERS ##########


def msgAllSovs(msg):
    '''
    Send a msg (str) to all Sovereigns
    '''
    sovIDList = getSovList('id')
    for sov in sovIDList:
        api.send_message(sov, msg)
    print('\n\tMessages successfully relayed to ' +
          str(len(sovIDList))+' sovereigns!')


def transferFleet(gift, fleet):
    '''
    Transfer a 'gift' (str) fleet to the world it orbits
    Optionally transfer to another 'fleet' (str) in orbit of the world
    '''
    fleetData = getGameObj('dict', 'fleet', empireName)
    fleetList = getGameObj('list', 'fleet')
    for objID, attrib in fleetData.items():
        if attrib['name'] == gift:
            giftID = objID
            if fleet == '1':
                destID = attrib['anchorObjID']
                api.disband_fleet(giftID, destID)
                print('\n\t'+gift+' successfully transferred to world!')
            else:
                # todo: add checks for same name: is the fleet orbiting the same world?
                destID = getObjID(fleet, fleetList)
                api.disband_fleet(giftID, destID)
                print('\n\t'+gift+' successfully transferred to '+fleet+'!')


########## MINISTRY OF INTELLIGENCE ORDERS ##########


def dismissAllMsg():
    '''
    Clears all messages and notifications from the game client
    '''
    history = api.history_dict
    for msgID in history:
        api.set_history_read(msgID)
    return 0


def showAllSovs():
    '''
    Return and print sorted (list) of all Sovereigns in the game
    '''
    sovList = []
    for attrib in gameInfo['sovereigns']:
        if not attrib['id'] == api.sovID:
            sovList.append([attrib['name'], attrib['imperialMight']])
    sovList = sorted(sovList, key=lambda x: x[1], reverse=True)
    numSovs = 0
    for i in range(0, len(sovList)):
        numSovs += 1
        print('\t\t'+str(numSovs)+'. ' +
              sovList[i][0]+' ['+str(sovList[i][1])+']')
    return sovList


def showRivals():
    '''
    Return and print sorted (list) of all empire Rivals,
    defined as Sovereigns with 50 < imperialMight < 200
    '''
    sovList = []
    for attrib in gameInfo['sovereigns']:
        if not attrib['id'] == api.sovID:
            if attrib['imperialMight'] > 50 and attrib['imperialMight'] < 200:
                if attrib['imperialMight'] > 100:
                    sovList.append(
                        ['[!] '+attrib['name'], attrib['imperialMight']])
                else:
                    sovList.append([attrib['name'], attrib['imperialMight']])
    sovList = sorted(sovList, key=lambda x: x[1], reverse=True)
    numRivals = 0
    for i in range(0, len(sovList)):
        numRivals += 1
        print('\t\t'+str(numRivals)+'. ' +
              sovList[i][0]+' ['+str(sovList[i][1])+']')
    return sovList
