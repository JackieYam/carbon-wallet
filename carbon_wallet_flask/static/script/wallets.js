document.addEventListener("DOMContentLoaded", () => {
    const addBtn = document.querySelector(".add-btn");
    const popup = document.getElementById("popup");
    const confirmBtn = document.getElementById("confirmAdd");
    const cancelBtn = document.getElementById("cancelAdd");
    const input = document.getElementById("walletName");
  
    // 點擊顯示彈窗
    addBtn.addEventListener("click", () => {
      popup.classList.remove("hidden");
      input.value = "";
    });
  
    // 點擊取消
    cancelBtn.addEventListener("click", () => {
      popup.classList.add("hidden");
    });
  
    // 點擊新增
    confirmBtn.addEventListener("click", () => {
      const walletName = input.value.trim();
      if (walletName) {
        // 導向到 records 頁面並帶參數
        window.location.href = `/records?wallet=${encodeURIComponent(walletName)}`;
      } else {
        alert("請輸入錢包名稱！");
      }
    });
  });