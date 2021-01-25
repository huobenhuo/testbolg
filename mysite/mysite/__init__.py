import pymysql;
pymysql.install_as_MySQLdb()
db= pymysql.connect(host="127.0.0.1",user="root",
  password="root",db="aaaa",port=3306,charset='utf8')