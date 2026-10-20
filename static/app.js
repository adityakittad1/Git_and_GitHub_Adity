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
    message.textContent = response.ok ? `${result.message} (UUID ${result.item.itemUUID})` : result.error;
  } catch (error) {
    message.textContent = "Could not reach the server.";
  }
});
