import sys
import re
import sqlite3
c = sqlite3.connect('words.sqlite')

c.execute("""
    CREATE TABLE IF NOT EXISTS words (word TEXT UNIQUE, misspell bool)
""")


def insert_words(words):
    return c.executemany("""
        INSERT OR IGNORE INTO words (word) VALUES (?)
    """, ((w,) for w in words))

for f in sys.argv[1:]:
    print f,
    t = open(f).read()
    words = (mo.group(0) for mo in re.finditer(r"\b\w+\b", t))
    with c:
        cursor = insert_words(words)
    print cursor.rowcount
