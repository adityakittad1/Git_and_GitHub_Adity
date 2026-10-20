const form = document.querySelector("#todo-form");
const message = document.querySelector("#message");
form.addEventListener("submit", async (event) => {
  event.preventDefault();
  const data = Object.fromEntries(new FormData(form).entries());
  try {
    const response = await fetch("/submittodoitem", {
      method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify(data)
    });
    const result = await response.json();
    if (response.ok) {
      form.elements.itemUUID.value = result.item.itemUUID;
      form.elements.itemHash.value = result.item.itemHash;
      message.textContent = result.message;
    } else {
      message.textContent = result.error;
    }
  } catch (error) {
    message.textContent = "Could not reach the server.";
  }
});

