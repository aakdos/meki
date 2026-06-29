from src.repositories.inventory_repository import (
    add_item,
    find_items_by_user_id,
)

from src.repositories.inventory_repository import (
    add_item,
    find_items_by_user_id,
    subtract_item,
)

def give_item(user_id: int, item_key: str, amount: int):
    add_item(user_id, item_key, amount)


def get_inventory(user_id: int):
    return find_items_by_user_id(user_id)

def consume_item(user_id: int, item_key: str, amount: int):
    return subtract_item(user_id, item_key, amount)