import discord
import os

intents = discord.Intents.default()
intents.members = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    game = discord.Game('서버 입퇴장 기록')
    await client.change_presence(status=discord.Status.online, activity=game)
    print("봇이 온라인으로 변경되었습니다")

@client.event
async def on_member_join(member):
    embed = discord.Embed(title="[서버 입장 로그]", description=f"{member.mention} 님께서 입장하셨습니다", color=0x62c1cc)
    embed.add_field(name="[ 뉴비 인증 안내 ]", value="?????", inline=False)
    embed.set_footer(text=f"{member}")
    await client.get_channel(820657549018660864).send(embed=embed)

access_token = ["BOT_TOKEN"]
client.run(access_token)
