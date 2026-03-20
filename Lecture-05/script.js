// =============================
// CLICK COUNTER
// =============================
const clickBtn = document.getElementById("clickBtn");
const clickCountSpan = document.getElementById("clickCount");

let count = 0;

clickBtn.onclick = () => {
    count++;
    clickCountSpan.textContent = count;
};

// =============================
// THEME TOGGLE + LOCAL STORAGE
// =============================
const btnToggleTheme = document.getElementById("btnToggleTheme");
let isDark = false;

// Load saved theme
const savedTheme = localStorage.getItem("portfolio_theme");
if (savedTheme === "dark") {
    isDark = true;
    document.body.classList.add("dark");
}

// Toggle theme
btnToggleTheme.onclick = () => {
    isDark = !isDark;
    document.body.classList.toggle("dark", isDark);
    localStorage.setItem("portfolio_theme", isDark ? "dark" : "light");
};

// =============================
// LAST UPDATED
// =============================
const lastUpdated = document.getElementById("lastUpdated");
const today = new Date();
const yyyy = today.getFullYear();
const mm = String(today.getMonth() + 1).padStart(2, "0");
const dd = String(today.getDate()).padStart(2, "0");
lastUpdated.textContent = `Last updated: ${yyyy}-${mm}-${dd}`;