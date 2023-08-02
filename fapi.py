from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import oracledb
import logging

# Replace these with your Oracle database connection details
DB_USER = 'admin'
DB_PASSWORD = '*****'
DB_DSN = ''

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

# Endpoint to delete an order by ID
@app.delete("/orders/{order_id}")
def delete_order(order_id: int):
    try:
        cursor.execute("DELETE FROM orders WHERE order_id = :1", (order_id,))
        conn.commit()
        return {"message": "Order deleted successfully"}
    except oracledb.Error as e:
        logging.error(f"Database error while deleting order: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")


# Endpoint to update an order by ID
@app.put("/orders/{order_id}", response_model=Order)
def update_order(order_id: int, updated_order: Order):
    try:
        # Update the order in the database
        cursor.execute(
            "UPDATE orders SET product_name = :1, quantity = :2 WHERE order_id = :3",
            (updated_order.product_name, updated_order.quantity, order_id),
        )
        conn.commit()
        return updated_order
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
