import discord
import datetime
import time

import Ganglimbot

from discord.ext import commands , tasks
from ExternalVariable import Token

bot=commands.Bot(command_prefix='!')
timenow = datetime.datetime.now()
waittime = 60

@tasks.loop(seconds=1)
async def GangLimNotice():
    text_channel_list = []
    for guild in bot.guilds:
        for channel in guild.text_channels:
            text_channel_list.append(channel)

    for ch in text_channel_list:
        if ch.name == "강림봇":
            minute = datetime.datetime.now().strftime("%M")
            hour = datetime.datetime.now().strftime("%H")
            if(hour == "10" or hour == "22") and minute == "00" :
                channel = bot.get_channel(ch.id)
                await channel.send("나 \"강림\"")
                print("debugged")
                time.sleep(waittime)

@bot.command()
async def 강림봇테스트(ctx):
    await ctx.send("나 \"강림\"")

@bot.command()
async def 강림봇테스트시간(ctx):
    if ctx.message.author.bot: return None
    GangLimBotChannel = Ganglimbot.getGanlimbotChannel(ctx.message)
    if not GangLimBotChannel or ctx.message.channel in GangLimBotChannel:
        hour = datetime.datetime.now().strftime("%H")
        minute = datetime.datetime.now().strftime("%M")
        await ctx.send("현재 시간은 :" + hour + "시" + minute + "분")

@bot.event
async def on_ready():
    print('로그인중입니다. ')
    print(f"봇={bot.user.name}로 연결중")
    print('연결이 완료되었습니다.')
    await bot.change_presence(status=discord.Status.online, activity=None)

GangLimNotice.start()
bot.run(Token)