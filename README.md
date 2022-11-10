# Unidad16
##Acceso a  Bases de Datos


#Para la instalación de la base de datos sobre DEBIAN 11 se utilizo el instructivo
https://es.linuxcapable.com/c%C3%B3mo-instalar-postgresql-en-debian-11-bullseye/

<<< Si bien este paso esta recomendado por el manual, deberia ser ejecutado solo a conciencia ya que implica un upgrade de la version de linux>>>
sudo apt update && sudo apt upgrade -y

sudo apt install software-properties-common apt-transport-https wget -y

sudo wget -O- https://www.postgresql.org/media/keys/ACCC4CF8.asc | gpg --dearmor | sudo tee /
usr/share/keyrings/postgresql.gpg

echo deb [arch=amd64,arm64,ppc64el signed-by=/usr/share/keyrings/postgresql.gpg] http://apt.postgresql.org/pub/repos/apt/ bullseye-pgdg main | sudo tee /etc/apt/sources.list.d/postgresql.list

echo deb [arch=amd64,arm64,ppc64el signed-by=/usr/share/keyrings/postgresql.gpg] http://apt.postgresql.org/pub/repos/apt/ bullseye-pgdg-testing main | sudo tee /etc/apt/sources.list.d/postgresql-testing.list


-----------------------
#Comandos de servicio para PostgreSQL

Para Iniciar
sudo systemctl start postgresql

Para detener
sudo systemctl stop postgresql
---------------

#Configurar Postgress
sudo -i -u postgres

Accedemos al servicio 
psql

Para salir del servicio
exit

# Gestion de Usuarios

sudo su - postgres -c "createuser <name>"

Crear bbdd para el usuario nuevo
sudo su - postgres -c "createdb <namedb>"
sudo -u postgres psql

GRANT ALL PRIVILEGES ON DATABASE <usernamedb> TO <name>;


