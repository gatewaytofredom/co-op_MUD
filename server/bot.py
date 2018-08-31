import discord
from discord.ext import commands
from threading import Thread
import asyncio
import random

with open("token.txt") as t:
    TOKEN = t.read()

bot = commands.Bot(command_prefix="$")

discord.Channel

class Bot:
    def __init__(self, client):
        self.client = client
        self.regroup_data = None
        self.channels = {}
        self.persons = {}
        self.server = None

    async def on_message(self, message):
        if message.author == self.client.user:
            return
        if message.content.startswith("!ping"):
            msg = "I live to serve you, {}.".format(message.author.mention)
            await self.client.send_message(message.channel, msg)

        if "@someone" in message.content:
            online_members = [m for m in message.server.members 
                if m.status == discord.Status.online]
            msg = "R-r-r-r-r-randomly chose {0.mention}".format(
                random.choice(online_members)
            )
            await self.client.send_message(message.channel, msg)

        if message.content.startswith("$mud setup"):
            self.server = message.server

        if message.content.startswith("$mud end"):
            for channel in self.channels.values():
                await self.client.delete_channel(channel)

    #update loop for regroup checking
    #much faster than running new task with wait_until_ready()
    #for each event
    async def background_loop(self):
        await self.client.wait_until_ready()
        while not self.client.is_closed:
            if (
                self.regroup_data is not None 
                and self.server is not None
            ):
                await self.async_regroup(self.regroup_data)
                self.regroup_data = None
            await asyncio.sleep(0.1)

    def regroup(self, groups):
        self.regroup_data = groups

    '''
    Regroups chats
    groups - dictionary of players to move
    '''
    #This code is awful. Please re-write it.
    async def async_regroup(self, groups):
        voice_members = [m for m in self.server.members
            if m.voice.voice_channel is not None]
        
        #list of channels that need to be deleted (empty)
        delete_channels = []

        #move users to appropriate rooms
        for key, users in groups.items():
            for user in users:
                member = self.find_member(user, voice_members)

                if member is None:
                    continue

                #create channel for key if DNE
                if key not in self.channels.keys():
                    self.channels[key] = await self.client.create_channel(
                        self.server,
                        "MUD Server",
                        type=discord.ChannelType.voice
                    )

                old_channel = self.get_old_channel(member)

                #add persons property to channel if DNE (because voice_members is broken)
                if self.channels[key].id not in self.persons.keys():
                    self.persons[self.channels[key].id] = 1
                else:
                    self.persons[self.channels[key].id] += 1


                #delete old room if necessary
                if old_channel is not None:
                    self.persons[old_channel.id] -= 1
                    if self.persons[old_channel.id] == 0:
                        delete_channels.append(old_channel)

                #move user
                await self.client.move_member(member, self.channels[key])

        #remove any empty rooms
        for channel in delete_channels:
            await self.client.delete_channel(channel)
        #remove from channels dict
        self.channels = {k:v for k, v in self.channels.items()
            if v not in delete_channels}

    #find member from list using userid and numbers
    def find_member(self, user, members):
        for member in members:
            if user == str(member):
                return member
        return None

    #find old channel in self.channels
    def get_old_channel(self, member):
        for channel in self.channels.values():
            if member.voice.voice_channel.id == channel.id:
                return channel
        return None

def start(mud_bot):
    bot.add_cog(mud_bot)
    bot.loop.create_task(mud_bot.background_loop())
    t = Thread(target=bot.run, args=(TOKEN,))
    t.daemon = True
    t.start()

def create_bot():
    return Bot(bot)

if __name__ == "__main__":
    mud_bot = create_bot()
    start(mud_bot)