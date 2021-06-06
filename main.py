import os
from discord.ext import commands
import joke as getJoke
import createEmbed
import createAscii

from dotenv import load_dotenv
load_dotenv()
token = os.environ['Token']


bot=commands.Bot(command_prefix= '$')

text_channel_list = {}
for guild in bot.guilds:
    for channel in guild.channels:
        if str(channel.type) == 'text':
            text_channel_list[guild]=guild.get_all_channels()

@bot.command()
async def ping(ctx,arg):
    await ctx.send("pong")
    await ctx.send(arg)

@bot.command()
async def test(ctx, arg):
    await ctx.send(arg)

@bot.command(aliases=['meme','funny'])
async def joke(ctx,*args):
    if(len(args)==0):
        category="misc"
    else:
        category=args[0]
    embed=createEmbed.makeEmbed(category,getJoke.get(category))
    await ctx.send(embed=embed)

@bot.command()
async def ascii(ctx,*arg):
    await ctx.send("```"+createAscii.get(arg)+"```")

@bot.event
async def on_ready():
    def gen():
        for guild in bot.guilds:
            for channel in guild.channels:
                yield channel

    for item in gen():
        print(item)

@bot.event
async def on_member_join(member):
    print("f{member} has joined")
    


bot.run(token)
