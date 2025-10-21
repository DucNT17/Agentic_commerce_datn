# Hướng dẫn Migration với Alembic

## 📋 Tổng quan

Alembic là công cụ migration database cho SQLAlchemy. Nó giúp bạn quản lý các thay đổi schema database một cách có tổ chức.

## 🚀 Các bước thực hiện Migration

### Bước 1: Đảm bảo đã cấu hình DATABASE_URL trong .env

```bash
# File .env ở thư mục gốc project
DATABASE_URL=postgresql+psycopg2://username:password@localhost:5432/database_name
```

### Bước 2: Kiểm tra kết nối database (tùy chọn)

```bash
cd app
python tests/test_db_connection.py
```

### Bước 3: Tạo migration file (autogenerate)

```bash
cd app
alembic revision --autogenerate -m "Initial migration - create users and products tables"
```

**Giải thích:**

- `revision`: Tạo migration file mới
- `--autogenerate`: Tự động detect thay đổi từ models
- `-m "message"`: Mô tả về migration này

**Kết quả:** Sẽ tạo file mới trong `app/alembic/versions/` với tên dạng `xxxx_initial_migration.py`

### Bước 4: Kiểm tra migration file (QUAN TRỌNG!)

Mở file vừa tạo trong `app/alembic/versions/` và kiểm tra:

- Các bảng được tạo có đúng không?
- Các cột có đầy đủ không?
- Các index, constraint có đúng không?

### Bước 5: Chạy migration (áp dụng vào database)

```bash
cd app
alembic upgrade head
```

**Giải thích:**

- `upgrade head`: Áp dụng tất cả migrations chưa chạy lên version mới nhất

### Bước 6: Xác nhận migration thành công

```bash
cd app
alembic current
```

Hoặc kiểm tra bằng script test:

```bash
python tests/test_db_connection.py
```

## 📝 Các lệnh Alembic thường dùng

### Xem lịch sử migrations

```bash
alembic history
```

### Xem migration hiện tại

```bash
alembic current
```

### Upgrade lên version cụ thể

```bash
alembic upgrade <revision_id>
```

### Downgrade về version trước

```bash
alembic downgrade -1
```

### Downgrade về version cụ thể

```bash
alembic downgrade <revision_id>
```

### Downgrade về trạng thái ban đầu (xóa tất cả)

```bash
alembic downgrade base
```

### Tạo migration thủ công (không autogenerate)

```bash
alembic revision -m "Add custom index"
```

## 🔄 Quy trình khi thay đổi Models

1. **Sửa model** trong `app/models/`
2. **Tạo migration mới:**

   ```bash
   cd app
   alembic revision --autogenerate -m "Mô tả thay đổi"
   ```

3. **Kiểm tra file migration** được tạo
4. **Chạy migration:**

   ```bash
   alembic upgrade head
   ```

## ⚠️ Lưu ý quan trọng

1. **Luôn kiểm tra file migration** trước khi chạy upgrade
2. **Backup database** trước khi chạy migration trên production
3. **Không sửa file migration đã chạy** - tạo migration mới thay vì sửa cái cũ
4. **Commit file migration** vào git để team cùng sử dụng
5. **Test migration** trên môi trường dev trước khi deploy production

## 🛠️ Troubleshooting

### Lỗi: "Target database is not up to date"

```bash
alembic stamp head  # Đánh dấu database ở version hiện tại
```

### Lỗi: "Can't locate revision identified by 'xxx'"

Kiểm tra file trong `alembic/versions/` có đủ không

### Lỗi kết nối database

- Kiểm tra PostgreSQL đã chạy chưa
- Kiểm tra DATABASE_URL trong .env
- Kiểm tra user/password có quyền truy cập không

### Migration không detect được thay đổi

- Đảm bảo đã import model trong `app/models/__init__.py`
- Kiểm tra `target_metadata` trong `env.py` đã trỏ đúng `Base.metadata`

## 📚 Ví dụ thực tế

### Ví dụ 1: Thêm cột mới vào bảng User

```python
# app/models/user.py
class User(Base):
    # ... existing columns ...
    phone_number = Column(String(20))  # Thêm cột mới
```

Sau đó:

```bash
cd app
alembic revision --autogenerate -m "Add phone_number to users"
alembic upgrade head
```

### Ví dụ 2: Tạo bảng mới

```python
# app/models/order.py
from app.models import Base

class Order(Base):
    __tablename__ = "orders"
    id = Column(Integer, primary_key=True)
    # ... other columns ...
```

Thêm import trong `app/models/__init__.py`:

```python
from app.models.order import Order
__all__ = ["Base", "User", "Product", "Order"]
```

Sau đó:

```bash
cd app
alembic revision --autogenerate -m "Create orders table"
alembic upgrade head
```

## 🎯 Best Practices

1. **Tên migration rõ ràng:** Sử dụng tên mô tả chi tiết

   ```bash
   alembic revision --autogenerate -m "Add email verification fields to users"
   ```

2. **Một migration cho một thay đổi logic:** Không gộp quá nhiều thay đổi vào một migration

3. **Test rollback:** Đảm bảo downgrade cũng hoạt động

   ```bash
   alembic downgrade -1
   alembic upgrade head
   ```

4. **Document migration phức tạp:** Thêm comment trong file migration nếu có logic phức tạp

5. **Version control:** Luôn commit file migration vào git

## 📊 Cấu trúc thư mục

```
app/
├── alembic/
│   ├── versions/          # Các file migration
│   │   ├── xxxx_initial.py
│   │   └── yyyy_add_field.py
│   ├── env.py            # Cấu hình Alembic
│   └── script.py.mako    # Template cho migration
├── alembic.ini           # File config chính
├── models/               # SQLAlchemy models
│   ├── __init__.py
│   ├── user.py
│   └── product.py
└── tests/
    └── test_db_connection.py
```
