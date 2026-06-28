import sqlite3
from pathlib import Path

# ============================
# 데이터베이스 경로
# ============================

DATA_DIR = Path("data")
DATA_DIR.mkdir(exist_ok=True)

DATABASE_PATH = DATA_DIR / "meki.db"


# ============================
# 데이터베이스 연결
# ============================

def get_connection():
    return sqlite3.connect(DATABASE_PATH)