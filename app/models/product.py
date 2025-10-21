"""
Product Model
"""
from datetime import datetime
from sqlalchemy import Column, Integer, String, Float, Text, DateTime, Boolean, Index, Numeric
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.sql import func
from .base import Base


class Product(Base):
    """Model cho bảng products"""
    __tablename__ = "products"
    
    id = Column(Integer, primary_key=True, index=True)
    
    # --- Thông tin cơ bản ---
    name = Column(String(255), nullable=False, index=True)
    description = Column(Text, nullable=True) # Mô tả
    
    # Dùng Numeric thay vì Float để đảm bảo chính xác về tiền tệ
    price = Column(Numeric(15, 2), nullable=False, index=True) 
    
    sku = Column(String(100), unique=True, index=True) # Mã SKU (nếu có)
    url = Column(Text, nullable=False) # Link sản phẩm (nên dùng Text)
    image_url = Column(Text, nullable=True) # Link ảnh (nên dùng Text)
    source = Column(String(50), nullable=False, index=True) # Nguồn (Tiki, Shopee, eBay)
    
    # --- Phân loại & Tình trạng ---
    category = Column(String(100), nullable=False, index=True) # "Điện thoại" hoặc "Máy tính"
    brand = Column(String(100), index=True) # "Apple", "Dell", v.v.
    is_available = Column(Boolean, default=True)
    
    # Dùng JSONB để lưu trữ thông số kỹ thuật linh hoạt
    # Đây là "bộ não" để Agent AI so sánh
    specifications = Column(JSONB, nullable=True)
    
    # --- Đánh giá (nếu có) ---
    rating_score = Column(Float, nullable=True) # Điểm đánh giá
    review_count = Column(Integer, nullable=True) # Số lượng đánh giá
    
    # --- Dấu vết thời gian ---
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)

    # Tạo một chỉ mục GIN cho cột JSONB
    # Giúp tăng tốc độ tìm kiếm bên trong JSONB (ví dụ: tìm tất cả sản phẩm có 'ram' = 16)
    __table_args__ = (
        Index('ix_products_specifications', 'specifications', postgresql_using='gin'),
    )
    
    def __repr__(self):
        return f"<Product(id={self.id}, name={self.name}, price={self.price})>"
