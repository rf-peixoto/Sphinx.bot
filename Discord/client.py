# Dependences:
from datetime import datetime
from mail_sender import MailSender
from manager import Manager
from utils import Utils
import discord
import secrets

#--------------------------------------------------#
# Log
log = []
# Setup:
client = discord.Client()
# Util:
util = Utils()
# DB Manager:
manager = Manager()
# Mail Sender:
mail_sender = MailSender()
# Removal Tokens:
tokens = {}
#--------------------------------------------------#
# On Start:
@client.event
async def on_read():
    print("Starting as {0}.".format(client.user))

#--------------------------------------------------#
# On Message:
@client.event
async def on_message(message):
    # Time of the Message:
    time = datetime.now()
    time_string = "{1}/{0}/{2} | {3}:{4}".format(time.day, time.month, time.year, time.hour, time.minute)

    # Ignore Bots as Authors:
    if message.author == client.user or message.author.bot:
        return

    # Ignore DM:
    if str(message.channel.type) == "private":
        await message.channel.trigger_typing()
        await message.channel.send("Searching on private channels is not allowed.")
        return

    # Owner Messages:
    if str(message.author.id) == util.owner_id:
        # Initialize Database:
        if message.content.startswith(".dump"):
            await message.channel.send("Updating database. This may take some time.")
            await message.channel.trigger_typing()
            try:
                manager.dump()
                await message.add_reaction('\u2611')
                await message.channel.send("Records have been updated.")
                log.append("{0} - Update complete..".format(time_string))
            except Exception as error:
                print(error)
                await message.channel.send("There was an error in the operation. Check the log for more details.")
            return

        # Save log:
        if message.content.startswith(".log"):
            # Time of the Message:
            time = datetime.now()
            filename = "LOG_{1}_{0}_{2}_{3}_{4}.txt".format(time.day, time.month, time.year, time.hour, time.minute)
            await message.channel.trigger_typing()
            with open(filename, "w") as fl:
                for entry in log:
                    fl.write(entry + "\n")
                fl.close()
            log.clear()
            await message.add_reaction("\u2611")
            await message.channel.send("The activity history has been successfully exported.")
            return

#--------------------------------------------------#
    # Ping:
    if message.content.startswith(".ping"):
        delay = client.latency
        await message.add_reaction("\u2611")
        await message.channel.send("**Latency:**: {0}".format(delay))
        return

    # Check Account:
    if message.content.startswith(".check"):
        tmp = util.sanitize(message.content.split(".check ")[-1]).lower()
        tmp_string = time_string + " | " + "[{0}:{1}]".format(message.guild.name, message.channel.name) + " | " + message.author.name + "[{0}]".format(message.author.id) + " are looking for " + tmp
        if util.check_string(tmp):
            # Check in DB:
            try:
                value = manager.get_data(tmp)
                if value:
                    await message.delete()
                    await message.author.send("```{0}:{1}```".format(tmp, value))
                    log.append(tmp_string + " | 0")
                    print(tmp_string + " | 0")
                else:
                    await message.delete()
                    await message.channel.send("This address is not in my database.")
                    log.append(tmp_string + " | 1")
                    print(tmp_string + " | 1")
            except Exception as error:
                await message.channel.send("There was an error in the search, check the history of operations.")
        else:
            await message.channel.send("I couldn't verify this address. Please check your message and try again.")
        return

    # Send Removal Token:
    if message.content.startswith(".remove"):
        await message.delete()
        await message.channel.trigger_typing()
        try:
            tmp = util.sanitize(message.content.split(".remove ")[-1]).lower()
            this_email_token = util.sanitize(secrets.token_urlsafe(8))
            await message.channel.send("You will receive a token for removing this email in the next few minutes. Check your spam box and follow the instructions.")
            tokens.update({this_email_token:tmp})
            mail_sender.send_email(tmp, this_email_token)                
        except Exception as error:
            print(error)
            await message.channel.send("There was an error while trying to remove this address. Check the history of operations.")
        return

    # Remove Account With Token:
    if message.content.startswith(".verify "):
        tmp = util.sanitize(message.content.split(".verify ")[-1])
        await message.channel.trigger_typing()
        if tmp in tokens.keys():
            try:
                address = tokens.pop(tmp)
                manager.users.update({address:"[REMOVED]"})
                log.append("{0} - The address {1} has been removed.".format(time_string, address))
                print(log[-1])
                await message.add_reaction('\u2611')
                await message.channel.send("The address has been successfully removed.")
            except Exception as error:
                await message.channel.send("There was an error while trying to remove this address. Check the history of operations.")
                print(error)
        else:
            await message.channel.send("I was unable to recognize this token. Check your email or contact support.")
        return

    # Get DB Size:
    if message.content.startswith(".size"):
        await message.channel.trigger_typing()
        tmp = str(manager.get_lenght())
        await message.channel.send("The database has {0} records.".format(tmp))
        await message.add_reaction('\u2611')
        return


#--------------------------------------------------#
# Exec:
client.run(util.bot_token)
