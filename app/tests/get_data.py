import os
import requests
from dotenv import load_dotenv
import json
import base64
# Load environment variables từ file .env
load_dotenv()

# Lấy ACCESS_TOKEN từ biến môi trường
ACCESS_TOKEN = os.getenv("EBAY_ACCESS_TOKEN")

if not ACCESS_TOKEN:
    raise ValueError(
        "EBAY_ACCESS_TOKEN not found in environment variables. "
        "Please set it in your .env file."
    )

ACCESS_TOKEN = ACCESS_TOKEN.replace("Bearer ", "").strip()

url = "https://api.sandbox.ebay.com/buy/browse/v1/item_summary/search"

headers = {
    "Authorization": f"Bearer {ACCESS_TOKEN}",
    "Content-Type": "application/json",
    "X-EBAY-C-MARKETPLACE-ID": "EBAY_US"  # Bắt buộc cho Browse API
}

# Từ khoá tìm kiếm (ví dụ)
params = {"q": "laptop gaming", "limit": 1}

response = requests.get(url, headers=headers, params=params)

# -------------------------------
# Xử lý kết quả
# -------------------------------
if response.status_code == 200:
    data = response.json()
    items = data.get("itemSummaries", [])

    print(items)
    # for item in items:
    #     print("Tên sản phẩm:", item.get("title", "N/A"))
    #     price = item.get("price", {})
    #     print(f"Giá: {price.get('value', 'N/A')} {price.get('currency', '')}")
    #     print("Link:", item.get("itemWebUrl", "N/A"))
    #     print("---")

elif response.status_code == 204:
    print("Không có dữ liệu (Sandbox thường trống hoặc dữ liệu mẫu).")

else:
    print(f"Lỗi {response.status_code}: {response.text}")
