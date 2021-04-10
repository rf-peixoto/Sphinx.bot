# Dependencies:
from datetime import datetime
from mail_sender import MailSender
from manager import Manager
from tools import Tools
import discord
import secrets

# ---------------------------------------------------------------------------- #
# Log:
log = []
# Discord CLient:
client = discord.Client()
# Tools
tools = Tools()
# Database Manager:
manager = Manager()
# Mail Sender:
mail_sender = MailSender()
# Verification Tokens:
tokens = {}
# ---------------------------------------------------------------------------- #
# On Start:
@client.event
async def on_read():
    print("Starting as {0}.".format(client.user))
# ---------------------------------------------------------------------------- #
# On Message:
@client.event
async def on_message(message):
    # Time:
    time = datetime.now()
    time_string = "{1}/{0}/{2} {3}:{4}".format(time.day, time.month, time.year, time.hour, time.minute)

    # Ignore Bots:
    if message.author == client.user or message.author.bot:
        return

    # Ignore DM:
    if str(message.channel.type) == "private":
        await message.channel.trigger_typing()
        await message.channel.send("Searching on private channels is not allowed.")
        return
# ---------------------------------------------------------------------------- #
    # Owner Messages:
    if str(message.author.id) == tools.owner_id:
        # Manual Exclusion
        if message.content.startswith(".exclude"):
            await message.delete()
            await message.channel.trigger_typing()
            email = tools.sanitize(message.content.split(".exclude ")[-1]).lower()
            try:
                manager.remove(email)
                log.append(time_string + " | The address {0} has been successfully removed from the system by an admin.".format(email))
                print(log[-1])
                await message.channel.send("The address has been successfully removed.")
                return
            except Exception as error:
                print(error)
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

        # Save Changes on Database:
        if message.content.startswith(".commit"):
            await message.delete()
            try:
                manager.save_changes()
                print("The database was saved.")
            except Exception as error:
                print("An error ocurred while saving changes on database: {0}".format(error))
            return
# ---------------------------------------------------------------------------- #
    # Ping:
    if message.content.startswith(".ping"):
        delay = client.latency
        await message.add_reaction("\u2611")
        await message.channel.send("**Latency:**: {0}".format(delay))
        return

    # Check Account:
    if message.content.startswith(".check"):
        tmp = tools.sanitize(message.content.split(".check ")[-1]).lower()
        if not tools.check_string(tmp):
            await message.channel.send("I was unable to recognize this address. Check your email or contact support.")
            return
        tmp_string = time_string + " | " + "[{0}:{1}]".format(message.guild.name, message.channel.name) + " | " + message.author.name + "[{0}]".format(message.author.id) + " are looking for " + tmp
        if tools.check_string(tmp):
            # Check in DB:
            try:
                value = manager.get_data(tmp)
                if value:
                    await message.delete()
                    await message.author.send("```{0}:{1}```".format(tmp, value))
                    log.append(tmp_string)
                    print(log[-1])
                else:
                    await message.delete()
                    await message.channel.send("This address is not in my database.")
                    log.append(tmp_string)
                    print(log[-1])
            except Exception as error:
                await message.delete()
                await message.channel.send("There was an error in the search, check the history of operations.")
                print(error)
        else:
            await message.delete()
            await message.channel.send("I couldn't verify this address. Please check your message and try again.")
        return

    # Send Removal Token:
    if message.content.startswith(".remove "):
        await message.delete()
        await message.channel.trigger_typing()
        tmp = tools.sanitize(message.content.split(".remove ")[-1]).lower()
        if not tools.check_string(tmp):
            await message.channel.send("I was unable to recognize this address. Check your email or contact support.")
            return
        await message.channel.send("You will receive a token for removing this email in the next few minutes. Check your spam box and follow the instructions.")
        this_email_token = tools.sanitize(secrets.token_urlsafe(8))
        tokens.update({this_email_token:tmp})
        try:
            mail_sender.send_email(tmp, this_email_token)
        except Exception as error:
            await message.channel.send("There was an error while trying to remove this address. Check the history of operations.")
            print(error)
        return

    # Remove Account With Token:
    if message.content.startswith(".verify "):
        tmp = tools.sanitize(message.content.split(".verify ")[-1])
        await message.channel.trigger_typing()
        if tmp in tokens.keys():
            try:
                address = tokens.pop(tmp)
                manager.remove(address)
                log.append("{0} | The address {1} has been removed.".format(time_string, address))
                print(log[-1])
                await message.add_reaction('\u2611')
                await message.channel.send("The address has been successfully removed.")
            except Exception as error:
                await message.channel.send("There was an error while trying to remove this address. Check the history of operations.")
                print(error)
        else:
            await message.channel.send("I was unable to recognize this token. Check your email or contact support.")
        return
# ---------------------------------------------------------------------------- #
# Run:
client.run(tools.bot_token)
