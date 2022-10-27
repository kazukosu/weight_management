import MySQLdb

con = MySQLdb.connect(
    host = "localhost",
    user = "root",
    passwd = "ryo",
    db = "mw"
)

cur = con.cursor()

cur.execute(
    """
    CREATE TABLE mw.user
    (id MEDIUMINT NOT NULL AUTO_INCREMENT,
    sex CHAR(1),
    age INT(1),
    height INT(1),
    PRIMARY KEY (id))
    """
)
con.commit()
con.close()