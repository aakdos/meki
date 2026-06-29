import random

from src.repositories.monster_repository import MonsterRepository
from src.services.inventory_service import get_inventory, consume_item
from src.services.player_monster_service import give_monster


STARTER_TICKET_KEY = "starter_ticket"


def has_starter_ticket(user_id: int) -> bool:
    items = get_inventory(user_id)

    for item in items:
        item_key = item[1]
        amount = item[2]

        if item_key == STARTER_TICKET_KEY and amount > 0:
            return True

    return False


def summon_starter_monster(user_id: int):
    if not consume_item(user_id, STARTER_TICKET_KEY, 1):
        return None

    monster_repository = MonsterRepository()
    monsters = monster_repository.get_all_species()

    selected_monster = random.choice(monsters)
    monster_key = selected_monster["monster_key"]

    give_monster(user_id, monster_key)

    return selected_monster