This is the implementation of **Sphinx.bot** for Discord. You can access the official server [here](https://discord.gg/m2vvU67qCg). Keep in mind that this is a beta version. Sphinx.bot will not be available for consultation at all times. Before suggesting any changes, check the TODO file.

To use this version, add it to a group, configure the file [utils.py](https://github.com/rf-peixoto/Sphinx.bot/blob/main/Discord/utils.py) and run [client.py](https://github.com/rf-peixoto/Sphinx.bot/blob/main/Discord/client.py).

## Commands

These are the commands available only to the developer, the personal profile informed in the settings:
```
.dump       Starts the database, once Sphinx.bot is online.
.remove     Command not yet implemented.
.log        Saves all activities performed during the session.
```

These are the public commands, available to all members of the server:
```
.ping               Check the Sphinx.bot connection.
.check [email]      Checks records related to [email]. If found, the reply will be sent on a DM.
.size               Checks the current number of emails in the database.
```
