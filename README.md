databases folder that houses all sorts of types'o bases,
created like this to make thew host system clean without running servers all the time.

using docker compose untill i learn a better way~!

How to connect ?:

Sql server:
"Server=localhost;Database=Master;User Id=sa;Password=PASSWORD;

mySql:
"server=localhost:3306;user id=USERNAME;password=PASSWORD;persistsecurityinfo=True"

Postgres:
"\nServer=127.0.0.1;Port=5433;Database=DB<Can be Empty>;User Id=User;Password=Password;"

DataLake local-dev
"LocalAzureConnection": "AccountName=devstoreaccount1;AccountKey=Eby8vdM02xNOcqFlqUwJPLlmEtlCDXJ1OUzFT50uSRZ6IFsuFq2UVErCz4I6tq/K1SZFPTOtr/KBHBeksoGMGw==;DefaultEndpointsProtocol=http;BlobEndpoint=http://<CONTAINER NAME>:10000/devstoreaccount1;QueueEndpoint=http://<CONTAINER NAME>:10001/devstoreaccount1;TableEndpoint=http://<CONTAINER NAME>:10002/devstoreaccount1;"

useful links:

https://docs.microsoft.com/en-us/sql/linux/sql-server-linux-configure-mssql-conf?view=sql-server-ver15#datadir

for future me: the db files are in g drive <3
