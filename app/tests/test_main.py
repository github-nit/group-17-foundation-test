from fastapi.testclient import TestClient
from src.main import app, products

client = TestClient(app)


def setup_function():
    # Clear in-memory products before every test
    products.clear()


def test_root():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json()["status"] == "running"


def test_health():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


def test_create_product():
    product = {
        "sku": "LAP-001",
        "name": "Business Laptop",
        "category": "Electronics",
        "price": 75000,
        "quantity": 25,
        "supplier": "Acme Supplier",
        "reorder_level": 10,
    }

    response = client.post("/products", json=product)

    assert response.status_code == 200
    assert response.json()["product"]["sku"] == "LAP-001"


def test_duplicate_sku():
    product = {
        "sku": "LAP-001",
        "name": "Business Laptop",
        "category": "Electronics",
        "price": 75000,
        "quantity": 25,
        "supplier": "Acme Supplier",
        "reorder_level": 10,
    }

    first_response = client.post("/products", json=product)
    second_response = client.post("/products", json=product)

    assert first_response.status_code == 200
    assert second_response.status_code == 400
    assert second_response.json()["detail"] == "SKU already exists"


def test_search_products():
    product1 = {
        "sku": "LAP-001",
        "name": "Business Laptop",
        "category": "Electronics",
        "price": 75000,
        "quantity": 25,
        "supplier": "Acme Supplier",
        "reorder_level": 10,
    }

    product2 = {
        "sku": "MON-001",
        "name": "Computer Monitor",
        "category": "Electronics",
        "price": 18000,
        "quantity": 15,
        "supplier": "Display Supplier",
        "reorder_level": 5,
    }

    client.post("/products", json=product1)
    client.post("/products", json=product2)

    response = client.get(
        "/products/search?query=laptop"
    )

    assert response.status_code == 200
    assert response.json()["count"] == 1
    assert response.json()["products"][0]["sku"] == "LAP-001"


def test_get_product():
    product = {
        "sku": "KEY-001",
        "name": "Keyboard",
        "category": "Accessories",
        "price": 1500,
        "quantity": 20,
        "supplier": "Keyboard Supplier",
        "reorder_level": 5,
    }

    client.post("/products", json=product)

    response = client.get("/products/KEY-001")

    assert response.status_code == 200
    assert response.json()["sku"] == "KEY-001"


def test_get_product_not_found():
    response = client.get("/products/UNKNOWN-001")

    assert response.status_code == 404
    assert response.json()["detail"] == "Product not found"


def test_update_product():
    product = {
        "sku": "MOUSE-001",
        "name": "Wireless Mouse",
        "category": "Accessories",
        "price": 1200,
        "quantity": 10,
        "supplier": "Mouse Supplier",
        "reorder_level": 5,
    }

    updated_product = {
        "sku": "MOUSE-001",
        "name": "Premium Wireless Mouse",
        "category": "Accessories",
        "price": 1500,
        "quantity": 15,
        "supplier": "New Mouse Supplier",
        "reorder_level": 5,
    }

    client.post("/products", json=product)

    response = client.put(
        "/products/MOUSE-001",
        json=updated_product,
    )

    assert response.status_code == 200
    assert response.json()["product"]["name"] == "Premium Wireless Mouse"
    assert response.json()["product"]["quantity"] == 15


def test_delete_product():
    product = {
        "sku": "DEL-001",
        "name": "Delete Test Product",
        "category": "Test",
        "price": 100,
        "quantity": 5,
        "supplier": "Test Supplier",
        "reorder_level": 2,
    }

    client.post("/products", json=product)

    response = client.delete("/products/DEL-001")

    assert response.status_code == 200
    assert response.json()["product"]["sku"] == "DEL-001"

    get_response = client.get("/products/DEL-001")

    assert get_response.status_code == 404


def test_low_stock_products():
    product = {
        "sku": "LOW-001",
        "name": "Low Stock Product",
        "category": "Test",
        "price": 500,
        "quantity": 3,
        "supplier": "Test Supplier",
        "reorder_level": 10,
    }

    client.post("/products", json=product)

    response = client.get("/products/low-stock")

    assert response.status_code == 200
    assert response.json()["count"] == 1
    assert response.json()["products"][0]["sku"] == "LOW-001"


def test_out_of_stock_products():
    product = {
        "sku": "OUT-001",
        "name": "Out of Stock Product",
        "category": "Test",
        "price": 500,
        "quantity": 0,
        "supplier": "Test Supplier",
        "reorder_level": 5,
    }

    client.post("/products", json=product)

    response = client.get("/products/out-of-stock")

    assert response.status_code == 200
    assert response.json()["count"] == 1
    assert response.json()["products"][0]["sku"] == "OUT-001"


def test_stock_in():
    product = {
        "sku": "STOCK-IN-001",
        "name": "Stock In Product",
        "category": "Test",
        "price": 1000,
        "quantity": 10,
        "supplier": "Test Supplier",
        "reorder_level": 5,
    }

    client.post("/products", json=product)

    response = client.post(
        "/products/STOCK-IN-001/stock/in?quantity=5"
    )

    assert response.status_code == 200
    assert response.json()["quantity_added"] == 5
    assert response.json()["new_quantity"] == 15


