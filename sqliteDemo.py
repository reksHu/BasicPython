import sqlite3

zufang=sqlite3.connect("zufang.sqlite")
create_table="create table zufang(title varchar(512), money varchar(128))"
zufang.execute(create_table)