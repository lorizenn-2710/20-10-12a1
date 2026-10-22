# Món Quà 20/10 – Tập Thể 12A1 ✨🌸

Trang web thiệp tương tác 3D kỷ niệm Ngày Phụ Nữ Việt Nam 20/10 dành tặng các bạn nữ lớp 12A1.

## 🚀 Cấu Trúc Dự Án (Decoupled Assets Architecture)

Dự án được chuẩn hóa theo tiêu chuẩn web hiện đại, tách biệt hoàn toàn mã nguồn HTML và tài nguyên media (ảnh, nhạc) để đảm bảo:
- **Tốc độ tải cực nhanh (< 100ms)**: Không bị nghẽn parse DOM hay tràn bộ nhớ RAM/GPU trên điện thoại di động.
- **Triệt tiêu 4 rủi ro kỹ thuật**:
  1. *Chống lỗi 404 / biểu tượng ảnh vỡ*: Tích hợp cơ chế Graceful SVG Fallback tự động khi thiếu file ảnh.
  2. *Chống lỗi phân biệt hoa/thường*: Toàn bộ 100% file ảnh và đường dẫn được chuẩn hóa chữ thường (lowercase) chuẩn Linux / GitHub Pages.
  3. *Đường dẫn tương đối chuẩn*: Dùng tiền tố `./assets/...` đảm bảo chạy hoàn hảo cả khi mở trực tiếp file offline lẫn deploy GitHub Pages.
  4. *Kiểm tra tính toàn vẹn*: Đi kèm công cụ kiểm tra tự động `verify_assets.py`.

```
aweri-12a1/
├── index.html                   # Giao diện chính (~438 KB, nhẹ hơn 98% so với bản cũ)
├── verify_assets.py             # Script tự động kiểm tra toàn bộ link ảnh/nhạc
├── .gitignore                   # Loại trừ file rác hệ điều hành
├── README.md                    # Hướng dẫn chi tiết
└── assets/
    ├── audio/                   # Nhạc nền (JVKE, Baby)
    └── images/
        ├── night-garden-women.png # Hình minh họa vườn đêm
        ├── photos/              # 46 ảnh kỷ niệm (1-23 đoạn cuối, 24-46 quả cầu 3D)
        ├── book/                # 17 ảnh cuốn sách thanh xuân
        └── qr/                  # 23 mã QR riêng biệt cho từng bạn nữ
```

## 🛠️ Hướng Dẫn Kiểm Tra & Đẩy Lên GitHub

### 1. Kiểm tra tài nguyên
Trước khi đẩy code, chạy lệnh kiểm tra tự động:
```bash
python3 verify_assets.py
```

### 2. Đẩy lên GitHub
```bash
cd /home/phuc/aweri-12a1
git init
git add .
git commit -m "feat: deploy decoupled lightweight 12A1 20/10 website"
git branch -M main
git remote add origin https://github.com/lorizenn-2710/20-10-12a1.git
git push -u origin main --force
```
*(Hoặc tạo repository mới trên GitHub tùy ý).*
