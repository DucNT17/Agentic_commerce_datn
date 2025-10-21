"""seed_data_test

Revision ID: 823f8198c11c
Revises: 3f6c044564a1
Create Date: 2025-10-21 11:11:23.672495

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '823f8198c11c'
down_revision: Union[str, Sequence[str], None] = '3f6c044564a1'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Thêm dữ liệu mẫu vào bảng products."""
    op.execute("""
    INSERT INTO products (
        name, 
        description, 
        price, 
        sku, 
        url, 
        image_url, 
        source, 
        category, 
        brand, 
        is_available, 
        specifications, 
        rating_score, 
        review_count, 
        created_at, 
        updated_at
    ) 
    VALUES
    (
        -- Mẫu 1: Laptop Dell XPS (Tiki)
        'Laptop Dell XPS 15 9530', 
        'Laptop cao cấp, màn hình OLED 3.5K, cấu hình mạnh cho dân sáng tạo nội dung, vỏ nhôm nguyên khối.', 
        45990000, 
        'TK_XPS15_9530', 
        'https://tiki.vn/laptop-dell-xps-15-9530-p123456.html', 
        'https://tiki.vn/images/xps15.png',
        'Tiki', 
        'Máy tính', 
        'Dell', 
        true, 
        '{
            "cpu": "Intel Core i7-13700H", 
            "gpu": "NVIDIA GeForce RTX 4060 8GB", 
            "ram": 16, 
            "storage_capacity": 1024, 
            "storage_type": "SSD", 
            "screen_size": 15.6, 
            "screen_resolution": "3.5K OLED", 
            "weight": 1.86
        }', 
        4.8, 
        150, 
        NOW(), 
        NOW()
    ),
    (
        -- Mẫu 2: MacBook Pro (Shopee)
        'Apple MacBook Pro 14 inch M3 Pro 18GB/512GB', 
        'MacBook Pro mới nhất với chip M3 Pro siêu mạnh, 18GB RAM thống nhất, màn hình Liquid Retina XDR.', 
        52490000, 
        'SP_MBP14_M3', 
        'https://shopee.vn/apple-macbook-pro-14-m3-pro-p654321.html', 
        'https://shopee.vn/images/mbp14.png',
        'Shopee', 
        'Máy tính', 
        'Apple', 
        true, 
        '{
            "cpu": "Apple M3 Pro (11-core)", 
            "gpu": "Apple M3 Pro GPU (14-core)", 
            "ram": 18, 
            "storage_capacity": 512, 
            "storage_type": "SSD", 
            "screen_size": 14.2, 
            "screen_resolution": "Liquid Retina XDR", 
            "weight": 1.61
        }', 
        4.9, 
        230, 
        NOW(), 
        NOW()
    ),
    (
        -- Mẫu 3: iPhone 15 Pro Max (Tiki)
        'Điện thoại Apple iPhone 15 Pro Max 256GB - Titan Tự Nhiên', 
        'iPhone 15 Pro Max, khung viền Titan chuẩn hàng không vũ trụ, chip A17 Pro, camera zoom quang 5x.', 
        31990000, 
        'TK_IP15_PM_256', 
        'https://tiki.vn/iphone-15-pro-max-256gb-p987654.html', 
        'https://tiki.vn/images/ip15.png',
        'Tiki', 
        'Điện thoại', 
        'Apple', 
        true, 
        '{
            "operating_system": "iOS 17", 
            "storage_capacity": 256, 
            "ram": 8, 
            "screen_size": 6.7, 
            "chipset": "Apple A17 Pro", 
            "main_camera_resolution": 48, 
            "battery_capacity": 4422
        }', 
        4.9, 
        1120, 
        NOW(), 
        NOW()
    ),
    (
        -- Mẫu 4: Samsung S24 Ultra (Shopee)
        'Điện thoại Samsung Galaxy S24 Ultra 12GB/512GB', 
        'Samsung S24 Ultra, tích hợp Galaxy AI, bút S Pen, camera 200MP, khung Titan.', 
        30490000, 
        'SP_S24_U_512', 
        'https://shopee.vn/samsung-galaxy-s24-ultra-p456789.html', 
        'https://shopee.vn/images/s24u.png',
        'Shopee', 
        'Điện thoại', 
        'Samsung', 
        true, 
        '{
            "operating_system": "Android 14", 
            "storage_capacity": 512, 
            "ram": 12, 
            "screen_size": 6.8, 
            "chipset": "Snapdragon 8 Gen 3 for Galaxy", 
            "main_camera_resolution": 200, 
            "battery_capacity": 5000
        }', 
        4.7, 
        890, 
        NOW(), 
        NOW()
    ),
    (
        -- Mẫu 5: Laptop Gaming (Tiki)
        'Laptop Gaming Acer Nitro 5 Tiger AN515-58-52SP', 
        'Laptop gaming tầm trung, tản nhiệt tốt, card RTX 4050, màn hình 144Hz.', 
        21990000, 
        'TK_ACER_N5_TIGER', 
        'https://tiki.vn/acer-nitro-5-tiger-p789012.html', 
        'https://tiki.vn/images/nitro5.png',
        'Tiki', 
        'Máy tính', 
        'Acer', 
        true, 
        '{
            "cpu": "Intel Core i5-12500H", 
            "gpu": "NVIDIA GeForce RTX 4050 6GB", 
            "ram": 16, 
            "storage_capacity": 512, 
            "storage_type": "SSD", 
            "screen_size": 15.6, 
            "screen_resolution": "1920x1080", 
            "weight": 2.5
        }', 
        4.6, 
        540, 
        NOW(), 
        NOW()
    );
    """)


def downgrade() -> None:
    """Xóa dữ liệu mẫu khỏi bảng products."""
    # Dùng TRUNCATE để reset bảng về trống và reset ID,
    # hoặc dùng DELETE nếu bạn muốn xóa cụ thể các SKU này.
    # TRUNCATE an toàn hơn cho dữ liệu seed.
    op.execute("TRUNCATE TABLE products RESTART IDENTITY CASCADE;")