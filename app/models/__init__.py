"""
SQLAlchemy Models cho Agentic Commerce
"""
# Import Base từ file riêng để tránh circular import
from .base import Base

# Import tất cả models ở đây để Alembic có thể detect
# from .user import User
from .product import Product

__all__ = ["Base", "Product"]

