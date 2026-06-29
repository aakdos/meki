from src.database.database import get_connection


def find_by_user_id(user_id: int):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM users WHERE user_id = ?",
        (user_id,)
    )

    user = cursor.fetchone()

    conn.close()

    return user


def insert_user(user_id: int, discord_name: str, game_name: str, created_at: str):
    conn = get_connection()
    cursor = conn.cursor()

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