import sqlalchemy as db
from sqlalchemy import MetaData,Table,Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,String,Integer
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class Database():
    """Database Clase para setear la conexion a la base de datos
       y los metodos definen los procedimientos que podemos realizar con la
       tabla customers
       Metodos: fetchByQuery | saveData | updateCustomer |
                deleteCustomer | fetchUserByName | fetchAllUsers

    """
    # Creamos la conexion a la base de datos y el objeto session
    engine = db.create_engine(
        'postgresql://meragelman:sebastian@localhost/practica')
    Session = sessionmaker(bind=engine)
    session = Session()

    def __init__(self):
        """__init__ Conectamos con un pool del objeto engine
        """

        self.connection = self.engine.connect()
        print("instancia de conexion realizada")

    def fetchByQuery(self, query: str) -> None:
        """fetchByQuery Obtengo todos los registros con todas las columnas
                        para la tabla de interes

        :param query: tabla a consultar
        :type query: str
        """

        # Ejecuto la consulta contra la tabla y luego retorno los resultados
        fetchQuery = self.connection.execute(f"SELECT * FROM {query}")
        for data in fetchQuery.fetchall():
            print(data)

    def saveData(self, customer: list) -> None:
        self.connection.execute(
            f"""INSERT INTO customer(name,age,email,address,zip_code) VALUES( '
            {customer.name}','{customer.age}','{customer.email}','
            {customer.address}','{customer.zip_code}')""")

        self.session.add(customer)
        self.session.commit()

    def updateCustomer(self,customerName,address):
        
        dataToUpdate= {Customer.address: address}
        customerData=self.session.query(Customer).filter(Customer.name==customerName)
        customerData=update(dataToUpdate)
        self.session.commit()

    def deleteCustomer(self,customer):
        
        customerData= self.session.query(Customer).filter(Customer.name==customer).first()
        self.session.delete(customerData)
        self.session.commit()



    def fetchUserByName(self):
        meta = MetaData()
        customer = Table('customer', meta, Column('name'))
        data = self.connection.execute(customer.select())
        for cust in data:
            print(cust)


    def fetchAllUsers(self):
        self.session = Session(bind=self.connection)
        customers = self.session.query(Customer).all()
        for cust in customers:
            print(cust)


class Customer(Base):

    __tablename__ = 'customer'
    name= Column(String,primary_key=True)
    age= Column(Integer)
    email= Column(String)
    address= Column(String)
    zip_code= Column(String)


    def __init__(self,name,age,email,address,zip_code):
        self.name = name
        self.age = age
        self.email = email
        self.address = address
        self.zip_code = zip_code

    def __repr__(self):
        return "<Customer(name= '%s', age= '%s',email= '%s',address= '%s',zip_code= '%s')>" % (self.name,self.age,self.email,self.address,self.zip_code)





def main():
    db = Database()
    address= Column(String)
    customer = Customer("Leonela", 28, "leo@gmail.com", "Av. Primera", "C1455")
    db.saveData(customer)
    db.fetchByQuery('public.customer')



if __name__ == "__main__":
    main()

