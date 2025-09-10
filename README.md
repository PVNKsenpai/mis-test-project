# MIS Test Project

Dự án mẫu kiểm thử Manufacturing Information System (MIS).

## 🎯 Mục tiêu
- Kiểm thử các chức năng MIS: đăng nhập, quản lý đơn hàng, tồn kho.
- Viết unit test, integration test.
- Tích hợp CI với GitHub Actions.

## 📂 Cấu trúc thư mục
- `docs/` – Tài liệu yêu cầu & kế hoạch test
- `src/` – Mã giả lập MIS
- `tests/` – Test scripts
- `.github/workflows/` – CI pipeline

## 🚀 Cách chạy

### 1. Cài môi trường
```bash
python3 -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
pip install -r requirements.txt
```

### 2. Chạy test
```bash
pytest tests/ --junitxml=tests/reports/results.xml
```

### 3. CI/CD
Khi push lên GitHub, CI workflow sẽ tự động chạy test.
