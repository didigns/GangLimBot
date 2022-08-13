import discord

print("강림봇 부팅")

def getGanlimbotChannel(message):
    GangLimBotChannel = []
    channels = message.guild.text_channels
    for ch in channels:
        if ch.topic is not None and '#강림봇' in ch.topic :
            GangLimBotChannel.append(ch)
    
    return GangLimBotChannel


def getGanlimbotChannelFromChannel(channel):
    GangLimBotChannel = []
    channels = channel
    for ch in channels:
        if ch.topic is not None and '#강림봇' in ch.topic :
            GangLimBotChannel.append(ch)
    
    return GangLimBotChannel