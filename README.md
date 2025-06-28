# MCP AI Assistant API

A comprehensive AI assistant API with multiple tools and capabilities, optimized for frontend integration.

## 🚀 Features

- **🧮 Math Operations**: Addition, multiplication, subtraction, division
- **📈 Finance Tools**: Stock prices, fundamentals, crypto prices, market data
- **📰 News Services**: Breaking news, tech news, business news, sports, science
- **🎵 Music Generation**: AI-powered music creation using ModelsLab
- **📊 Data Analysis**: CSV analysis, SQL queries, data preprocessing
- **🌐 Web Scraping**: Extract content from websites
- **🔍 Web Search**: Search the web for information

## 📋 Requirements

### Required API Keys
1. **OpenAI API Key** (`OPENAI_API_KEY`) - Required for all AI operations
2. **ModelsLab API Key** (`MODELSLAB_API_KEY`) - Required for music generation

### Optional API Keys
3. **Tavily API Key** (`TAVILY_API_KEY`) - Enhanced web search (optional)

## 🛠️ Installation

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd mcp-ai-assistant
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   Create a `.env` file in the project root:
   ```env
   # Required API Keys
   OPENAI_API_KEY=your_openai_api_key_here
   MODELSLAB_API_KEY=your_modelslab_api_key_here
   
   # Optional API Keys
   TAVILY_API_KEY=your_tavily_api_key_here
   
   # Server Configuration
   HOST=0.0.0.0
   PORT=8000
   RELOAD=true
   ```

## 🚀 Quick Start

### Start the API Server
```bash
python start_server.py
```

The server will start on `http://localhost:8000`

### API Documentation
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc
- **Health Check**: http://localhost:8000/api/health

## 📚 API Endpoints

### Math Operations
- `POST /api/math/add` - Add two numbers
- `POST /api/math/multiply` - Multiply two numbers
- `POST /api/math/subtract` - Subtract two numbers
- `POST /api/math/divide` - Divide two numbers

### Finance Tools
- `POST /api/finance/stock-price` - Get stock price
- `POST /api/finance/stock-fundamentals` - Get stock fundamentals
- `POST /api/finance/crypto-price` - Get cryptocurrency price

### News Services
- `POST /api/news/search` - Search news articles
- `POST /api/news/breaking` - Get breaking news

### Music Generation
- `POST /api/music/generate` - Generate AI music

### Data Analysis
- `POST /api/data/analyze` - Analyze CSV data

### Web Tools
- `POST /api/web/scrape` - Scrape website content

### System
- `GET /api/health` - Health check
- `GET /api/info` - API information

## 🔧 Usage Examples

### Math Operation
```bash
curl -X POST "http://localhost:8000/api/math/add" \
     -H "Content-Type: application/json" \
     -d '{"operation": "add", "a": 10, "b": 5}'
```

### Stock Price
```bash
curl -X POST "http://localhost:8000/api/finance/stock-price" \
     -H "Content-Type: application/json" \
     -d '{"symbol": "AAPL"}'
```

### News Search
```bash
curl -X POST "http://localhost:8000/api/news/search" \
     -H "Content-Type: application/json" \
     -d '{"topic": "artificial intelligence", "max_results": 5}'
```

### Music Generation
```bash
curl -X POST "http://localhost:8000/api/music/generate" \
     -H "Content-Type: application/json" \
     -d '{"prompt": "Create a relaxing ambient melody"}'
```

## 🏗️ Project Structure

```
mcp-ai-assistant/
├── api_server.py          # Main FastAPI server
├── start_server.py        # Startup script
├── requirements.txt       # Python dependencies
├── .env                  # Environment variables
├── README.md             # This file
├── API_KEYS_SETUP.md     # API key setup guide
├── finance_tools.py      # Finance-related functions
├── news_tools.py         # News-related functions
├── music_tools.py        # Music generation functions
└── data_analysis_tools.py # Data analysis functions
```

## 🔒 Security

- Never commit your `.env` file to version control
- Keep your API keys secure
- Monitor API usage to avoid unexpected charges
- Configure CORS properly for production

## 🚀 Frontend Integration

This API is designed for easy frontend integration:

- **CORS enabled** for cross-origin requests
- **RESTful endpoints** with consistent response format
- **JSON request/response** format
- **Comprehensive error handling**
- **Health check endpoint** for monitoring

### Response Format
All endpoints return JSON responses with the following structure:
```json
{
  "result": "response data",
  "timestamp": "2024-01-01T12:00:00",
  "additional_fields": "..."
}
```

### Error Handling
Errors return HTTP status codes with detailed error messages:
```json
{
  "detail": "Error description"
}
```

## 📊 API Key Setup

See [API_KEYS_SETUP.md](API_KEYS_SETUP.md) for detailed instructions on obtaining and configuring API keys.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🆘 Support

For support and questions:
- Check the API documentation at `/docs`
- Review the health check at `/api/health`
- Check the API information at `/api/info`
