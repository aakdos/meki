from datetime import datetime

from src.repositories.user_repository import (
    find_by_user_id,
    insert_user,
)

# ============================
# 유저 조회
# ============================

def get_user(user_id: int):
    return find_by_user_id(user_id)

# ============================
# 유저 생성
# ============================

def create_user(user_id: int, discord_name: str, game_name: str):
    created_at = datetime.now().isoformat(timespec="seconds")

    insert_user(
        user_id=user_id,
        discord_name=discord_name,
        game_name=game_name,
        created_at=created_at,
    )
    