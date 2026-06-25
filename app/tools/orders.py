async def get_order_summary(order_id: str):
    mock_orders = {
        "12345": {
            "order_id": "12345",
            "customer_name": "Sanket",
            "items": ["Shoes", "Watch"],
            "payment_status": "Paid",
            "order_status": "Shipped"
        }
    }

    order = mock_orders.get(order_id)

    if not order:
        return {
            "success": False,
            "message": f"Order {order_id} not found"
        }

    return {
        "success": True,
        **order
    }