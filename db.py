import MySQLdb

con = MySQLdb.connect(
    host = "localhost",
    user = "root",
    passwd = "Kosuge123",
    db = "mw"
)

cur = con.cursor()

cur.execute(
    """
    CREATE TABLE mw.user
    (id VARCHAR(255),
    sex CHAR(1),
    age INT(1),
    height INT(1),
    passwd VARCHAR(255),
    PRIMARY KEY (id));

    CREATE TABLE mw.weight
    (weight_id MEDIUMINT NOT NULL AUTO_INCREMENT,
    user_id VARCHAR(255),
    date datetime,
    weight INT(1),
    PRIMARY KEY (weight_id),
    FOREIGN KEY (user_id) REFERENCES user(id))
    """
)
con.commit()
con.close()