import discord
from discord.ext import commands
from model import fish

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def check(ctx):
    if ctx.message.attachments:
        # Приветствие без имени пользователя
        await ctx.send('Привет! Сейчас проверим твое изображение.')

        # Сообщаем пользователю, что начали обработку
        await ctx.send('Начинаем обработку изображения...')

        for attachment in ctx.message.attachments:
            file_name = attachment.filename
            file_path = f'images/{file_name}'

            # Сохраняем изображение
            await attachment.save(file_path)
            
            # Распознаём изображение
            name = fish(file_path)

            # Сообщаем о сохранении изображения
            await ctx.send(f'Сохранили изображение в {file_path}')
            
            # Сообщаем результат распознавания
            await ctx.send(f'Распознано: {name}')

            # Проверяем название цветка и отправляем сообщение
            if name == "Роза":
                await ctx.channel.send('Это Роза🌹')
            elif name == "Тюльпан":
                await ctx.channel.send('Это Тюльпан🌷')
            elif name == "Ромашка":
                await ctx.channel.send('Это Ромашка🌼')
            elif name == "Лилия":
                await ctx.channel.send('Это Лилия🌺')
            else:
                await ctx.channel.send('Неизвестный цветок🌸')
    else:
        await ctx.send('Вы забыли загрузить картинку 😕')

bot.run("TOKEN")
