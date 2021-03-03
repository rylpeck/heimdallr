from datetime import datetime
import os
import random
import asyncio
import subprocess
from subprocess import Popen

import discord
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

# client = discord.Client()
bot = commands.Bot(command_prefix='!')




@bot.event  # Login
async def on_ready():
    print(f'We have logged in as {bot.user}!')

    await bot.change_presence(activity=discord.Game(name="bot test"))

    # server details
    guild = discord.utils.get(bot.guilds, name=GUILD)
    print(
        f'{bot.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

# Commands section


class WTF(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None
        
    @commands.Cog.listener()
    async def on_ready(self):
        await self.bot.change_presence(activity=discord.Game(name="with Gulltoppr"))

        guild = discord.utils.get(self.bot.guilds, name=GUILD)
        
        print(
            #f'{self.bot.user} is connected to the following guild:\n'
            #f'{guild.name}(id: {guild.id})'
        )

        # Load in last kyl time
        try:
            with open("status.txt", mode='r') as file:
                self.serverstatus = file.read()
        except FileNotFoundError as e:
                file = open("kyl.txt", mode='w')
                file.close()
                
    @commands.command()
    async def greetings(self, ctx):
        await ctx.send('Greetings! I am Heimdallr, posessor of Gjallarhorn, Rider of Gulltoppr and controller of the bifrost')
        
    @commands.command()
    async def opentheland(self, ctx):

        if (self.serverstatus == 'down'):
            await ctx.send('I am opening the Bifrost, go forth!')
            
            p = Popen("startValheim.bat")
            with open("status.txt", mode = "w") as file:
                file.write("up")
            with open("status.txt", mode='r') as file:
                self.serverstatus = file.read()

            p.communicate()
        else:
            await ctx.send("The Bifrost is already open, go check")

    @commands.command()
    async def checkstatus(self, ctx):
        await ctx.send(self.serverstatus)

    @commands.command()
    async def killme(self, ctx):
        await ctx.send("https://tenor.com/view/tf2-spy-kill-me-meet-the-medic-gif-14709106")

    @commands.command()
    async def begone(self, ctx):
        await ctx.send("https://tenor.com/view/be-gone-thot-meme-thot-gif-15410781")

    @commands.command()
    async def fuckyou(self, ctx):
        await ctx.send("https://tenor.com/view/devil-may-cry-devil-may-cry5-dmc5-nero-nero-sparda-gif-13795288")
    
    @commands.command()
    async def smash(self, ctx):
        await ctx.send("https://tenor.com/view/one-for-all-united-states-of-smash-might-boku-no-gif-12014967")
    
    
    
    @commands.command()
    async def update(self, ctx):

        if (self.serverstatus == 'down'):
            await ctx.send("Changing the land to a better feel")
            p = Popen("Downloadit.bat")
            p.communicate()
        else:
            await ctx.send('Cannot change the land with friends inside!')
            
    

    @commands.command()
    async def closetheland(self, ctx):
        if (self.serverstatus == 'up'):
            await ctx.send('Closing the Door.')
            subprocess.call(["taskkill","/IM", "valheim_server.exe"])
            self.serverstatus = "down"
        else:
            await ctx.send('I cannot see the land.')


    @commands.command()
    async def hydra(self, ctx):
        """Check the status of our other one true god."""
        await ctx.send('Hydra is home')

@bot.event
async def on_ready():
    print('Logged in as {0} ({0.id})'.format(bot.user))
    print('------')
    serverup = 0

bot.add_cog(WTF(bot))

bot.run(TOKEN)
