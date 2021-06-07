from os import name
import credential
from discord.ext import commands
import joke as getJoke
import createEmbed
import createAscii
import asyncpraw
import random

reddit = asyncpraw.Reddit(
    client_id=credential.client_id,
    client_secret=credential.client_secret,
    user_agent="discordBot",
)
bot=commands.Bot(command_prefix= '$')



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
    pass


@bot.command()
async def get(ctx,*args):
    try:
        subreddit= await reddit.subreddit(args[0])
        print(dir(subreddit))
        await ctx.send([post async for post in subreddit.random_rising(limit=1)][0].url)
    except:
        await ctx.send("Not a subreddit 🤕")


bot.run(credential.Token)
