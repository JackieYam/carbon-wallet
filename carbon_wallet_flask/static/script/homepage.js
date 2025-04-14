document.addEventListener("DOMContentLoaded", () => {
    // 🔹 導覽列：高亮目前頁面
    const links = document.querySelectorAll("nav ul li a");
    const currentPath = window.location.pathname;
  
    links.forEach(link => {
      if (link.getAttribute("href") === currentPath) {
        link.style.borderBottom = "2px solid white";
      }
    });
  
    // 🔹 首次載入歡迎提示
    if (!localStorage.getItem("homepage_popup_shown")) {
      setTimeout(() => {
        alert("🎉 歡迎來到智能減碳錢包！");
        localStorage.setItem("homepage_popup_shown", "true");
      }, 800);
    }
  });
  
  // 🔹 滾動導覽列變透明
  window.addEventListener("scroll", () => {
    const navbar = document.querySelector(".navbar");
    if (window.scrollY > 10) {
      navbar.style.backgroundColor = "rgba(76, 175, 80, 0.9)";
    } else {
      navbar.style.backgroundColor = "#4CAF50";
    }
  });
  