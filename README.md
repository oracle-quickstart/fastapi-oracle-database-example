# FastAPI Oracle Database Example

This is an example Python FastAPI application that interacts with Oracle Database.

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

###### Example:

   ```
   export PYTHON_USERNAME=cj
   export PYTHON_CONNECTSTRING=localhost/orclpdb1
   ```

##### 4. Running the FastAPI App

To run the FastAPI app, use the following command:

```
uvicorn fapi:app --host 127.0.0.1 --port 8000 --reload
```

If the uvicorn binary is not in your PATH, you may need to specify the full
path, for example:

```
$HOME/Library/Python/3.9/bin/uvicorn fapi:app --host 127.0.0.1 --port 8000 --reload
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
