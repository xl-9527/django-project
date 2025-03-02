from pymysql import install_as_MySQLdb

# python3 中默认使用 pymysql，需要安装 pymysql，但是 django 默认的是 mysqldb 所以需要执行一下的方法
install_as_MySQLdb()