from src.database.database import get_connection


def create_users_table(cursor):
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY,
        discord_name TEXT NOT NULL,
        game_name TEXT NOT NULL,
        created_at TEXT NOT NULL,
        tutorial_completed INTEGER DEFAULT 0
    )
    """)


def create_monster_species_table(cursor):
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS monster_species (
        species_id INTEGER PRIMARY KEY AUTOINCREMENT,
        monster_key TEXT UNIQUE NOT NULL,
        name TEXT NOT NULL,
        region TEXT NOT NULL,
        origin TEXT NOT NULL,
        description TEXT,
        flavor_text TEXT,
        icon TEXT,
        image_path TEXT,
        is_active INTEGER NOT NULL DEFAULT 1,
        created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
    )
    """)


def initialize_database():
    conn = get_connection()
    cursor = conn.cursor()

    create_users_table(cursor)
    create_monster_species_table(cursor)

    conn.commit()
    conn.close()

    print("데이터베이스 초기화 완료!")


if __name__ == "__main__":
    initialize_database()