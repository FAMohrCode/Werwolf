let knownPlayers = new Set();

function loadLobbyUsers() {
    const list = document.getElementById("player-list");
    if (!list) return;

    fetch("/api/lobby-users")
        .then(res => res.json())
        .then(data => {
            const newSet = new Set();

            // ➕ Neue Spieler
            for (const id in data) {
                const nickname = data[id].nickname;
                newSet.add(id);

                if (knownPlayers.has(id)) continue;

                const li = document.createElement("li");
                li.textContent = nickname;
                li.dataset.id = id;

                list.appendChild(li);
            }

            // ➖ Entfernte Spieler
            [...knownPlayers].forEach(id => {
                if (!newSet.has(id)) {
                    document
                        .querySelector(`#player-list li[data-id="${id}"]`)
                        ?.remove();
                }
            });

            knownPlayers = newSet;
        })
        .catch(err => console.error("Lobby-Fehler:", err));
}

document.addEventListener("DOMContentLoaded", () => {
    if (document.getElementById("player-list")) {
        loadLobbyUsers();
        setInterval(loadLobbyUsers, 2000);
    }
});
