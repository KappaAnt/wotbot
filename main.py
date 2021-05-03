import discord
import os
from discord.ext import commands
from api1 import WotFact
from api2 import WotFact2

def Command():
    client = commands.Bot(command_prefix = '.')
    numberID = 0
    Hits = 0
    @client.event
    async def on_ready():
        print("\nBot is ready")

    @client.event
    async def on_member_join(member):
        print(f" {member} has joined the server.")
        
    @client.event
    async def on_member_remove(member):
        print(f" {member} has left the server.")
        
    @client.command(aliases=["ARTY","Arty","tank"])
    async def arty(ctx):
        await ctx.send('Enter your WOT username: ')
        msg = await client.wait_for('message', check=lambda msg: msg.author == ctx.author)
        username = str(msg.content)
        
        nameID = WotFact(username)
        numberID = nameID.get()
        ID = numberID
        #await ctx.send("ID: " + ID)
        artyHit = WotFact2(numberID)
        Hits = artyHit.get()
        await ctx.send("Hit By Arty: " + str(Hits) + " times!")






              
    client.run(os.environ["DISCORD_TOKEN"])
    
def main():
    #nameID = WotFact("Kappa_Ant")
    #numberID = nameID.get()

    #artyHit = WotFact2(numberID)
    #artyHit.get()
    Command()
    
main()

    
    
