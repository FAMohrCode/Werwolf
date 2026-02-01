// Main-Menu
function startServer() {
    fetch('/start-server', { method: 'POST' })
        .then(res => res.json())
        .then(data => alert(data.status))
        .catch(err => console.error(err));

    window.location.href = "/lobby";
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

function saveSettings() {
    const language = document.getElementById('language').value;
    const port = document.getElementById('port').value;
    const theme = document.getElementById('theme').checked ? 'dark' : 'light';

    const settings = {
        language: language,
        port: port,
        theme: theme
    };

    fetch('/save-settings', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(settings)
    })
    .then(response => response.json())
    .then(data => {
        alert(data.message); // z.B. "Einstellungen gespeichert!"
    })
    .catch(error => {
        console.error('Fehler:', error);
    });
}

// Einstellungen beim Laden der Seite holen
window.addEventListener("DOMContentLoaded", () => {
    const languageSelect = document.getElementById("language");
    const portInput = document.getElementById("port");
    const themeCheckbox = document.getElementById("theme");
    const themeText = document.getElementById("theme-text");

    if (languageSelect && portInput && themeCheckbox) {
        fetch("/settings-data")
            .then(res => res.json())
            .then(data => {
                languageSelect.value = data.language || "de";
                portInput.value = data.port || 5000;
                themeCheckbox.checked = data.theme === "dark";
                themeText.textContent = data.theme === "dark" ? "Dunkelmodus" : "Hellmodus";
            })
            .catch(err => console.error("Fehler beim Laden der Einstellungen:", err));
    }
});


