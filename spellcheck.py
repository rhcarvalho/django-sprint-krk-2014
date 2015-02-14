import sqlite3
import enchant

c = sqlite3.connect('words.sqlite')
d = enchant.Dict("en_US")

def check_spelling(word):
    return d.check(word)

c.create_function("check_spelling", 1, check_spelling)

with c:
    cursor = c.execute("""
    UPDATE words
    SET misspell = check_spelling(word)
    WHERE misspell IS NULL
    """)
    print cursor.rowcount
