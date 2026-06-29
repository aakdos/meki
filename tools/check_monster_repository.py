from src.repositories.monster_repository import MonsterRepository


repository = MonsterRepository()

print("=== 전체 몬스터 ===")
monsters = repository.get_all_species()

for monster in monsters:
    print(monster)

print()
print("=== 주황버섯 조회 ===")
orange_mushroom = repository.get_species_by_key("orange_mushroom")
print(orange_mushroom)

print()
print("=== 존재 여부 ===")
print(repository.exists("orange_mushroom"))
print(repository.exists("not_existing_monster"))