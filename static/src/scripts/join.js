const saveBtn = document.getElementById('save-btn');
const nicknameInput = document.getElementById('nickname');
const message = document.getElementById('message');

saveBtn.addEventListener('click', () => {
  const nickname = nicknameInput.value.trim();
  if (!nickname) {
      message.textContent = "Bitte einen Nickname eingeben!";
      return;
  }

  fetch('/save_nickname', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ nickname })
  })
  .then(res => res.json())
  .then(data => {
      message.textContent = data.message;
      window.location.href = "/lobby";
  })
  .catch(err => {
      console.error(err);
      message.textContent = "Fehler beim Speichern!";
  });
});