from pydantic import BaseModel, Field


class Product(BaseModel):
    sku: str = Field(..., min_length=1)
    name: str = Field(..., min_length=1)
    category: str = Field(..., min_length=1)
    price: float = Field(..., ge=0)
    quantity: int = Field(..., ge=0)
    supplier: str = Field(..., min_length=1)
    reorder_level: int = Field(default=10, ge=0)