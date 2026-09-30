from fastapi import FastAPI, HTTPException
from src.models import Product

app = FastAPI(
    title="Acme Retail Inventory Management System",
    version="1.0.0",
)

# Temporary in-memory product storage.
products = []


def get_inventory_status(product: Product) -> str:
    if product.quantity == 0:
        return "Out of Stock"

    if product.quantity <= product.reorder_level:
        return "Low Stock"

    return "In Stock"


@app.get("/")
def root():
    return {
        "message": "Acme Retail Inventory Management System",
        "status": "running",
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
    }


@app.post("/products")
def create_product(product: Product):
    for existing_product in products:
        if existing_product.sku == product.sku:
            raise HTTPException(
                status_code=400,
                detail="SKU already exists",
            )

    products.append(product)

    return {
        "message": "Product created successfully",
        "product": product,
    }


@app.get("/products")
def get_products():
    return products


@app.get("/products/search")
def search_products(query: str):
    search_query = query.lower()

    matching_products = []

    for product in products:
        if (
            search_query in product.sku.lower()
            or search_query in product.name.lower()
            or search_query in product.category.lower()
        ):
            matching_products.append(product)

    return {
        "count": len(matching_products),
        "products": matching_products,
    }


@app.post("/products/{sku}/stock/in")
def stock_in(sku: str, quantity: int):
    if quantity <= 0:
        raise HTTPException(
            status_code=400,
            detail="Quantity must be greater than 0",
        )

    for product in products:
        if product.sku == sku:
            product.quantity += quantity

            return {
                "message": "Stock added successfully",
                "sku": sku,
                "quantity_added": quantity,
                "new_quantity": product.quantity,
            }

    raise HTTPException(
        status_code=404,
        detail="Product not found",
    )


@app.get("/products/low-stock")
def get_low_stock_products():
    low_stock_products = []

    for product in products:
        if product.quantity <= product.reorder_level:
            low_stock_products.append(product)

    return {
        "count": len(low_stock_products),
        "products": low_stock_products,
    }


@app.get("/products/out-of-stock")
def get_out_of_stock_products():
    out_of_stock_products = []

    for product in products:
        if product.quantity == 0:
            out_of_stock_products.append(product)

    return {
        "count": len(out_of_stock_products),
        "products": out_of_stock_products,
    }


@app.post("/products/{sku}/stock/out")
def stock_out(sku: str, quantity: int):
    if quantity <= 0:
        raise HTTPException(
            status_code=400,
            detail="Quantity must be greater than 0",
        )

    for product in products:
        if product.sku == sku:
            if quantity > product.quantity:
                raise HTTPException(
                    status_code=400,
                    detail="Insufficient stock",
                )

            product.quantity -= quantity

            return {
                "message": "Stock removed successfully",
                "sku": sku,
                "quantity_removed": quantity,
                "new_quantity": product.quantity,
            }

    raise HTTPException(
        status_code=404,
        detail="Product not found",
    )


@app.get("/products/{sku}/status")
def get_product_status(sku: str):
    for product in products:
        if product.sku == sku:
            return {
                "sku": sku,
                "status": get_inventory_status(product),
            }

    raise HTTPException(
        status_code=404,
        detail="Product not found",
    )


@app.get("/products/{sku}")
def get_product(sku: str):
    for product in products:
        if product.sku == sku:
            return product

    raise HTTPException(
        status_code=404,
        detail="Product not found",
    )


@app.put("/products/{sku}")
def update_product(sku: str, updated_product: Product):
    # Check if the product being updated exists
    for index, product in enumerate(products):
        if product.sku == sku:

            # Prevent changing the SKU to one that already exists
            if updated_product.sku != sku:
                for existing_product in products:
                    if existing_product.sku == updated_product.sku:
                        raise HTTPException(
                            status_code=400,
                            detail="SKU already exists",
                        )

            products[index] = updated_product

            return {
                "message": "Product updated successfully",
                "product": updated_product,
            }

    raise HTTPException(
        status_code=404,
        detail="Product not found",
    )


@app.delete("/products/{sku}")
def delete_product(sku: str):
    for index, product in enumerate(products):
        if product.sku == sku:
            deleted_product = products.pop(index)

            return {
                "message": "Product deleted successfully",
                "product": deleted_product,
            }

    raise HTTPException(
        status_code=404,
        detail="Product not found",
    )