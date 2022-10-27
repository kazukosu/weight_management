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
    PRIMARY KEY (id));

    CREATE TABLE mw.weight
    (weight_id MEDIUMINT NOT NULL AUTO_INCREMENT,
    user_id MEDIUMINT NOT NULL,
    date datetime,
    weight INT(1),
    PRIMARY KEY (weight_id),
    FOREIGN KEY (user_id) REFERENCES user(id))
    """
)

"""



"""
con.commit()
con.close()