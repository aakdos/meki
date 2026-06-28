import discord
from discord.ext import commands
from discord import app_commands

from config import DISCORD_TOKEN
from src.database.init_database import initialize_database
from src.services.user_service import create_user, get_user

# ============================
# 데이터베이스 초기화
# ============================
initialize_database()

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
    synced_commands = await bot.tree.sync()

    print("--------------------------------")
    print(f"{bot.user} 로그인 완료!")
    print(f"슬래시 명령어 동기화 완료! ({len(synced_commands)}개)")
    for command in synced_commands:
        print(f"- /{command.name}")
    print("--------------------------------")


# ============================
# 테스트용 슬래시 명령어
# ============================
@bot.tree.command(
    name="핑",
    description="봇이 정상적으로 작동하는지 확인합니다."
)
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message("🏓 Pong!")


# ============================
# 가입 명령어
# ============================
@bot.tree.command(
    name="가입",
    description="메키 게임을 시작합니다."
)
@app_commands.describe(
    nickname="게임에서 사용할 닉네임"
)
async def join(interaction: discord.Interaction, nickname: str):
    user_id = interaction.user.id
    discord_name = interaction.user.name
    game_name = nickname

    existing_user = get_user(user_id)

    if existing_user is not None:
        await interaction.response.send_message(
            "이미 메키에 가입되어 있습니다.",
            ephemeral=True
        )
        return

    create_user(
        user_id=user_id,
        discord_name=discord_name,
        game_name=game_name
    )

    await interaction.response.send_message(
        f"🎉 가입 완료!\n"
        f"환영합니다, **{game_name}**님!\n"
        f"이제 메키의 모험을 시작할 수 있습니다."
    )


# ============================
# 봇 실행
# ============================
print("bot.py 실행 시작")
bot.run(DISCORD_TOKEN)