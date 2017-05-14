"""
Сохраняет в файл базу данных, находящуюся в оперативной памяти, используя
собственный формат записи; предполагается, что в данных отсутствуют строки
‘endrec.’, ‘enddb.’ и ‘=>’; предполагается, что база данных является словарем
словарей; внимание: применение функции eval может быть опасным – она
выполняет строки как программный код; с помощью функции eval() можно также
реализовать сохранение словарей-записей целиком; кроме того, вместо вызова
print(key,file=dbfile) можно использовать вызов dbfile.write(key + ‘\n’);
"""

dbfilename = 'people-file.txt'
ENDDB = 'enddb.'
ENDREC = 'endrec.'
RECSEP = '=>'

def store_db(db, dbfilename=dbfilename):
    """Save database to file"""
    dbfile = open(dbfilename, 'w')
    for key in db:
        dbfile.write(key + '\n')
        for (name, value) in db[key].items():
            dbfile.write(name + RECSEP + repr(value) + '\n')
        dbfile.write(ENDREC + '\n')
    dbfile.write(ENDDB)
    dbfile.close()


def load_db(dbfilename=dbfilename):
    """Restores database, reconsructing the database"""
    dbfile = open(dbfilename)
    import sys
    sys.stdin = dbfile
    db = {}
    key = input()
    while key != ENDDB:
        rec = {}
        field = input()
        while field != ENDREC:
            name, value = field.split(RECSEP)
            rec[name] = eval(value)
            field = input()
        db[key] = rec
        key = input()
    return db

if __name__ == '__main__':
    from programming_on_python.ex_1_humen_database.init_database import db
    store_db(db)
