import discord, asyncio #asyncio is needed for a sleep function
from discord.ext import commands

#I will admit i didn't fully understand this whole part of discord.py, but it works. At one point I had the bot run itself twice somehow.
intents = discord.Intents.default() 
intents.message_content = True
intents.members = True
bot = commands.Bot(command_prefix="BOL:", intents=intents)
BOL = 0 #this variable is supposed to be the target's ID which I have left out in this version.

@bot.event
async def on_ready():
    print(f'BOLBOT started as {bot.user}')
    for guild in bot.guilds:
        for channel in guild.text_channels:
            await channel.send("BOLBOT ha iniciado. usa el comando BOL:ayuda para empezar.") #BOLBOT has initialized. use command BOL:ayuda (help)
            print("Intro message sent") 
            break

#"help" command which simply sends the other commands to chat. In case the target user (BOL) uses this, it doesn't help him.
@bot.command(name="ayuda")
async def ayuda(ctx): #the "ctx" is "context" and in discord.py it tells the bot where it is and where to send messages
    if ctx.author.id != BOL:
        await ctx.send("Comandos: BOL:callao , BOL:silenciar , BOL:desconectar")
        print("ayuda command executed successfully.")
    else:
        await ctx.send("No atiendo weones")
        print("BOL tried using ayuda command")

#"shut up", it deletes their last message
@bot.command(name="callao", help="Borra el último mensaje del B.O.L.") 
async def callao_bol(ctx):
    async for message in ctx.channel.history(limit=100):
        if message.author.id == BOL:
            await message.delete()
            await ctx.send("Se ha borrado el último mensaje del BOUL.", delete_after=5)
            return
    await ctx.send("No hay mensajes del BOL para eliminar.") #if no messages from the target user are found, send "no messages found"
    print("callao command executed successfully.")

#"mute", this mutes them for X ammount of seconds
@bot.command(name="silenciar", help="mutea al BOL por X segundos. (formato: Bol:silenciar [número])")
async def silence(ctx, secs: int):
    member = ctx.guild.get_member(BOL) #member variable must be used so the ID from user (BOL) is more than mere numbers, it tells the bot all the info on this member.
    if member and member.voice: #if member exists and is in voice:
        await member.edit(mute=True)
        await ctx.send(f"{member.display_name} ha sido silenciado por {secs} segundos.")
        await asyncio.sleep(secs)
        await member.edit(mute=False)
    print("silenciar command executed successfully.")

#disconnects the user from the call (voice chat).
@bot.command(name="desconectar", help="desconecta al BOL de la llamada.")
async def disconnect(ctx):
    member = ctx.guild.get_member(BOL)
    if member and member.voice:
        await member.move_to(None)
        await ctx.send(f"{member.display_name} ha sido sacado de la llamada.")
    print("desconectar command executed successfully.")

#simply sends "mish" to the chat. Inside joke.
@bot.command(name="mish")
async def mish(ctx):
    await ctx.send("mish")
    print("mish")

bot.run('bot token.')