async function fetchKnowledgeBase() {
    const response = await fetch("cached_courses_from_scraped.json");
    return response.json();
}

async function searchKnowledgeBase(query) {
    const knowledgeBase = await fetchKnowledgeBase();
    return knowledgeBase.filter(item => item.text.toLowerCase().includes(query.toLowerCase())).slice(0, 5);
}

async function callGemini(promptText) {
    const response = await fetch("/api/ask", { // Use a relative URL for hosting compatibility
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ contents: [{ parts: [{ text: promptText }] }] })
    });

    const data = await response.json();
    return data.candidates?.[0]?.content?.parts?.[0]?.text || "No response from Gemini.";
}

async function handleUserQuery() {
    const userQuery = document.getElementById("queryInput").value;
    if (!userQuery) return alert("Please enter a question.");

    const relevantSnippets = await searchKnowledgeBase(userQuery);
    if (relevantSnippets.length === 0) {
        document.getElementById("answer").innerText = "No relevant info found.";
        return;
    }

    const promptText = `Use the following snippets to answer the user's question:\n\n` + 
                       relevantSnippets.map((s, i) => `Snippet ${i+1}: ${s.text}`).join("\n\n") +
                       `\n\nUser Question:\n${userQuery}\n\nAnswer in plain text:`;

    const answer = await callGemini(promptText);
    document.getElementById("answer").innerText = answer;
}

document.getElementById("askButton").addEventListener("click", handleUserQuery);
