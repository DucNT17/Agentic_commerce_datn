"""
Script kiểm tra kết nối database PostgreSQL
"""
import os
from dotenv import load_dotenv, find_dotenv
from sqlalchemy import create_engine, text

# Load biến môi trường từ .env
load_dotenv(find_dotenv())

def test_database_connection():
    """Kiểm tra kết nối đến PostgreSQL database"""
    database_url = os.getenv("DATABASE_URL")
    
    if not database_url:
        print("❌ Lỗi: Không tìm thấy DATABASE_URL trong file .env")
        return False
    
    print(f"📍 Đang kết nối đến: {database_url.split('@')[1] if '@' in database_url else 'database'}")
    
    try:
        # Tạo engine và test kết nối
        engine = create_engine(database_url)
        
        with engine.connect() as connection:
            # Thực hiện một query đơn giản
            result = connection.execute(text("SELECT version();"))
            version = result.scalar()
            
            print("✅ Kết nối thành công!")
            print(f"📊 PostgreSQL version: {version}")
            
            # Kiểm tra các bảng hiện có
            result = connection.execute(text("""
                SELECT table_name 
                FROM information_schema.tables 
                WHERE table_schema = 'public'
                ORDER BY table_name;
            """))
            tables = [row[0] for row in result]
            
            if tables:
                print(f"📋 Các bảng trong database: {', '.join(tables)}")
            else:
                print("📋 Chưa có bảng nào trong database")
            
            # Kiểm tra bảng alembic_version (migration history)
            result = connection.execute(text("""
                SELECT EXISTS (
                    SELECT FROM information_schema.tables 
                    WHERE table_schema = 'public' 
                    AND table_name = 'alembic_version'
                );
            """))
            has_alembic = result.scalar()
            
            if has_alembic:
                result = connection.execute(text("SELECT version_num FROM alembic_version;"))
                current_version = result.scalar()
                if current_version:
                    print(f"🔄 Alembic version hiện tại: {current_version}")
                else:
                    print("🔄 Alembic đã được khởi tạo nhưng chưa có migration nào")
            else:
                print("⚠️  Chưa chạy alembic migration (bảng alembic_version chưa tồn tại)")
            
        return True
        
    except Exception as e:
        print(f"❌ Lỗi kết nối database: {e}")
        print("\n💡 Kiểm tra lại:")
        print("   1. PostgreSQL server đã chạy chưa?")
        print("   2. DATABASE_URL trong .env đúng chưa?")
        print("   3. User/password có quyền truy cập không?")
        print("   4. Database đã được tạo chưa?")
        return False

if __name__ == "__main__":
    print("=" * 60)
    print("🔍 KIỂM TRA KẾT NỐI DATABASE")
    print("=" * 60)
    test_database_connection()
    print("=" * 60)

