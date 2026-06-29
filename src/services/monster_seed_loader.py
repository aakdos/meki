import json
import sqlite3
from pathlib import Path


REQUIRED_FIELDS = [
    "key",
    "name",
    "region",
    "origin",
    "description",
    "icon",
    "image_path",
]


def load_monster_species(db_path: str = "data/meki.db", monsters_dir: str = "data/monsters") -> None:
    monster_path = Path(monsters_dir)

    if not monster_path.exists():
        print(f"몬스터 데이터 폴더가 없습니다: {monsters_dir}")
        return

    json_files = list(monster_path.glob("*.json"))

    if not json_files:
        print("로드할 몬스터 JSON 파일이 없습니다.")
        return

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    for json_file in json_files:
        with json_file.open("r", encoding="utf-8") as file:
            monster = json.load(file)

        missing_fields = [field for field in REQUIRED_FIELDS if field not in monster]
        if missing_fields:
            raise ValueError(f"{json_file.name} 필수 필드 누락: {missing_fields}")

        cursor.execute(
            """
            INSERT OR REPLACE INTO monster_species (
                monster_key,
                name,
                region,
                origin,
                description,
                flavor_text,
                icon,
                image_path
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                monster["key"],
                monster["name"],
                monster["region"],
                monster["origin"],
                monster["description"],
                monster.get("flavor_text"),
                monster["icon"],
                monster["image_path"],
            ),
        )

    conn.commit()
    conn.close()

    print(f"몬스터 Species 로드 완료: {len(json_files)}개")