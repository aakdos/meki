from datetime import datetime

from src.database.database import get_connection


# ============================
# 유저 조회
# ============================

def get_user(user_id: int):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM users WHERE user_id = ?",
        (user_id,)
    )

    user = cursor.fetchone()

    conn.close()

    return user


# ============================
# 유저 생성
# ============================

def create_user(user_id: int, discord_name: str, game_name: str):
    conn = get_connection()
    cursor = conn.cursor()

    created_at = datetime.now().isoformat(timespec="seconds")

    cursor.execute(
        """
        INSERT INTO users (
            user_id,
            discord_name,
            game_name,
            created_at,
            tutorial_completed
        )
        VALUES (?, ?, ?, ?, ?)
        """,
        (
            user_id,
            discord_name,
            game_name,
            created_at,
            0
        )
    )

    conn.commit()
    conn.close()
    