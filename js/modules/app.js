export function initApp() {
  const main = document.getElementById('main-section');

  const views = {
    home: '<p>مرحبًا بك في متجرنا! اختر من القائمة أعلاه.</p>',
    products: `
      <div class="products">
        <div class="product-card">
          <img src="https://via.placeholder.com/200x180?text=منتج+1" />
          <h3>هاتف ذكي ممتاز</h3>
          <p>600 جنيه</p>
          <button onclick="alert('✅ أُضيف إلى السلة')">أضف إلى السلة</button>
        </div>
        <div class="product-card">
          <img src="https://via.placeholder.com/200x180?text=منتج+2" />
          <h3>سماعة لاسلكية</h3>
          <p>450 جنيه</p>
          <button onclick="alert('✅ أُضيف إلى السلة')">أضف إلى السلة</button>
        </div>
      </div>
    `,
    cart: '<p>🛒 سلة المشتريات الخاصة بك فارغة.</p>',
    wishlist: '<p>⭐ لا يوجد عناصر في المفضلة حالياً.</p>',
    login: '<p>🔐 يرجى تسجيل الدخول للمتابعة.</p>'
  };

  // تفعيل التنقل
  document.getElementById("nav-products").addEventListener("click", () => {
    main.innerHTML = views.products;
  });
  document.getElementById("nav-cart").addEventListener("click", () => {
    main.innerHTML = views.cart;
  });
  document.getElementById("nav-wishlist").addEventListener("click", () => {
    main.innerHTML = views.wishlist;
  });
  document.getElementById("nav-login").addEventListener("click", () => {
    main.innerHTML = views.login;
  });

  // عرض البداية
  main.innerHTML = views.home;
}
