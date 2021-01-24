def botMainCode(prefix="!"):
    mainCode =f'''
import discord
from discord.ext import commands

intents = discord.Intents(messages=True, guilds=True,
         reactions=True, members=True, presences=True)
Bot = commands.Bot(command_prefix="{prefix}", intents=intents)


@Bot.event
async def on_ready():
    print("Ben bir botum ve çalışmaya hazırım.")
'''
    return mainCode

def joinCode(message="Sunucumuza Hoşgeldiniz",kanalBilgisi="Bilgi Verilmedi."):
    join = f"""
@Bot.event
async def on_member_join(member):
    channel = discord.utils.get(
        member.guild.text_channels, name="{kanalBilgisi}")"""+"""
    await channel.send(f"{member}"""+f""" {message}")
        """
    return join

def remove(message="Sunucumuzdan Ayrıldı.",kanalBilgisi="Bilgi Verilmedi."):
    remove = f"""
@Bot.event
async def on_member_remove(member):
    channel = discord.utils.get(
        member.guild.text_channels, name="{kanalBilgisi}")"""+"""
    await channel.send(f"{member}"""+f""" {message}")"""
    return remove

def clear(amount=5,role="Yok"):
    if role == "Yok":
        clearCode =f"""
@Bot.command()
async def clear(ctx, amount={amount}):
    await ctx.channel.purge(limit=amount)"""
        return clearCode
    else :
        clearCode =f"""
@Bot.command()
@commands.has_any_role("{role}")
async def clear(ctx, amount={amount}):
    await ctx.channel.purge(limit=amount)"""
        return clearCode

def clones(aliases="copy",role="Yok"):
    if role == "Yok":
       cloneCode = f'''
@Bot.command(aliases=["{aliases}"])
async def clone_channel(ctx):
    await ctx.channel.clone()
    '''
    else :
        cloneCode = f"""
@Bot.command(aliases=["{aliases}"])
@commands.has_any_role("{role}")
async def clone_channel(ctx):
    await ctx.channel.clone()"""
    
    return cloneCode

def kick(message="Yok",role="Yok"):
    if role == "Yok":
        kickCode =f"""
@Bot.command()
async def kick(ctx, member: discord.Member, *args, reason="{message}"):
    await member.kick(reason=reason)"""
    else :
        kickCode =f"""
@Bot.command()
@commands.has_any_role("{role}")
async def kick(ctx, member: discord.Member, *args, reason="{message}"):
    await member.kick(reason=reason)"""

    return kickCode

def ban(message="Yok",role="Yok"):
    if role == "Yok":
        banCode =f"""
@Bot.command()
async def ban(ctx, member: discord.Member, *args, reason="{message}"):
    await member.ban(reason=reason)"""
    else :
        banCode =f"""
@Bot.command()
@commands.has_any_role("{role}")
async def ban(ctx, member: discord.Member, *args, reason="{message}"):
    await member.ban(reason=reason)"""

    return banCode

def unBan(message="Ban Kaldırıldı.",role="Yok"):
    if role == "Yok":
        unbanCode ="""
@Bot.command()
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name = member_discriminator = member.split("#")
    print(member_name)

    for bans in banned_users:
        user = bans.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f"""+f"""'{message} """+"""{user.mention}')
            return"""
    else :
        unbanCode =f"""
@Bot.command()
@commands.has_any_role({role})
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name = member_discriminator = member.split("#")
    print(member_name)

    for bans in banned_users:
        user = bans.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f"""+f"""'{message} """+"""{user.mention}')
            return"""

    return unbanCode

def token(Token):
    run = f"""
Bot.run("{Token}")"""

    return run