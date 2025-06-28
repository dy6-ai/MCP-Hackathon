# Frontend Integration Guide

## 🎯 Overview

Your MCP AI Assistant has been cleaned and optimized for frontend integration. All Streamlit apps have been removed, and a clean FastAPI server has been created.

## 🏗️ Current Structure

```
mcp-ai-assistant/
├── api_server.py          # Main FastAPI API server
├── start_server.py        # Startup script
├── requirements.txt       # Dependencies
├── README.md             # Updated documentation
├── API_KEYS_SETUP.md     # API key setup guide
├── finance_tools.py      # Finance functions
├── news_tools.py         # News functions
├── music_tools.py        # Music generation
└── data_analysis_tools.py # Data analysis
```

## 🚀 Quick Start

1. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Set up environment variables**
   Create a `.env` file:
   ```env
   OPENAI_API_KEY=your_openai_api_key_here
   MODELSLAB_API_KEY=your_modelslab_api_key_here
   TAVILY_API_KEY=your_tavily_api_key_here
   HOST=0.0.0.0
   PORT=8000
   RELOAD=true
   ```

3. **Start the server**
   ```bash
   python start_server.py
   ```

4. **Access API documentation**
   - Swagger UI: http://localhost:8000/docs
   - Health Check: http://localhost:8000/api/health

## 📡 API Endpoints

### Math Operations
- `POST /api/math/add` - Add numbers
- `POST /api/math/multiply` - Multiply numbers
- `POST /api/math/subtract` - Subtract numbers
- `POST /api/math/divide` - Divide numbers

### Finance
- `POST /api/finance/stock-price` - Get stock price
- `POST /api/finance/stock-fundamentals` - Get fundamentals
- `POST /api/finance/crypto-price` - Get crypto price

### News
- `POST /api/news/search` - Search news
- `POST /api/news/breaking` - Breaking news

### Music
- `POST /api/music/generate` - Generate music

### Data Analysis
- `POST /api/data/analyze` - Analyze data

### Web Tools
- `POST /api/web/scrape` - Scrape websites

### System
- `GET /api/health` - Health check

## 🔧 Frontend Integration Examples

### JavaScript/TypeScript

```javascript
// Math operation
const mathResponse = await fetch('http://localhost:8000/api/math/add', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({ operation: 'add', a: 10, b: 5 })
});
const mathResult = await mathResponse.json();

// Stock price
const stockResponse = await fetch('http://localhost:8000/api/finance/stock-price', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({ symbol: 'AAPL' })
});
const stockResult = await stockResponse.json();

// News search
const newsResponse = await fetch('http://localhost:8000/api/news/search', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({ topic: 'AI', max_results: 5 })
});
const newsResult = await newsResponse.json();
```

### React Example

```jsx
import { useState } from 'react';

function MathCalculator() {
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const calculate = async (a, b, operation) => {
    setLoading(true);
    try {
      const response = await fetch(`http://localhost:8000/api/math/${operation}`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ operation, a, b })
      });
      const data = await response.json();
      setResult(data.result);
    } catch (error) {
      console.error('Error:', error);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div>
      <button onClick={() => calculate(10, 5, 'add')} disabled={loading}>
        {loading ? 'Calculating...' : 'Add 10 + 5'}
      </button>
      {result && <p>Result: {result}</p>}
    </div>
  );
}
```

### Python Requests

```python
import requests

# Math operation
response = requests.post('http://localhost:8000/api/math/add', 
                        json={'operation': 'add', 'a': 10, 'b': 5})
result = response.json()

# Stock price
response = requests.post('http://localhost:8000/api/finance/stock-price',
                        json={'symbol': 'AAPL'})
stock_data = response.json()

# News search
response = requests.post('http://localhost:8000/api/news/search',
                        json={'topic': 'AI', 'max_results': 5})
news_data = response.json()
```

## 🔒 Security Considerations

1. **CORS Configuration**: The API has CORS enabled for development. Configure properly for production.
2. **API Keys**: Never expose API keys in frontend code. Use environment variables.
3. **Rate Limiting**: Consider implementing rate limiting for production.
4. **Authentication**: Add authentication if needed for production use.

## 🎨 Response Format

All API endpoints return consistent JSON responses:

```json
{
  "result": "response data",
  "timestamp": "2024-01-01T12:00:00.000000",
  "additional_fields": "..."
}
```

Error responses:
```json
{
  "detail": "Error description"
}
```

## 🚀 Production Deployment

1. **Environment Variables**: Set all required API keys
2. **CORS**: Configure CORS for your frontend domain
3. **HTTPS**: Use HTTPS in production
4. **Rate Limiting**: Implement rate limiting
5. **Monitoring**: Add health checks and monitoring

## 📚 Additional Resources

- [API Documentation](http://localhost:8000/docs) - Interactive API docs
- [API_KEYS_SETUP.md](API_KEYS_SETUP.md) - API key setup guide
- [README.md](README.md) - Complete project documentation 