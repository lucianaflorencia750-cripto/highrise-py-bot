class config:
    # Basic configuration: If you are unsure how to obtain the Bot ID, simply start the bot and it will be logged in the console.
    prefix = '/'
    botID = 'c4a611d1f58978e4d2c8e37976b692ef954f8a5d4445b14936bdc54ba3339eb1'
    botName = 'botcitoflo'
    ownerName = '_florcitaa_'
    roomName = 'floor'
    coordinates = {
        'x': 8.5,
        'y': 0.6000,
        'z': 20.5,
        'facing': 'FrontRight'
    }


class loggers:
    # The following settings are related to events. Each event log can be enabled or disabled. Note that turning these off will not affect their usage in the game.
    SessionMetadata = True
    messages = True
    whispers = True
    joins = True
    leave = True
    tips = True
    emotes = False
    reactions = False
    userMovement = False


class messages:
    # The following are optional and serve as a basic usage example for calling messages and replacing variables.
    invalidPosition = "Your position could not be determined."
    invalidPlayer = "{user} is not in the room."
    invalidUser = "User {user} is not found."
    invalidUsage = "Usage: {prefix}{commandName}{args}"
    invalidUserFormat = "Invalid user format. Please use '@username'."


class permissions:
    # You can add as many IDs as you want, for example: ['id1', 'id2'].
    owners = ['_florcitaa_']
    moderators = ['_florcitaa_']


class authorization:
    # To obtain your token, visit https://highrise.game/ and log in. Then, go to the settings and create a new bot. Accept the terms and generate a token.
    # To obtain your room ID, go to the game and navigate to the top right corner where the player list is displayed. Click on "Share this room" and copy the ID.
    room = 'https://high.rs/world?id=6894bd39e3e4a405517cb530&ownedRoomId=68f1c9b2e43fb7e1ecba51db&invite_id=6a20ddfb69f947fef7d0af9c'
    token = 'c4a611d1f58978e4d2c8e37976b692ef954f8a5d4445b14936bdc54ba3339eb1'
