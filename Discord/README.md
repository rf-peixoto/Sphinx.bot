This is the implementation of **Sphinx.bot** for Discord. You can access the official server [here](https://discord.gg/m2vvU67qCg). Keep in mind that this is a beta version. **Sphinx.bot** will not be available for consultation at all times. Before suggesting any changes, check the [TODO](https://github.com/rf-peixoto/Sphinx.bot/blob/main/Discord/TODO.md) file.

To use this version, add it to a group, configure the file [tools.py](https://github.com/rf-peixoto/Sphinx.bot/blob/main/Discord/tools.py) and [mail_sender.py](https://github.com/rf-peixoto/Sphinx.bot/blob/main/Discord/mail_sender.py) . Then run [client.py](https://github.com/rf-peixoto/Sphinx.bot/blob/main/Discord/client.py).

## Commands

These are the commands available only to the developer, the personal profile informed in the settings:
```
.exclude            Manually delete a record.
.log                Saves all activities performed during the session.
.save               Save changes on the database itself.
```

The _.log_ command will generate a list with the following structure:

``` [DATE] [TIME] | [GUILD:CHANNEL] | [USER][USER ID] are looking for [QUERY] ```

The next are the public commands, available to all members of the server:

```
.ping               Check the Sphinx.bot connection.
.check [email]      Checks records related to [email]. If found, the reply will be sent on a DM.
.remove [email]     Send a verification message to the [email] to be removed.
.verify [token]     Checks whether the token is valid and removes an email previously used in the .remove option.

```
**DISCLAIMER:** To remain on the Discord server your profile must **1)** have an email registered on the platform, **2)** a profile photo and **3)** it does not have random names, sets of numbers and characters merged in order with no apparent meaning.
