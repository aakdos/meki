from src.database.database import get_connection


def find_item(user_id: int, item_key: str):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT *
        FROM player_items
        WHERE user_id = ?
          AND item_key = ?
        """,
        (user_id, item_key)
    )

    item = cursor.fetchone()

    conn.close()

    return item


def find_items_by_user_id(user_id: int):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT *
        FROM player_items
        WHERE user_id = ?
        """,
        (user_id,)
    )

    items = cursor.fetchall()

    conn.close()

    return items


def add_item(user_id: int, item_key: str, amount: int):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO player_items (
            user_id,
            item_key,
            amount
        )
        VALUES (?, ?, ?)
        ON CONFLICT(user_id, item_key)
        DO UPDATE SET amount = amount + excluded.amount
        """,
        (user_id, item_key, amount)
    )

    conn.commit()
    conn.close()

def subtract_item(user_id: int, item_key: str, amount: int):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        UPDATE player_items
        SET amount = amount - ?
        WHERE user_id = ?
          AND item_key = ?
          AND amount >= ?
        """,
        (amount, user_id, item_key, amount)
    )

    conn.commit()
    affected_rows = cursor.rowcount
    conn.close()

    return affected_rows > 0