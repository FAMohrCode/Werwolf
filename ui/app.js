// Main-Menu
function startServer() {
    fetch('/start-server', { method: 'POST' })
        .then(res => res.json())
        .then(data => alert(data.status))
        .catch(err => console.error(err));
}

function exitApp() {
    fetch('/exit', { method: 'POST' })
        .then(res => res.json())
        .then(data => alert(data.status))
        .catch(err => console.error(err));
}

document.addEventListener("DOMContentLoaded", () => {
    const settingsBtn = document.getElementById("settings");
    if (settingsBtn) {
        settingsBtn.addEventListener("click", () => {
            window.location.href = "/settings";
        });
    }

    const exitBtn = document.getElementById("exit");
    if (exitBtn) {
        exitBtn.addEventListener("click", () => {
            exitApp();
        });
    }
});

// Settings-Menu
document.addEventListener("DOMContentLoaded", () => {
    const settingsContainer = document.getElementById("back");
    if (settingsContainer) {
      settingsContainer.addEventListener("click", () => {
        // Weiterleitung zur Flask-Route /
        window.location.href = "/";
      });
    }
});

const themeCheckbox = document.getElementById("theme");
const themeText = document.getElementById("theme-text");

function updateThemeText() {
    themeText.textContent = themeCheckbox.checked ? "Dunkelmodus" : "Hellmodus";
}

themeCheckbox.addEventListener("change", updateThemeText);

// Initial setzen
updateThemeText();


