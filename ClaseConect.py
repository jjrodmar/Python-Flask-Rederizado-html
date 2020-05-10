import pymysql

class ClaseConect():
    def __init__(self):
        # host="localhost", port=3306, user="root", passwd="", db="company"
        self.__host = "127.0.0.1"
        self.__port = 3306
        self.__user = "root"
        self.__passwd = ""
        self.__db = "alumnos"
        self.CrearConec()
        self.CrearCursor()
        
      
    @property
    def Host(self):
        return self.__host
    @Host.setter
    def Host(self,host):
        self.__host = host
 
    @property
    def Port(self):
        return self.__port
    @Port.setter
    def Port(self,port):
        self.__port = port
    
    @property
    def User(self):
        return self.__user
    @User.setter
    def User(self,user):
        self.__user = user
    
    @property
    def Passwd(self):
        return self.__passwd
    @Passwd.setter
    def Passwd(self,passwd):
        self.__passwd = passwd
    
    @property
    def Db(self):
        return self.__db
    @Db.setter
    def Db(self,db):
        self.__db = db
    
    def CrearConec(self):
        self.__conect = pymysql.connect(host=self.__host , port=self.__port, user=self.__user,
        passwd=self.__passwd, db=self.__db)
        
    def CrearCursor(self):
        self.__cursor = self.__conect.cursor()
    def EjecutarSql(self,sql):
        self.__cursor.execute(sql)
    def DevolverTodos(self):
        return self.__cursor.fetchall()
    def DevolverUno(self):
        return self.__cursor.fetchone()
    def CerrarConect(self):
        self.__conect.close()
    def RealizaCambios(self):
        self.__conect.commit()
    def DeshaceCambios(self):
        self.__conect.rollback()










