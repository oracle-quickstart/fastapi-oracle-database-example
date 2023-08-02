# FastAPI Oracle Database Example

This is an example FastAPI application that interacts with an Oracle database.

![FastAPI OracleDB](https://github.com/oracle-quickstart/fastapi-oracle-database-example/assets/39692236/8964ebc2-b854-403b-95d2-56c488f848c3)


## Prerequisites

- Python 3.11+
- Oracle database connection details

##### Create Table in Oracle Database

```
CREATE TABLE orders (
  order_id NUMBER PRIMARY KEY,
  product_name VARCHAR2(100) NOT NULL,
  quantity NUMBER NOT NULL
);
```

## Installation

##### 1. Clone this repository:
   ```
   git clone https://github.com/oracle-quickstart/fastapi-oracle-database-example.git
   cd fastapi-oracle-database-example
   ```

##### 2. Install the required packages using pip:

   ``` 
   pip3 install -r requirements.txt
   ```

##### 3. Configuration

    Open fapi.py and replace the following placeholders with your Oracle database connection details:

   ```
        DB_USER
        DB_PASSWORD
        DB_DSN
   ```

###### Example:

  ```
DB_USER = 'admin'
DB_PASSWORD = 'YourP@ssw0rd82762A'
DB_DSN = '(description= (retry_count=15)(retry_delay=3)(address=(protocol=tcps)(port=1521)(host=adb.ap-sydney-1.oraclecloud.com))(connect_data=(service_name=gxxx_xxx_high.adb.oraclecloud.com))(security=(ssl_server_dn_match=yes)))'
   ```

##### 4. Running the FastAPI App

To run the FastAPI app, use the following command:

```
uvicorn fapi:app --host 127.0.0.1 --port 8000
```

The app will be accessible at http://localhost:8000 or http://YOUR_LOCAL_IP:8000

##### 5. API Endpoints

<img width="995" alt="Screen Shot 2023-08-02 at 6 18 06 pm" src="https://github.com/oracle-quickstart/fastapi-oracle-database-example/assets/39692236/20351ceb-4c48-4418-96a4-80531111260b">

###### Create an order:

POST: to create data.
GET: to read data.
PUT: to update data.
DELETE: to delete data.


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


