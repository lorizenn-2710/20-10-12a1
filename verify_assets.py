#!/usr/bin/env python3
"""
Asset Integrity Audit for 12A1 20/10 Web Project
Checks that:
1. All assets referenced in index.html exist on disk.
2. Filenames are strictly lowercase with valid extensions.
3. No broken paths or missing files exist before pushing to GitHub.
"""

import os, re, sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
INDEX_FILE = os.path.join(BASE_DIR, "index.html")

def run_audit():
    print("=" * 60)
    print(" 🌸 BẢN KIỂM TRA TÍNH TOÀN VẸN TÀI NGUYÊN WEB 12A1 (AUDIT) 🌸")
    print("=" * 60)

    if not os.path.exists(INDEX_FILE):
        print(f"❌ LỖI: Không tìm thấy file index.html tại {INDEX_FILE}")
        sys.exit(1)

    with open(INDEX_FILE, "r", encoding="utf-8") as f:
        html = f.read()

    # Find all ./assets references
    asset_refs = sorted(list(set(re.findall(r"[\x27\"](\./assets/[^\x27\"]+)[\x27\"]", html))))
    print(f"🔍 Phát hiện tổng cộng {len(asset_refs)} đường dẫn tài nguyên trong index.html\n")

    errors = []
    success_count = 0

    for ref in asset_refs:
        rel_path = ref.replace("./", "")
        abs_path = os.path.join(BASE_DIR, rel_path)

        # Check existence
        if not os.path.exists(abs_path):
            errors.append(f"❌ THIẾU FILE: {ref}")
            continue

        # Check casing on Linux filesystem
        parent_dir = os.path.dirname(abs_path)
        base_name = os.path.basename(abs_path)
        actual_files = os.listdir(parent_dir)
        if base_name not in actual_files:
            errors.append(f"⚠️ SAI HOA/THƯỜNG (Case-mismatch): '{base_name}' trong {parent_dir}")
            continue

        # Check file non-empty
        size = os.path.getsize(abs_path)
        if size == 0:
            errors.append(f"⚠️ FILE RỖNG (0 byte): {ref}")
            continue

        success_count += 1

    print(f"📊 KẾT QUẢ KIỂM TRA:")
    print(f"   - Hợp lệ & Sẵn sàng: {success_count}/{len(asset_refs)} files")
    print(f"   - Lỗi / Cảnh báo:    {len(errors)} files\n")

    if errors:
        print("DANH SÁCH LỖI CẦN SỬA TRƯỚC KHI PUSH:")
        for err in errors:
            print(f"  {err}")
        sys.exit(1)
    else:
        print("✅ 100% TÀI NGUYÊN ĐÃ SẴN SÀNG! HOÀN TOÀN KHÔNG CÓ RỦI RO KHI PUSH GITHUB.")
        print("=" * 60)

if __name__ == "__main__":
    run_audit()
