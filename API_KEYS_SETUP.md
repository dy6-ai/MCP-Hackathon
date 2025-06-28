# 🔑 API Keys Setup Guide

This guide lists all the API keys required and optional for the MCP AI Assistant project.

## Required API Keys

### 1. OpenAI API Key (Required)
- **Purpose**: Used by ALL AI agents and tools for natural language processing
- **Get it from**: https://platform.openai.com/api-keys
- **Environment Variable**: `OPENAI_API_KEY`
- **Used in**: All Streamlit apps, MCP server, research tools, music generation, data analysis

### 2. ModelsLab API Key (Required for Music Generation)
- **Purpose**: AI music generation using ModelsLab API
- **Get it from**: https://modelslab.com/
- **Environment Variable**: `MODELSLAB_API_KEY`
- **Used in**: music_tools.py, music_app.py, combined_server.py

## Optional API Keys

### 3. Tavily API Key (Optional - Enhanced Web Search)
- **Purpose**: Enhanced web search capabilities
- **Get it from**: https://tavily.com/
- **Environment Variable**: `TAVILY_API_KEY`
- **Used in**: combined_server.py (web_search function)
- **Note**: If not provided, the system uses basic web scraping with requests/BeautifulSoup

## Services That Don't Require API Keys

The following services work without API keys:
- **Yahoo Finance** (`yfinance`) - Free, no API key needed
- **DuckDuckGo Search** (`duckduckgo-search`) - Free, no API key needed
- **Web Scraping** (`requests` + `BeautifulSoup`) - Free, no API key needed
- **Math operations** - Local calculations, no API needed
- **Weather data** - Uses free weather APIs, no key required

## How to Set Up Your .env File

1. Create a file named `.env` in your project root directory
2. Copy the following template and fill in your API keys:

```bash
# MCP AI Assistant - API Keys Configuration

# OpenAI API Key (Required for all AI operations)
OPENAI_API_KEY=your_openai_api_key_here

# ModelsLab API Key (Required for music generation)
MODELSLAB_API_KEY=your_modelslab_api_key_here

# Tavily API Key (Optional - for enhanced web search)
TAVILY_API_KEY=your_tavily_api_key_here

# Environment Configuration
ENVIRONMENT=development
MCP_SERVER_URL=http://localhost:8000/mcp
LOG_LEVEL=INFO
```

## Getting Your API Keys

### OpenAI API Key
1. Go to https://platform.openai.com/api-keys
2. Sign up or log in to your OpenAI account
3. Click "Create new secret key"
4. Copy the key and paste it in your `.env` file
5. **Important**: Keep this key secure and never share it publicly

### ModelsLab API Key
1. Go to https://modelslab.com/
2. Sign up for an account
3. Navigate to API section
4. Generate your API key
5. Copy the key and paste it in your `.env` file

### Tavily API Key (Optional)
1. Go to https://tavily.com/
2. Sign up for a free account
3. Get your API key from the dashboard
4. Copy the key and paste it in your `.env` file

## Testing Your API Keys

After setting up your `.env` file, you can test if the keys are working:

```bash
# Test OpenAI API key
python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('OpenAI API Key:', '✅ Set' if os.getenv('OPENAI_API_KEY') else '❌ Missing')"

# Test ModelsLab API key
python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('ModelsLab API Key:', '✅ Set' if os.getenv('MODELSLAB_API_KEY') else '❌ Missing')"

# Test Tavily API key
python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('Tavily API Key:', '✅ Set' if os.getenv('TAVILY_API_KEY') else '❌ Missing')"
```

## Security Notes

- **Never commit your `.env` file to version control**
- **Keep your API keys secure and private**
- **Monitor your API usage to avoid unexpected charges**
- **Use environment variables in production deployments**

## Troubleshooting

### Common Issues:
1. **"API key not found"**: Make sure your `.env` file is in the project root directory
2. **"Invalid API key"**: Double-check that you copied the key correctly
3. **"Rate limit exceeded"**: You may need to upgrade your API plan or wait

### Getting Help:
- Check the API provider's documentation
- Verify your account status and billing
- Test your keys with the provider's test endpoints

## Cost Estimation

### OpenAI API (GPT-4):
- **Input tokens**: ~$0.03 per 1K tokens
- **Output tokens**: ~$0.06 per 1K tokens
- **Typical conversation**: $0.01-$0.10 per chat

### ModelsLab API:
- **Music generation**: Varies by duration and quality
- **Typical cost**: $0.10-$1.00 per generation

### Tavily API:
- **Free tier**: 1,000 searches per month
- **Paid plans**: Start at $10/month

## Next Steps

Once you have your API keys set up:

1. Start the MCP server: `python combined_server.py`
2. Run the chatbot: `streamlit run chatbot_app.py`
3. Test the features that require your API keys
4. Enjoy your AI assistant! 🚀 