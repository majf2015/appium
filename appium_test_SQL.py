# -*- coding:UTF-8 -*-
import MySQLdb, ConfigParser, MySQLdb.cursors, os, sys



class Mysqldb:
    def __init__(self):
        self.current_path = sys.path[0]
        self.project_path = os.path.dirname(os.path.dirname(self.current_path))
        self.conf = ConfigParser.ConfigParser()
        self.conf.read(os.path.join(self.project_path,'config.conf'))
        self.debug = int(self.conf.get('Debug','debug'))
        self.db = dict(self.conf.items('DB'))
        self.account = dict(self.conf.items('ManagerAccount'))
        self.conn = MySQLdb.Connection\
        (host = self.db['host'], port = int(self.db['port']), user = self.db['user'], passwd = self.db['passwd'],
         db = self.db['db'], cursorclass = MySQLdb.cursors.DictCursor)
        self.cursor = self.conn.cursor()
        self.result = {}

    def run_main(self):

        self.db_tv()

        self.write_to_test_data()
        self.cursor.close()
        self.conn.close()

    def db_tv(self):
        pass

    def write_to_test_data(self):
        #self.conf.set('Tech','tech',self.result['tech'])
        self.conf.write(open(os.path.join(self.project_path,'test_data\home\home_test_data.conf'),'w'))


db = Mysqldb()
db.run_main()