import discord
import os
from discord.ext import commands
import datetime
#from discord.ext.commands import Bot

PREFIX = '.'

token = 'Njg4NzA5OTExMzU3NDIzNjQ2.Xm4RKA.nl4wUApwqF0z2no-3EOLY587V9o'
clientID = '688709911357423646'

client = commands.Bot( command_prefix = PREFIX)
#Bot = commands.Bot( command_prefix = PREFIX)
client.remove_command('help')

#words
hello_worlds = ['Hello', 'hi', 'Привет', 'Nihao', 'Bonjure', 'Ку', 'hello', 'hi', 'привет', 'nihao', 'bonjure', 'ку']
answer_words = ['узнать информацию о сервере','какая информация','команды','команды сервера','что здесь делать?']
goodbye_words = ['bb', 'пока','byby']

@client.event
async def on_ready():
    print('Bot connected')

#Clear message
@client.command( pass_context = True )
async def clear( ctx, amount = 2 ):
    await ctx.channel.purge( limit = amount)
# .clear 3

# @clear.error
# async def clear_error(ctx, error):
#     if isinstance(error, commands.MissingPermissions):
#         await ctx.send("You cant do that!")

#reaction
@client.command(pass_context = True)
async def reaction(ctx):
    # await Bot.add_reaction(ctx.message, "👻")
    await ctx.message.add_reaction('👻')


@client.command(pass_context = True)
async def hello(ctx, arg):
    author = ctx.message.author
    await ctx.send(f' {author} /// {author.mention} Hello, rabotyagi!\n' + arg)

@client.command(pass_context = True)
@commands.has_permissions(administrator = True)
async def help (ctx):
    emb = discord.Embed(title = "Navigation")

    emb.add_field(name = '{}clear'.format(PREFIX), value = "Очистка чата")
    emb.add_field(name = '{}reaction'.format(PREFIX), value = "Реакция 👻")
    emb.add_field(name = '{}time'.format(PREFIX), value = ".time width height")

    await ctx.send(embed = emb)


#внешние ресурсы
@client.command(pass_context = True)
@commands.has_permissions(administrator = True)

async def time(ctx,width,height):
    emb = discord.Embed(title = 'Date', color = discord.Color.green(), url = 'https://www.timeserver.ru/cities/ru/moscow')

    emb.set_author( name = client.user.name, icon_url= client.user.avatar_url)
    emb.set_footer( text = ctx.author.name, icon_url= ctx.author.avatar_url)
    emb.set_image( url = 'https://picsum.photos/'+width+'/'+height)
    emb.set_thumbnail( url = 'https://picsum.photos/'+width+'/'+height)

    now_date = datetime.datetime.now()
    emb.add_field( name ='Time', value ='Time : {}'.format(now_date) )

    await ctx.send( embed = emb)




@client.event
async def on_message(message):
    msg = message.content.lower()

    if msg in hello_worlds:
        await message.channel.send('Добро пожаловать в клуб Бойз!')

    elif msg in answer_words:
        await message.channel.send('пропишите в чат .help')

    elif msg in goodbye_words:
        await message.channel.send('Chao')

    elif msg == 'поменяй':
        await message.channel.send('(поменял)')
    else:
        print("Not found command")

    await client.process_commands(message)


#Connect

client.run(token)