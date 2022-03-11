
import discord, asyncio, logging, sys

from ritoBot import getChallenger
from keys import d_key

#creates log file in local directory of discords runtime
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

client = discord.Client()


#wait on stand by for any message to be sent
@client.event
async def on_message(message):

    #check if author of message is the current client aka this bot
    if message.author == client.user:
        return


    
    if message.content.startswith('!ally'):
        cleanFive = getChallenger()
        #if cleanFive is false that means function isnt working properly, this avoids runtime failures
        if cleanFive == False:
            print("Error grabbing Top 5 SoloQ players")
            await message.channel.send("Error grabbing Top 5 SoloQ players")
            return
        
        body = ""
        for key, value in cleanFive.items():
            #goes through leaderboard dict and formats into a string leaderboard to prepare to send in chat
            body += key + " " + str(value) + '\n'
    
        embed=discord.Embed(title="Top 5 SoloQ Players", url="https://tracker.gg/lol/leaderboards/stats/all/LeaguePoints?region=NA", description=body, color=0xFF5733)
        await message.channel.send(embed=embed)




client.run(d_key)
