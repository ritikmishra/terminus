# Terminus #

Project Terminus is a command-line based extension written in Python for [Anacreon 3](https://anacreon.kronosaur.com), which is an online [4X](https://en.wikipedia.org/wiki/4X) game produced by [Kronosaur Productions, LLC.](http://kronosaur.com/)

The aim of this project is to provide a user-friendly front-end interface for using pre-packaged scripts that make use of the Anacreon API, to automate some micromanagement aspects of the game, as well as providing some additional features not present in the vanilla game client.

This project is currently in an Alpha state. Please report bugs on the [Issues](https://github.com/RexImperator/terminus/issues) page, and note that additional scripts will be added in the future. Participate in discussion of this project on the [Kronosaur Forums](https://forums.kronosaur.com/viewforum.php?f=48).

## Installation ##

1. Download and install [Python 3.7.0](https://www.python.org/downloads/). During installation, ensure that the option to "Add Python 3.7.0 to PATH" is checked.

2. Open a terminal session (Command Prompt or PowerShell on Windows, Terminal on OS X or similar). Input: ```python -V```. The response should be: ```Python 3.7.0```. If not, Python was not installed correctly.

3. Input: ```python -m pip install requests```. This will install the "requests" module, required for anacreonlib functionality.

4. Download this repository and save it to an easily accessible directory on your machine (e.g. ```Desktop/terminus```)

5. Download the [anacreonlib](https://github.com/ritikmishra/anacreonlib) repository and save it to the Terminus directory (e.g. ```Desktop/terminus/anacreonlib```)

6. Input: ```python Desktop/terminus/terminus.py```.

## Notes ##

1. It is assumed that the user is playing on the latest Anacreon Beta game. At time of writing, this is the "Fallen Worlds: Era 4" scenario.

2. In the project's Alpha state, it is assumed that the user inputs valid commands. For example: if a world name is inputted, and no such world exists, Terminus will crash.

3. It is assumed that the user does not use the scripts provided with malicious intent.

## Features ##

### Main Menu ###

The user is prompted to login once to their Multiverse account, after which their username and password is stored on a plaintext file to use with future logins. If login is successful, the main menu reports some statistics about their Empire, along with options to navigate to the following submenus:

### Ministry of War ###

**1. Consolidate all fleets over a world:** Transfers all fleets belonging to the player to a single one. Optionally, also transfer this merged fleet down to the world the individual fleets were previously orbiting.

**2. Reinforce a world with fleets from shipyards:** Deploy all units from each one of either: jumpship yards, starship yards or ramjet yards belonging to the player. Send each of these reinforcement fleets to a designated world.

### Ministry of Commerce ###

**1. Purchase fleets from a Trader World:** Purhase any number of ships of any class from a Mesophon Traders Union and deploy this new fleet to a designated world.

**2. Set trade routes to import 100% of demand:** Set all import trade routes for a world or trade hub to be 100% of demand, importing the maximum possible amount for each supplier world.

### Ministry of Diplomacy ###

**1. Transfer fleet to a non-Imperial world or fleet:** Transfer a fleet to the world it orbits, even if the world belongs to another sovereign or is independent (i.e. a mechanism for "gifting" units to other players). Optionally, transfer this fleet to another non-Imperial fleet orbiting the same world.

**2. Send a message to all Sovereigns:** Relays a message from the player to all other players. At time of writing, the API limits this action to 120 calls per hour. Please use responsibly.

### Ministry of Intelligence ###

**1. Dismiss all notifications:** Clears all messages and notifications from the game client screen.

**2. Display a list of all active Sovereigns:** Print a list of all other players present in the game, sorted by relative Imperial Might, regardless if their capital has been discovered.
    
**3. Display the valid Rivals of our Empire:** Print a sorted list of all players within 50% and 200% of the player's Imperial Might. Sovereigns with equal or greater Imperial Might are indicated with a warning icon.

### Acknowledgement ###

["anacreonlib"](https://github.com/ritikmishra/anacreonlib) by [Ritik Mishra](https://github.com/ritikmishra) is used as a framework to make API calls.
