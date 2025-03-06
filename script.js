async function fetchKnowledgeBase() {
    try {
        const response = await fetch("cached_courses_from_scraped.json");
        if (!response.ok) throw new Error("Failed to load knowledge base.");
        return await response.json();
    } catch (error) {
        console.error("Error fetching knowledge base:", error);
        return []; // Return empty array if fetch fails
    }
}

async function searchKnowledgeBase(query) {
    const knowledgeBase = await fetchKnowledgeBase();
    return knowledgeBase.filter(item => item.text.toLowerCase().includes(query.toLowerCase())).slice(0, 5);
}

async function callGemini(promptText) {
    try {
        const response = await fetch("/api/gemini", { // Calls Vercel API
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ contents: [{ parts: [{ text: promptText }] }] })
        });

        if (!response.ok) {
            const errorMsg = await response.text();
            console.error("API Error:", response.status, errorMsg);
            throw new Error("Failed to get response from Gemini API.");
        }

        const data = await response.json();
        return data.candidates?.[0]?.content?.parts?.[0]?.text || "No response from Gemini.";
    } catch (error) {
        console.error("Error calling Gemini API:", error);
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

    // Find relevant snippets
    const relevantSnippets = await searchKnowledgeBase(userQuery);
    if (relevantSnippets.length === 0) {
        answerField.innerText = "No relevant info found.";
        return;
    }

    // Build prompt for Gemini
    const promptText = `Use the following snippets to answer the user's question:\n\n` + 
                        relevantSnippets.map((s, i) => `Snippet ${i+1}: ${s.text}`).join("\n\n") +
                        `\n\nUser Question:\n${userQuery}\n\nAnswer in plain text:`;

    // Fetch answer from Gemini
    const answer = await callGemini(promptText);
    answerField.innerText = answer;
}

document.getElementById("askButton").addEventListener("click", handleUserQuery);
document.getElementById("questionInput").addEventListener("keyup", (e) => {
    if (e.key === "Enter") {
        document.getElementById("askButton").click();
    }
});
