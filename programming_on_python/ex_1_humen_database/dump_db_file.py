from programming_on_python.ex_1_humen_database.make_db_file import load_db

db = load_db()

for kye in db:
    print(kye, '=>', db[kye])