def test_stock_out():
    product = {
        "sku": "STOCK-OUT-001",
        "name": "Stock Out Product",
        "category": "Test",
        "price": 1000,
        "quantity": 10,
        "supplier": "Test Supplier",
        "reorder_level": 5,
    }

    client.post("/products", json=product)

    response = client.post(
        "/products/STOCK-OUT-001/stock/out?quantity=3"
    )

    assert response.status_code == 200
    assert response.json()["quantity_removed"] == 3
    assert response.json()["new_quantity"] == 7


def test_stock_out_insufficient_stock():
    product = {
        "sku": "INSUFF-001",
        "name": "Insufficient Stock Product",
        "category": "Test",
        "price": 1000,
        "quantity": 5,
        "supplier": "Test Supplier",
        "reorder_level": 2,
    }

    client.post("/products", json=product)

    response = client.post(
        "/products/INSUFF-001/stock/out?quantity=10"
    )

    assert response.status_code == 400
    assert response.json()["detail"] == "Insufficient stock"


def test_stock_in_invalid_quantity():
    product = {
        "sku": "INVALID-IN-001",
        "name": "Invalid Stock In",
        "category": "Test",
        "price": 1000,
        "quantity": 5,
        "supplier": "Test Supplier",
        "reorder_level": 2,
    }

    client.post("/products", json=product)

    response = client.post(
        "/products/INVALID-IN-001/stock/in?quantity=0"
    )

    assert response.status_code == 400
    assert response.json()["detail"] == "Quantity must be greater than 0"


def test_stock_out_invalid_quantity():
    product = {
        "sku": "INVALID-OUT-001",
        "name": "Invalid Stock Out",
        "category": "Test",
        "price": 1000,
        "quantity": 5,
        "supplier": "Test Supplier",
        "reorder_level": 2,
    }

    client.post("/products", json=product)

    response = client.post(
        "/products/INVALID-OUT-001/stock/out?quantity=0"
    )

    assert response.status_code == 400
    assert response.json()["detail"] == "Quantity must be greater than 0"
def test_update_product_duplicate_sku():
    product1 = {
        "sku": "PROD-001",
        "name": "Product One",
        "category": "Test",
        "price": 1000,
        "quantity": 10,
        "supplier": "Supplier One",
        "reorder_level": 5,
    }

    product2 = {
        "sku": "PROD-002",
        "name": "Product Two",
        "category": "Test",
        "price": 2000,
        "quantity": 20,
        "supplier": "Supplier Two",
        "reorder_level": 5,
    }

    client.post("/products", json=product1)
    client.post("/products", json=product2)

    updated_product = {
        "sku": "PROD-002",
        "name": "Updated Product",
        "category": "Test",
        "price": 1500,
        "quantity": 15,
        "supplier": "Updated Supplier",
        "reorder_level": 5,
    }

    response = client.put(
        "/products/PROD-001",
        json=updated_product,
    )

    assert response.status_code == 400
    assert response.json()["detail"] == "SKU already exists"
def test_create_product_negative_price():
    product = {
        "sku": "INVALID-PRICE-001",
        "name": "Invalid Price Product",
        "category": "Test",
        "price": -100,
        "quantity": 10,
        "supplier": "Test Supplier",
        "reorder_level": 5,
    }

    response = client.post("/products", json=product)

    assert response.status_code == 422
def test_create_product_negative_quantity():
    product = {
        "sku": "INVALID-QTY-001",
        "name": "Invalid Quantity Product",
        "category": "Test",
        "price": 1000,
        "quantity": -5,
        "supplier": "Test Supplier",
        "reorder_level": 5,
    }

    response = client.post("/products", json=product)

    assert response.status_code == 422
def test_create_product_empty_sku():
    product = {
        "sku": "",
        "name": "Invalid SKU Product",
        "category": "Test",
        "price": 1000,
        "quantity": 10,
        "supplier": "Test Supplier",
        "reorder_level": 5,
    }

    response = client.post("/products", json=product)

    assert response.status_code == 422
def test_create_product_empty_name():
    product = {
        "sku": "INVALID-NAME-001",
        "name": "",
        "category": "Test",
        "price": 1000,
        "quantity": 10,
        "supplier": "Test Supplier",
        "reorder_level": 5,
    }

    response = client.post("/products", json=product)

    assert response.status_code == 422
def test_product_status_in_stock():
    products.clear()

    product = {
        "sku": "STATUS-001",
        "name": "Status Test Product",
        "category": "Test",
        "price": 100,
        "quantity": 20,
        "supplier": "Test Supplier",
        "reorder_level": 10,
    }

    client.post("/products", json=product)

    response = client.get("/products/STATUS-001/status")

    assert response.status_code == 200
    assert response.json()["status"] == "In Stock"


def test_product_status_low_stock():
    products.clear()

    product = {
        "sku": "STATUS-002",
        "name": "Low Stock Product",
        "category": "Test",
        "price": 100,
        "quantity": 5,
        "supplier": "Test Supplier",
        "reorder_level": 10,
    }

    client.post("/products", json=product)

    response = client.get("/products/STATUS-002/status")

    assert response.status_code == 200
    assert response.json()["status"] == "Low Stock"


def test_product_status_out_of_stock():
    products.clear()

    product = {
        "sku": "STATUS-003",
        "name": "Out of Stock Product",
        "category": "Test",
        "price": 100,
        "quantity": 0,
        "supplier": "Test Supplier",
        "reorder_level": 10,
    }

    client.post("/products", json=product)

    response = client.get("/products/STATUS-003/status")

    assert response.status_code == 200
    assert response.json()["status"] == "Out of Stock"