import discord

def makeEmbed(*args):
    embed = discord.Embed(title=args[0], description=args[1],color=discord.Color.blue()) 
    # embed.add_field(name="Name", value="you can make as much as fields you like to")
    # embed.set_footer(name="footer") #if you like to
    return embed
    