document.getElementById("waitlist-form").addEventListener("submit", function (event) {
    event.preventDefault();
    const email = document.getElementById("email").value;

    fetch("http://localhost:5000/api/waitlist", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ email: email })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("response-message").textContent = data.message;
    })
    .catch(error => {
        console.error("Error:", error);
    });
});
