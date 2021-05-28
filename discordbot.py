from discord.ext import commands
import os
import traceback

client = commands.Bot(command_prefix='/')
TOKEN = os.environ['DISCORD_BOT_TOKEN']

ID_silver = 842752442382286928
ID_gold = 815767410908332053
ID_platinum = 815637115736031232
ID_diamond = 815636793574948865
ID_master = 815808290998059028

async def remove_allrole(payload):
    channel = client.get_channel(payload.channel)
    member = payload.author
    role = member.guild.get_role(ID_silver)
    await member.remove_roles(role)
    role = member.guild.get_role(ID_gold)
    await member.remove_roles(role)
    role = member.guild.get_role(ID_platinum)
    await member.remove_roles(role)
    role = member.guild.get_role(ID_diamond)
    await member.remove_roles(role)
    role = member.guild.get_role(ID_master)
    await member.remove_roles(role)

async def add_role(payload,role_id):
    channel = client.get_channel(payload.channel)
    member = payload.author
    role = member.guild.get_role(role_id)
    await member.add_roles(role)

@client.event
async def on_ready():
    print('ログインしました')

@client.event
async def on_message(message):
    if message.author.bot:
        return
    if message.content == '/silver':
        await remove_allrole(message)
        await add_role(message,ID_silver)

    if message.content == '/gold':
        await remove_allrole(message)
        await add_role(message,ID_gold)

    if message.content == '/platinum':
        await remove_allrole(message)
        await add_role(message,ID_platinum)

    if message.content == '/diamond':
        await remove_allrole(message)
        await add_role(message,ID_diamond)

    if message.content == '/master':
        await remove_allrole(message)
        await add_role(message,ID_master)

client.run(TOKEN)
