async function sayHello() {
    const button = document.getElementById("helloButton");
    const responseDiv = document.getElementById("response");

    // Disable button and show loading state
    button.disabled = true;
    button.textContent = "Loading...";
    responseDiv.textContent = "Sending request to FastAPI...";
    responseDiv.className = "";

    try {
        // Send GET request to FastAPI endpoint
        const response = await fetch("/api/hello");

        if (response.ok) {
            const data = await response.json();

            // Display the message from FastAPI
            responseDiv.textContent = `FastAPI says: "${data.message}"`;
            responseDiv.className = "success";
        } else {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
    } catch (error) {
        console.error("Error:", error);
        responseDiv.textContent = `Error: ${error.message}`;
        responseDiv.className = "error";
    } finally {
        // Re-enable button
        button.disabled = false;
        button.textContent = "Say Message";
    }
}
