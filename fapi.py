from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import oracledb

# Replace these with your Oracle database connection details
DB_USER = ''
DB_PASSWORD = ''
DB_DSN = '' # eg: (description= (retry_count=15)(retry_delay=3)(address=(protocol=tcps)(port=1521)(host=adb.ap-sydney-1.oraclecloud.com))(connect_data=(service_name=gxxxxxx_high.adb.oraclecloud.com))(security=(ssl_server_dn_match=yes)))

# Pydantic model for order data
class Order(BaseModel):
    order_id: int
    product_name: str
    quantity: int

# Define the FastAPI app
app = FastAPI()

# Connect to the Oracle database
try:
    conn = oracledb.connect(user=DB_USER, password=DB_PASSWORD, dsn=DB_DSN)
    cursor = conn.cursor()
except oracledb.Error as e:
    raise SystemExit(f"Error connecting to Oracle: {e}")

# Endpoint to create an order
@app.post("/orders/", response_model=Order)
def create_order(order: Order):
    try:
        # Insert the order into the database
        cursor.execute(
            "INSERT INTO orders (order_id, product_name, quantity) VALUES (:1, :2, :3)",
            (order.order_id, order.product_name, order.quantity),
        )
        conn.commit()
        return order
    except oracledb.Error as e:
        raise HTTPException(status_code=500, detail=f"Database error: {e}")

# Endpoint to retrieve an order by ID
@app.get("/orders/{order_id}", response_model=Order)
def get_order(order_id: int):
    try:
        # Fetch the order from the database
        cursor.execute("SELECT order_id, product_name, quantity FROM orders WHERE order_id = :1", (order_id,))
        result = cursor.fetchone()
        if result:
            order = {
                "order_id": result[0],
                "product_name": result[1],
                "quantity": result[2],
            }
            return order
        else:
            raise HTTPException(status_code=404, detail="Order not found")
    except oracledb.Error as e:
        raise HTTPException(status_code=500, detail=f"Database error: {e}")

# Close the database connection on app shutdown
@app.on_event("shutdown")
def shutdown_event():
    cursor.close()
    conn.close()

# Run the FastAPI app with uvicorn
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
