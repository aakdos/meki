from src.repositories.player_monster_repository import (
    add_monster,
    find_monsters_by_user_id,
)


def give_monster(user_id: int, monster_key: str):
    add_monster(user_id, monster_key)


def get_player_monsters(user_id: int):
    return find_monsters_by_user_id(user_id)