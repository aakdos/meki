from src.repositories.inventory_repository import (
    add_item,
    find_items_by_user_id,
)


def give_item(user_id: int, item_key: str, amount: int):
    add_item(user_id, item_key, amount)


def get_inventory(user_id: int):
    return find_items_by_user_id(user_id)