from src.database.database import get_connection


# ============================
# 데이터베이스 초기화
# ============================

def initialize_database():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY,
        discord_name TEXT NOT NULL,
        game_name TEXT NOT NULL,
        created_at TEXT NOT NULL,
        tutorial_completed INTEGER DEFAULT 0
    )
    """)

    conn.commit()
    conn.close()

    print("데이터베이스 초기화 완료!")