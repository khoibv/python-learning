import pymysql


class DatabaseConnect:
    __db = None

    def __init__(self):
        """Constructor"""
        # open DB connection
        host = 'localhost'
        db_name = 'sakila'
        db_user = 'sakila'
        db_password = 'sakila'
        self.__db = pymysql.connect(host, db_user, db_password, db_name)

    def get_db_info(self):
        cursor = self.__db.cursor()
        cursor.execute('SELECT VERSION()')
        data = cursor.fetchone()
        print('Version of DB %s' % data)

    def work_with_ddl(self):
        cursor = self.__db.cursor()

        # drop test table first
        cursor.execute('DROP TABLE IF EXISTS python_test')

        # then re-create new table
        ddl_query = """
        CREATE TABLE python_test(
          first_name CHAR(20) NOT NULL,
          last_name CHAR(20) NOT NULL,
          age INT,
          sex CHAR(1)
        )
        """
        cursor.execute(ddl_query)

        try:
            # insert new records
            cursor.execute(
                'INSERT INTO python_test VALUES ("%s", "%s", %d, "%s")' % (
                    'khoi', 'bv', 30, 'M'))
            cursor.execute(
                'INSERT INTO python_test VALUES ("%s", "%s", %d, "%s")' % (
                    'tuan', 'nm', 20, 'M'))
            cursor.execute(
                'INSERT INTO python_test VALUES ("%s", "%s", %d, "%s")' % (
                    'test', 'xxx', 18, 'F'))

            print('DB before processing:')
            # get record from table
            self.get_emp()

            # update a record
            cursor.execute("""
            UPDATE python_test
            SET
              age = %d
            WHERE
              first_name = "%s" 
            """ % (35, 'khoi'))

            # delete a record
            cursor.execute("""
            DELETE FROM python_test
            WHERE
              first_name = "%s"
            """ % ('test'))

            # commit transaction
            self.__db.commit()

            print('DB after processing:')
            # get record from table
            self.get_emp()
        except:
            self.__db.rollback()

        # drop test table
        cursor.execute("""
        DROP TABLE python_test
        """)

    def get_emp(self):
        cursor = self.__db.cursor()
        cursor.execute(
            'SELECT first_name, last_name, age, sex FROM python_test')
        results = cursor.fetchall()
        for row in results:
            first_name = row[0]
            last_name = row[1]
            age = row[2]
            sex = row[3]
            print('{firstname: %s, lastname: %s, age: %d, sex: %s}' % \
                  (first_name, last_name, age, sex))

    def __del__(self):
        if self.__db is not None:
            self.__db.close();
