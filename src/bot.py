import discord
from discord.ext import commands
from discord import app_commands

# ============================
# Discord 권한(Intents)
# ============================
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

# ============================
# 봇 생성
# ============================
bot = commands.Bot(
    command_prefix="!",
    intents=intents
)

# ============================
# 봇 시작
# ============================
@bot.event
async def on_ready():

    # 슬래시 명령어 동기화
    await bot.tree.sync()

    print("--------------------------------")
    print(f"{bot.user} 로그인 완료!")
    print("슬래시 명령어 동기화 완료!")
    print("--------------------------------")


# ============================
# 테스트용 슬래시 명령어
# ============================
@bot.tree.command(
    name="핑",
    description="봇이 정상적으로 작동하는지 확인합니다."
)
async def ping(interaction: discord.Interaction):

    await interaction.response.send_message(
        "🏓 Pong!"
    )


# ============================
# 봇 실행
# ============================
bot.run("TOKEN_HIDDEN") 
print("bot.py 실행 시작")

bot.run("TOKEN_HIDDEN")    