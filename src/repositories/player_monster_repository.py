from datetime import datetime

from src.database.database import get_connection


def add_monster(user_id: int, monster_key: str):
    conn = get_connection()
    cursor = conn.cursor()

    obtained_at = datetime.now().isoformat(timespec="seconds")

    cursor.execute(
        """
        INSERT INTO player_monsters (
            user_id,
            monster_key,
            obtained_at
        )
        VALUES (?, ?, ?)
        """,
        (
            user_id,
            monster_key,
            obtained_at
        )
    )

    conn.commit()
    conn.close()


def find_monsters_by_user_id(user_id: int):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT *
        FROM player_monsters
        WHERE user_id = ?
        ORDER BY monster_id
        """,
        (user_id,)
    )

    monsters = cursor.fetchall()

    conn.close()

    return monsters
