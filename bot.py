import random

from discord.ext.commands import Bot

BOT_PREFIX = "!"
TOKEN = 'QGT4Q}X|PWX3RWPzRGD5RGH31Gg3UXz1MsV[lh]yrn[UYN|HE{dJ5WF4WTr'

bot = Bot(command_prefix=BOT_PREFIX)

text = ''

Member = []

class role:

    name = 'Blank_Name'
    role = 'Member'
    code = '00000000'
    tag = 'Black_Discord'

def staff_update():
    for i in range(6):
        Member.append(role())
    Member[0].name = 'Niko'
    Member[0].role = 'Guild Master'
    Member[0].code = '4520159825'
    Member[0].tag = '@MW_147'
    Member[1].name = 'TBD'
    Member[1].role = 'Vice Guild Master'
    Member[2].name = 'Haru'
    Member[2].role = 'Officer'
    Member[2].code = '6130975833'
    Member[2].tag = '@Haru'
    Member[3].name = 'Shiro'
    Member[3].role = 'Officer'
    Member[3].code = '28462667'
    Member[3].tag = '@Shiro'
    Member[4].name = 'Sureñio'
    Member[4].role = 'Officer'
    Member[4].code = '6870486802'
    Member[4].tag = '@Sureñio'
    Member[5].name = 'Raymond'
    Member[5].role = 'Officer'
    Member[5].code = '2381919750'
    Member[5].tag = '@raymond1432'
    
def update_member():
    value = 1
    num = 6
    rol = ''
    ch = [' ']
    bracket = False
    global Member
    Member = []
    staff_update()
    for i in range(len(text)):
        if text[i] not in ch:
            rol += text[i]
            if value == 1 and text[i] != '-':
                if text[i] == '@':
                    Member.append(role())
                    rol = rol.replace('-','')
                    rol = rol.replace('@','')
                    Member[num].name = rol.replace(' ','')
                    value = 2
                    rol = '@'
            elif value == 2 and not bracket:
                if text[i] == '-':
                    rol = rol.replace('-','')
                    Member[num].tag = rol.replace(' ','')
                    value = 3
                    rol = ''
            elif value == 3:
                if text[i] == chr(10) or i == len(text) - 1:
                    Member[num].code = rol.replace(' ','')
                    value = 1
                    rol = ''
                    num += 1

def return_member(num):
    i = int(num)
    msg = 'Name: ' + Member[i].name + chr(10) + 'Discord: ' + Member[i].tag + chr(10) + 'Role: ' + Member[i].role + chr(10) + 'Friend ID: ' + Member[i].code
    return msg
    
@bot.event
async def on_message(message):

    lewd = ['hot', 'lewd']
    
    if message.author == bot.user:
        return

    if 'no u' in message.content:
        msg = '{0.author.mention} no u'.format(message)
        await bot.send_message(message.channel, msg)
    elif message.content in lewd:
        msg = '( ͡° ͜ʖ ͡°)'.format(message)
        await bot.send_message(message.channel, msg)
    elif message.content.startswith('?'):
        NAME = message.content[1:]
        for i in range(len(Member)):
            if Member[i].name.lower() == NAME:
                await bot.send_message(message.channel, return_member(i).format(message))
                break
    elif message.content == 'print':
        msg = '@raymond1432'.format(message)
        await bot.send_message(message.channel, msg)
        
    await bot.process_commands(message)

@bot.command(name = 'cheese',
            description = 'Tells about a way to cheese a trial',
            brief = 'What cheese do you want on a trail? iubb, normal attack',
            pass_context = True)
async def cheese(context, *, cheese_type):
    normal_attack = ['normal attack',
                     'savia',
                     'normal',
                     'na']
    if cheese_type == "iubb":
        await bot.say(context.message.author.mention + " UBB over and over again until they're are dead")
    elif cheese_type in normal_attack:
        await bot.say(context.message.author.mention + " More like Savia UBB + Hit count SBB + Atk based on Def conversion buff + Brute Potions")
    else:
        await bot.say(context.message.author.mention + " Never hear of it, maybe " + cheese_type + " makes good fondue")

@bot.command(name = 'talk to yourself')
async def talk_to_yourself(*, message):
    await bot.say('''Haha, nice try. That's not going to happen again!''')

@bot.command(pass_context = True)
async def Graid(context,*,tip):
    if tip == 'tier':
        await bot.say(context.message.author.mention + '''https://docs.google.com/spreadsheets/d/1oXacoQxFZut_JsOXVfYm6wNz6S7LXXgkrUk3U9DR7qU/edit?usp=sharing
This is made by Haru and Shiro''')
           
@bot.command(pass_context = True)
async def force(context, *, num):
    await bot.say(return_member(num))

new = ''
for i in TOKEN:
    new += chr(ord(i)-3)
TOKEN = new
@bot.event
async def on_ready():
    print('RayBot is online')
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    text_id = await bot.get_message(bot.get_channel('445751409732878337'), '447551398482018305')
    global text
    text = ''.join(c for c in text_id.content if c <= '\uFFFF')
    update_member()

              
bot.run(TOKEN)
