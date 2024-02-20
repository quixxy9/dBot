import disnake
from disnake.ext import commands

bot = commands.Bot(command_prefix='/', help_command=None, intents=disnake.Intents.all())
# bot.remove_command('help')
censore = [
    'сука', 'блять', 'пизда', 'хуй',
    ]


# запуск по готовности
@bot.event
async def on_ready():
    print(f'Bot {bot.user} is ready')


# приветствие и выдача роли
@bot.event
async def on_member_join(member):
    role1 = disnake.utils.get(member.guild.roles, id=1208141361463951391)
    role2 = disnake.utils.get(member.guild.roles, id=1208125533066362930)
    channel = bot.get_channel(1208137581389418556)      # member.guild.system_channel

    embed = disnake.Embed(
        title='Новый участник',
        description=f'{member.global_name}, добро пожаловать на сервер!',
        color=0xfff
        )

    await member.add_roles(role1, role2)
    await channel.send(embed=embed)


# цензура
@bot.event
async def on_message(message):
    for censore_word in censore:
        if censore_word in message.content.lower():
            await message.delete()
            await message.channel.send(f'{message.author.mention} сообщение было удалено по причине употребления запрещённого слова')

print('хуй пизда')

token = open('token.txt').readline
bot.run(token)

print('пизда')