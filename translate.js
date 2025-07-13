export const translations = {
  ar: {
    title: "مرحبًا بك في متجر أحمد 🦅⚡",
    products: "المنتجات",
    cart: "سلة الشراء",
    wishlist: "المفضلة",
    login: "تسجيل دخول"
  },
  en: {
    title: "Welcome to Ahmed 🦅⚡ Store",
    products: "Products",
    cart: "Cart",
    wishlist: "Wishlist",
    login: "Login"
  }
};
import { translations } from "./lang/translations.js";

export function switchLanguage(lang) {
  const t = translations[lang];
  document.documentElement.lang = lang;
  document.documentElement.dir = lang === "ar" ? "rtl" : "ltr";
  document.getElementById("site-title").textContent = t.title;
  document.getElementById("nav-products").textContent = t.products;
  document.getElementById("nav-cart").textContent = t.cart;
  document.getElementById("nav-wishlist").textContent = t.wishlist;
  document.getElementById("nav-login").textContent = t.login;
}
