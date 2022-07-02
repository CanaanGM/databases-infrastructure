databases folder that houses all sorts of types'o bases,
created like this to make thew host system clean without running servers all the time.

using docker compose untill i learn a better way~!

How to connect ?:

Sql server:
"Server=localhost;Database=Master;User Id=sa;Password=PASSWORD;

mySql:
"server=localhost:3306;user id=USERNAME;password=PASSWORD;persistsecurityinfo=True"

Postgres:
dotnet:
"Server=127.0.0.1;Port=5433;Database=DB<Can be Empty>;User Id=User;                 Password=Password;"

psycopg2 (python):
```
    dialect+driver://username:password@host:port/database
    postgresql+psycopg2://admin:admin1234@localhost/fastlms
```

### mongodb
connection string: 
```
mongodb://[username:password@]host1[:port1][,...hostN[:portN]][/[defaultauthdb][?options]]
mongodb://mongodbadmin:admin@localhost:27017
```
- https://www.mongodb.com/docs/manual/reference/connection-string/


## Vault warden (local host)
connection should be "http:localhost:< PORT>"

DataLake local-dev
"LocalAzureConnection": "AccountName=devstoreaccount1;AccountKey=Eby8vdM02xNOcqFlqUwJPLlmEtlCDXJ1OUzFT50uSRZ6IFsuFq2UVErCz4I6tq/K1SZFPTOtr/KBHBeksoGMGw==;DefaultEndpointsProtocol=http;BlobEndpoint=http://< CONTAINER NAME>:10000/devstoreaccount1;QueueEndpoint=http://< CONTAINER NAME>:10001/devstoreaccount1;TableEndpoint=http://< CONTAINER NAME>:10002/devstoreaccount1;"

## Airflow

#### create a user thru WSL
``` 
    echo -e "AIRFLOW_UID=$(id -u)" > .env
```
#### init thre db
```
    docker-compose up airflow-init
```
### run 
```
    docker-compose up airflow-init
```
### ???

### PROFIT !! @ http://localhost:8080/
``` https://airflow.apache.org/docs/apache-airflow/stable/start/docker.html#setting-the-right-airflow-user  ```

# useful links:

https://docs.microsoft.com/en-us/sql/linux/sql-server-linux-configure-mssql-conf?view=sql-server-ver15#datadir

for future me: the db files are in g drive <3
