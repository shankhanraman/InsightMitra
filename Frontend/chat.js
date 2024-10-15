document.getElementById("chat-form").addEventListener("submit", function (event) {
    event.preventDefault();
    const message = document.getElementById("chat-input").value;

    fetch("http://localhost:5000/api/chat", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ message: message })
    })
    .then(response => response.json())
    .then(data => {
        console.log("Response from server:", data); // Debugging line
        const chatContainer = document.getElementById("chat-container");
        const userMessage = document.createElement("p");
        const botResponse = document.createElement("p");

        userMessage.textContent = `You: ${message}`;
        botResponse.textContent = `Bot: ${data.response}`;

        chatContainer.appendChild(userMessage);
        chatContainer.appendChild(botResponse);

        // Auto-scroll to the bottom of the chat container
        chatContainer.scrollTop = chatContainer.scrollHeight;

        // Clear the input field
        document.getElementById("chat-input").value = '';
    })
    .catch(error => {
        console.error("Error:", error);
        const chatContainer = document.getElementById("chat-container");
        const errorMessage = document.createElement("p");
        errorMessage.textContent = "Bot: Sorry, something went wrong. Please try again later.";
        chatContainer.appendChild(errorMessage);
    });
});
