async function callGemini(promptText) {
    try {
        const response = await fetch("/api/gemini", { // Calls Vercel API
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ contents: [{ parts: [{ text: promptText }] }] })
        });

        if (!response.ok) {
            console.error("API error:", response.status, await response.text());
            throw new Error("Failed to get response from Gemini API.");
        }

        const data = await response.json();
        
        if (!data.candidates || !data.candidates.length) {
            throw new Error("No valid response from Gemini.");
        }

        return data.candidates[0].content.parts[0].text || "No meaningful response.";
    } catch (error) {
        console.error("Error contacting Gemini API:", error);
        return "Error contacting the Gemini API.";
    }
}

async function handleUserQuery() {
    const inputField = document.getElementById("questionInput");
    const answerField = document.getElementById("answer");
    const userQuery = inputField.value.trim();

    if (!userQuery) {
        alert("Please enter a question.");
        return;
    }

    // Show loading indicator
    answerField.innerHTML = `<div class="spinner"></div>`;

    // Fetch answer from Gemini
    const answer = await callGemini(userQuery);
    
    // Remove loading indicator and show response
    answerField.innerText = answer;
}

document.getElementById("askButton").addEventListener("click", handleUserQuery);
document.getElementById("questionInput").addEventListener("keyup", (e) => {
    if (e.key === "Enter") {
        document.getElementById("askButton").click();
    }
});
