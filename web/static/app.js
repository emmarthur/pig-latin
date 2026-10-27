const sourceText = document.getElementById("source-text");
const outputCard = document.getElementById("output-card");
const outputText = document.getElementById("output-text");
const translateBtn = document.getElementById("btn-translate");
const copyBtn = document.getElementById("btn-copy");
const errorEl = document.getElementById("error-text");
const copyStatus = document.getElementById("copy-status");

function setError(message) {
  errorEl.hidden = !message;
  errorEl.textContent = message || "";
}

async function translate() {
  setError(null);
  copyStatus.hidden = true;
  const text = sourceText.value;
  if (!text.trim()) {
    setError("Enter some text to translate.");
    sourceText.focus();
    return;
  }

  translateBtn.disabled = true;
  try {
    const res = await fetch("/api/translate", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ text }),
    });
    const data = await res.json().catch(() => ({}));
    if (!res.ok) throw new Error(data.detail || "Translation failed.");
    outputCard.hidden = false;
    outputText.value = data.pig_latin;
  } catch (err) {
    setError(err.message || "Translation failed.");
  } finally {
    translateBtn.disabled = false;
  }
}

async function copyResult() {
  copyStatus.hidden = true;
  const value = outputText.value;
  if (!value) return;
  try {
    await navigator.clipboard.writeText(value);
    copyStatus.hidden = false;
  } catch {
    setError("Could not copy to clipboard.");
  }
}

document.querySelectorAll(".chip").forEach((chip) => {
  chip.addEventListener("click", () => {
    sourceText.value = chip.dataset.text || "";
    sourceText.focus();
  });
});

translateBtn.addEventListener("click", () => translate());
copyBtn.addEventListener("click", () => copyResult());
