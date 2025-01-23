from products import dao


class Product:
    def __init__(self, id: int, name: str, description: str, cost: float, qty: int = 0):
        self.id = id
        self.name = name
        self.description = description
        self.cost = cost
        self.qty = qty

    @staticmethod
    def load(data: dict) -> "Product":
        return Product(
            id=data['id'], 
            name=data['name'], 
            description=data['description'], 
            cost=data['cost'], 
            qty=data['qty']
        )


def list_products() -> list[Product]:
    try:
        return [Product.load(product) for product in dao.list_products()]
    except Exception as e:
        raise RuntimeError(f"Failed to list products: {e}")


def get_product(product_id: int) -> Product:
    try:
        product_data = dao.get_product(product_id)
        if not product_data:
            raise ValueError(f"Product with ID {product_id} not found")
        return Product.load(product_data)
    except Exception as e:
        raise RuntimeError(f"Failed to fetch product with ID {product_id}: {e}")


def add_product(product: dict):
    try:
        required_fields = {'id', 'name', 'description', 'cost', 'qty'}
        if not required_fields.issubset(product.keys()) or product['cost'] < 0 or product['qty'] < 0:
            raise ValueError("Invalid product data")
        dao.add_product(product)
    except Exception as e:
        raise RuntimeError(f"Failed to add product: {e}")


def update_qty(product_id: int, qty: int):
    try:
        if qty < 0:
            raise ValueError("Quantity cannot be negative")
        dao.update_qty(product_id, qty)
    except Exception as e:
        raise RuntimeError(f"Failed to update quantity for product ID {product_id}: {e}")

