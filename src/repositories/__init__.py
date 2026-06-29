import sqlite3


class MonsterRepository:
    def __init__(self, db_path: str = "data/meki.db"):
        self.db_path = db_path

    def get_all_species(self):
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()

        cursor.execute("""
            SELECT
                monster_key,
                name,
                region,
                origin,
                description,
                flavor_text,
                icon,
                image_path
            FROM monster_species
            ORDER BY monster_key
        """)

        rows = cursor.fetchall()
        conn.close()

        return [dict(row) for row in rows]

    def get_species_by_key(self, monster_key: str):
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()

        cursor.execute("""
            SELECT
                monster_key,
                name,
                region,
                origin,
                description,
                flavor_text,
                icon,
                image_path
            FROM monster_species
            WHERE monster_key = ?
        """, (monster_key,))

        row = cursor.fetchone()
        conn.close()

        if row is None:
            return None

        return dict(row)

    def exists(self, monster_key: str) -> bool:
        return self.get_species_by_key(monster_key) is not None