import discord
from discord.ext import commands
from discord import app_commands

from config import DISCORD_TOKEN
from src.database.init_database import initialize_database
from src.services.user_service import create_user, get_user
from src.services.inventory_service import get_inventory

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
# 내정보 명령어
# ============================
@bot.tree.command(
    name="내정보",
    description="내 메키 플레이어 정보를 확인합니다."
)
async def my_info(interaction: discord.Interaction):
    user_id = interaction.user.id

    user = get_user(user_id)

    if user is None:
        await interaction.response.send_message(
            "아직 메키에 가입하지 않았습니다.\n"
            "`/가입` 명령어로 먼저 게임을 시작해주세요.",
            ephemeral=True
        )
        return

    await interaction.response.send_message(
        f"👤 **플레이어 정보**\n\n"
        f"닉네임: **{user[2]}**\n"
        f"Discord: **{user[1]}**\n"
        f"가입일: `{user[3]}`\n"
        f"튜토리얼: {'완료' if user[4] else '미완료'}"
    )

# ============================
# 인벤토리 명령어
# ============================
@bot.tree.command(
    name="인벤토리",
    description="내가 보유한 아이템을 확인합니다."
)
async def inventory(interaction: discord.Interaction):
    user_id = interaction.user.id

    user = get_user(user_id)

    if user is None:
        await interaction.response.send_message(
            "아직 메키에 가입하지 않았습니다.\n"
            "`/가입` 명령어로 먼저 게임을 시작해주세요.",
            ephemeral=True
        )
        return

    items = get_inventory(user_id)

    if not items:
        await interaction.response.send_message(
            "🎒 **인벤토리**\n\n"
            "보유한 아이템이 없습니다."
        )
        return

    item_names = {
        "starter_ticket": "스타터 소환권",
    }

    lines = []

    for item in items:
        item_key = item[1]
        amount = item[2]
        item_name = item_names.get(item_key, item_key)

        lines.append(f"- {item_name} × {amount}")

    await interaction.response.send_message(
        "🎒 **인벤토리**\n\n" + "\n".join(lines)
    )


# ============================
# 봇 실행
# ============================
print("bot.py 실행 시작")
bot.run(DISCORD_TOKEN)