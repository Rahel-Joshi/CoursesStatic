export default {
    async fetch(request) {
      const GEMINI_API_KEY = "YOUR_SECRET_KEY"; // Store this securely in Cloudflare
      const url = `https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key=${GEMINI_API_KEY}`;
  
      const requestBody = await request.json();
      const response = await fetch(url, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(requestBody)
      });
  
      return new Response(response.body, response);
    }
  };
  