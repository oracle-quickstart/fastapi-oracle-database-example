# FastAPI Oracle Database Example

This is an example of a Python FastAPI Web Service that interacts with Oracle Database.

![FastAPI OracleDB](https://github.com/oracle-quickstart/fastapi-oracle-database-example/assets/39692236/8964ebc2-b854-403b-95d2-56c488f848c3)


## Prerequisites

- Python 3
- Oracle Database connection details
- curl (optional)

## Installation

##### 1. Clone this repository:

   ```
   git clone https://github.com/oracle-quickstart/fastapi-oracle-database-example.git
   cd fastapi-oracle-database-example
   ```

##### 2. Install the required packages using pip:

   ```
   python3 -m pip install -r requirements.txt
   ```

##### 3. Configuration

   Set database username and connection string environment variables:

   PYTHON_USERNAME

   PYTHON_CONNECTSTRING

##### Example:
###### Local Oracle DB
   ```
   export PYTHON_USERNAME=cj
   export PYTHON_CONNECTSTRING=localhost/orclpdb1
   ```

###### Autonomous Oracle DB

  ```
   export PYTHON_USERNAME=admin
   export PYTHON_CONNECTSTRING='(description= (retry_count=15)(retry_delay=3)(address=(protocol=tcps)(port=1521)(host=adb.ap-sydney-1.oraclecloud.com))(connect_data=(service_name=gxxxxxx_yxxxx_high.adb.oraclecloud.com))(security=(ssl_server_dn_match=yes)))'
  ```

##### 4. Running the FastAPI App

To run the FastAPI app, use the following command:

```
uvicorn fapi:app --reload
```

If the uvicorn binary is not in your PATH, you may need to specify the full
path, for example:

```
$HOME/Library/Python/3.9/bin/uvicorn fapi:app --reload
```

Enter your database user password when prompted.

The app will be accessible at http://localhost:8000 or http://YOUR_LOCAL_IP:8000

##### 5. API Endpoints

Endpoints are shown at http://localhost:8000/docs

They are:
- `POST`: to create data
- `GET`: to read data
- `PUT`: to update data
- `DELETE`: to delete data

Alternative documentation is at http://localhost:8000/redoc

To use the FastAPI app, you can use the 'Try it out' buttons on
http://localhost:8000/docs or alternatively use a command line tool such as
`curl`.

###### Create an order:

```
curl -X 'POST' \
  'http://localhost:8000/orders/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
    "order_id": 1,
    "product_name": "New Product",
    "quantity": 10
  }'
```

###### Update an order:

```
curl -X 'PUT' \
  'http://localhost:8000/orders/1' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
    "order_id": 1,
    "product_name": "Updated Product",
    "quantity": 20
  }'
```

###### Retrieve an order by ID:

```
curl -X 'GET' \
  'http://localhost:8000/orders/1' \
  -H 'accept: application/json'
```

###### Delete an order:

```
curl -X 'DELETE' \
  'http://localhost:8000/orders/1' \
  -H 'accept: application/json'
```

##### 6. Docs

With FastAPI you get OpenAPI docs generated automatically if you go to path ```/docs``` 

```http://127.0.0.1:8000/docs```

<img width="1477" alt="Screen Shot 2023-08-03 at 10 40 58 am" src="https://github.com/oracle-quickstart/fastapi-oracle-database-example/assets/39692236/3b853031-793a-4237-80c8-54a72c6f194f">



```http://127.0.0.1:8000/redoc```

<img width="1493" alt="Screen Shot 2023-08-07 at 10 36 34 am" src="https://github.com/oracle-quickstart/fastapi-oracle-database-example/assets/39692236/908c3794-206b-4e41-a296-37627128f148">

## More on REST APIs for Oracle

Oracle Database also provides native REST APIs capabilities. To learn more, see :

Product Page : https://www.oracle.com/database/technologies/appdev/rest.html

Hands-on LiveLab : https://apexapps.oracle.com/pls/apex/r/dbpm/livelabs/view-workshop?wid=815
