# Project State

## Version

v0.0.5

---

## Current Sprint

Sprint 1 - Foundation (Completed)

---

## Completed

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

### User System

* User Service 구현
* `/가입` 명령어 구현
* 중복 가입 방지
* 게임 닉네임 저장

### Monster Foundation

* `monster_species` 테이블 생성
* Monster Key 시스템 도입
* Monster Species 데이터 구조 설계
* JSON 기반 Monster 데이터 관리
* Monster Seed Loader 구현
* Monster Repository 구현
* 초기 Monster Species 5종 구현

  * orange_mushroom
  * blue_mushroom
  * slime
  * pig
  * stump

---

## Current Project Structure

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

## Current Database

### users

* user_id
* discord_name
* game_name
* created_at
* tutorial_completed

### monster_species

* monster_key
* name
* region
* origin
* description
* flavor_text
* icon
* image_path

---

## Current Goal

플레이어 시스템 및 첫 플레이 루프 구현

---

## Next Sprint

### Sprint 2

* `/내정보`
* 플레이어 프로필
* 인벤토리 시스템
* 스타터 소환권 지급
* `/소환`
* 첫 몬스터 획득
* 몬스터 도감

---

## Known Issues

* SQLite Migration 시스템 미구현
* 명령어 동기화는 개발 중 Discord 새로고침 필요

---

## Notes

현재 메키는 Foundation 단계를 완료하였다.

몬스터 데이터는 JSON 기반(Data Driven)으로 관리한다.

새로운 몬스터는 JSON 파일만 추가하면 Seed Loader를 통해 SQLite에 자동 등록된다.

Monster Repository를 통해 게임 시스템은 데이터베이스를 직접 접근하지 않고 Monster 데이터를 조회한다.

가입 시 스타터 몬스터를 직접 지급하지 않는다.

가입 시 **스타터 소환권**을 지급하며, 플레이어는 `/소환`을 통해 첫 몬스터를 획득한다.
