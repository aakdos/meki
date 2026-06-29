# Project State

## Version

v0.0.7

---

# Current Sprint

## Sprint 2 - First Play Loop (In Progress)

### Completed

#### User

* `/내정보` 구현

#### Inventory System

* player_items 테이블 생성
* Inventory Repository 구현
* Inventory Service 구현
* `/인벤토리` 구현
* 아이템 지급
* 아이템 소비

#### Player Monster System

* player_monsters 테이블 생성
* PlayerMonster Repository 구현
* PlayerMonster Service 구현
* 플레이어 몬스터 저장

#### Summon System

* Summon Service 구현
* `/뽑기` 구현
* 스타터 소환권 소비
* 랜덤 몬스터 획득
* player_monsters 저장

### Remaining

* `/내몬스터`
* 플레이어 몬스터 목록
* 중복 몬스터 합산 출력
* 몬스터 상세 조회
* 몬스터 도감

---

# Completed Sprints

## Sprint 1 - Foundation ✅

### Project

* Discord Bot 생성
* GitHub Repository 생성
* Slash Command 구현
* `/핑` 명령어 구현

### Environment

* `.env` 적용
* `config.py` 생성
* `.gitignore` 적용
* Discord Token 분리

### Database

* SQLite 연결
* 데이터베이스 초기화 시스템 구축
* users 테이블 생성
* monster_species 테이블 생성

### User System

* User Repository 구현
* User Service 리팩토링
* `/가입` 명령어 구현
* 중복 가입 방지
* 게임 닉네임 저장

### Monster Foundation

* Monster Key 시스템 도입
* Monster Species 데이터 구조 설계
* JSON 기반 Monster 데이터 관리
* Monster Seed Loader 구현
* Monster Repository 구현

초기 Monster Species

* orange_mushroom
* blue_mushroom
* slime
* pig
* stump

---

# Current Project Structure

```text
bot.py
config.py

src/
├── commands/
├── database/
├── models/
├── repositories/
├── services/
└── utils/

docs/

data/
└── monsters/

tools/
```

---

# Current Database

## users

* user_id
* discord_name
* game_name
* created_at
* tutorial_completed

## monster_species

* monster_key
* name
* region
* origin
* description
* flavor_text
* icon
* image_path

## player_items

* user_id
* item_key
* amount

## player_monsters

* monster_id
* user_id
* monster_key
* obtained_at

---

# Current Play Loop

```text
가입
    ↓
인벤토리 확인
    ↓
뽑기
    ↓
몬스터 획득
```

---

# Current Goal

Sprint 2 완료

↓

플레이어 몬스터 조회 시스템 구축

↓

첫 번째 플레이 루프 완성

---

# Known Issues

* SQLite Migration 시스템 미구현
* Slash Command 추가 후 Discord 새로고침 필요
* sqlite3.Row / Model 객체 리팩토링 예정

---

# Refactor Queue

* sqlite3.Row 적용
* Model 객체 적용 검토
* Repository 네이밍 정리
* monster_repository → monster_species_repository 검토

---

# Notes

현재 메키는 첫 번째 플레이 루프를 구현 중이다.

플레이어는

가입

↓

인벤토리

↓

뽑기

↓

첫 몬스터 획득

까지 정상적으로 플레이할 수 있다.

플레이어 몬스터는 개체(Instance) 단위로 저장한다.

동일한 몬스터를 여러 마리 보유할 수 있으며,
목록에서는 합산하여 표시한다.

개체값 및 레벨 시스템은 추후 확장한다.

가입 시 몬스터를 직접 지급하지 않는다.

가입 시 스타터 소환권을 지급하며,
플레이어는 `/뽑기`를 통해 첫 몬스터를 획득한다.

튜토리얼은 현재 구현하지 않는다.

향후 단계별 퀘스트(Guide) 형태로 구현하며,
첫 완료 보상으로 스타터 소환권을 지급하는 방향으로 설계한다.
