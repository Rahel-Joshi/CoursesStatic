export default async function handler(req, res) {
    console.log("Request method:", req.method); // Log the request method
    if (req.method !== "POST") {
        console.error("Method not allowed:", req.method);
        return res.status(405).json({ error: "Method Not Allowed" });
    }

    try {
        // Log the incoming request body for debugging
        const requestBody = await req.json();
        console.log("Received request body:", requestBody);

        const GEMINI_API_KEY = process.env.GEMINI_API_KEY;
        const GEMINI_URL = `https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key=${GEMINI_API_KEY}`;

        const response = await fetch(GEMINI_URL, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(requestBody),
        });

        const data = await response.json();
        console.log("Gemini API response:", data);

        return res.status(200).json(data);
    } catch (error) {
        console.error("Error in handler:", error);
        return res.status(500).json({ error: "Failed to fetch Gemini API" });
    }
}
