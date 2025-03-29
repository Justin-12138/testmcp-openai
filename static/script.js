const API_KEY = "your-secret-api-key"; // 应与后端一致

async function sendChat() {
    const input = document.getElementById('chatInput').value;
    const responseDiv = document.getElementById('chatResponse');
    responseDiv.textContent = '处理中...';

    try {
        const response = await fetch('/chat/completions', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'API-Key': API_KEY
            },
            body: JSON.stringify({
                prompt: input,
                max_tokens: 100
            })
        });

        const data = await response.json();
        responseDiv.textContent = JSON.stringify(data, null, 2);
    } catch (error) {
        responseDiv.textContent = '请求失败: ' + error.message;
    }
}

async function getEmbedding() {
    const input = document.getElementById('embeddingInput').value;
    const responseDiv = document.getElementById('embeddingResponse');
    responseDiv.textContent = '计算中...';

    try {
        const response = await fetch('/embeddings', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'API-Key': API_KEY
            },
            body: JSON.stringify({
                text: input
            })
        });

        const data = await response.json();
        responseDiv.textContent = JSON.stringify(data, null, 2);
    } catch (error) {
        responseDiv.textContent = '请求失败: ' + error.message;
    }
}
