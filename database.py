import sqlalchemy as db
from sqlalchemy import MetaData,Table,Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,String,Integer
from sqlalchemy.orm import sessionmaker

Base = declarative_base()



class Database():
    # Creamos la clase para la conexion a la base de datos

    engine = db.create_engine('postgresql://meragelman:sebastian@localhost/practica')
    Session = sessionmaker(bind=engine)    
    session = Session()
        


    def __init__(self):

        self.connection = self.engine.connect()
        print("instancia de conexion realizada")



    def fetchByQuery(self, query: str) -> None:
        #Lanza una consulta SQL a todas las columnas de la tabla ingresada
        
        fetchQuery = self.connection.execute(f"SELECT * FROM {query}")

        for data in fetchQuery.fetchall():
            print(data)



    def saveData(self,customer):
        self.connection.execute(f"""INSERT INTO customer(name,age,email,address,zip_code) VALUES( '{customer.name}','{customer.age}','{customer.email}','{customer.address}','{customer.zip_code}')""")

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

