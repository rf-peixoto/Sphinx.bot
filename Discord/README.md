This is the implementation of **Sphinx.bot** for Discord. You can access the official server [here](https://discord.gg/m2vvU67qCg). Keep in mind that this is a beta version. **Sphinx.bot** will not be available for consultation at all times. Before suggesting any changes, check the [TODO](https://github.com/rf-peixoto/Sphinx.bot/blob/main/Discord/TODO.md) file.

To use this version, add it to a group, configure the file [utils.py](https://github.com/rf-peixoto/Sphinx.bot/blob/main/Discord/utils.py) and [mail_sender.py](https://github.com/rf-peixoto/Sphinx.bot/blob/main/Discord/mail_sender.py) . Then run [client.py](https://github.com/rf-peixoto/Sphinx.bot/blob/main/Discord/client.py).

## Commands

These are the commands available only to the developer, the personal profile informed in the settings:
```
.dump               Starts the database, once Sphinx.bot is online.
.log                Saves all activities performed during the session.
```

The _.log_ command will generate a list with the following structure:

``` [DATE] | [TIME] | [GUILD:CHANNEL] | [USER][USER ID] are looking for [QUERY] | [RESULT] ```

To facilitate further analysis, the last parameter **[RESULT]** will return **0** if the query is successful and **1** if the record has not been found. The next are the public commands, available to all members of the server:
```
.ping               Check the Sphinx.bot connection.
.size               Checks the current number of emails in the database.
.check [email]      Checks records related to [email]. If found, the reply will be sent on a DM.
.remove [email]     Send a verification message to the [email] to be removed.
.verify [token]     Checks whether the token is valid and removes an email previously used in the .remove option.

```
