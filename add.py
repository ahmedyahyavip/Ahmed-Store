import 

# 📧 بيانات الدخول (مشفرة)
encoded_email = "cWF6ZWRjZWQwODJAZ21haWwuY29t"
encoded_password = "Mjc3LTIwMDUtMTUxMS0tLS1BaG1lZEBAIyM="

# فك التشفير
email = base64.b64decode(encoded_email).decode()
password = base64.b64decode(encoded_password).decode()

# ✏️ معلومات المنتج:
product_name = input("اسم المنتج: ").strip()
product_price = input("السعر بالجنيه: ").strip()
product_image_url = input("رابط صورة المنتج: ").strip()
product_category = input("الفئة (هواتف / لابتوبات / ملحقات): ").strip().lower()

# 📦 قالب المنتج:
product_html = f"""
<div class="product">
  <img src="{product_image_url}" alt="{product_name}">
  <h3>{product_name}</h3>
  <p>السعر: {product_price} جنيه</p>
  <form action="https://formsubmit.co/{email}" method="POST">
    <input type="hidden" name="_captcha" value="false">
    <input type="text" name="name" placeholder="الاسم الكامل" required>
    <input type="tel" name="phone" placeholder="رقم الهاتف" required>
    <textarea name="address" placeholder="العنوان" required></textarea>
    <input type="hidden" name="product" value="{product_name}">
    <button type="submit">اطلب الآن</button>
  </form>
</div>
"""

# 🔄 تحديد مكان الحفظ حسب الفئة
category_id = {
    "هواتف": "phones",
    "لابتوبات": "laptops",
    "ملحقات": "accessories"
}.get(product_category, "accessories")

# تحميل ملف index.html
index_path = "index.html"
if not os.path.exists(index_path):
    print("❌ ملف index.html غير موجود في المجلد الحالي.")
    exit()

with open(index_path, "r", encoding="utf-8") as f:
    content = f.read()

# التحقق من وجود زر Owner وإذا لم يكن موجودًا نضيفه في الـ nav
if '<a href="owner.html">Owner</a>' not in content:
    content = content.replace(
        "</nav>",
        '  <a href="owner.html">Owner</a>
</nav>'
    )

# إدخال المنتج قبل إغلاق قسم الفئة
insert_marker = f'<section class="category" id="{category_id}">'
section_end = content.find(f'</section>', content.find(insert_marker))

if section_end == -1:
    print("❌ لم يتم العثور على القسم المناسب لإضافة المنتج.")
    exit()

# إدراج المنتج في القسم المحدد
new_content = content[:section_end] + product_html + content[section_end:]

# حفظ الملف بعد التعديل
with open(index_path, "w", encoding="utf-8") as f:
    f.write(new_content)

print("✅ تم إضافة المنتج إلى الموقع بنجاح.")
