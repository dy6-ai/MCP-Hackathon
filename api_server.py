"""
Optimized MCP API Server for Frontend Integration
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional
import os
from datetime import datetime

# Import all tools
from finance_tools import (
    get_stock_price, get_stock_fundamentals, get_analyst_recommendations,
    get_market_news, calculate_portfolio_value, get_crypto_price, get_economic_indicators
)
from news_tools import (
    search_news_articles, search_breaking_news, search_tech_news, search_business_news,
    search_sports_news, search_science_news, create_news_summary, search_company_news
)
from music_tools import generate_music, get_music_generation_status
from data_analysis_tools import analyze_data_with_sql, get_data_analysis_status, preprocess_csv_data

# Web scraping imports
import requests
from bs4 import BeautifulSoup

app = FastAPI(
    title="MCP AI Assistant API",
    description="Comprehensive AI Assistant with multiple tools and capabilities",
    version="1.0.0"
)

# CORS middleware for frontend integration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Configure this properly for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Pydantic models
class MathRequest(BaseModel):
    operation: str
    a: float
    b: float

class StockRequest(BaseModel):
    symbol: str

class NewsRequest(BaseModel):
    topic: str
    max_results: Optional[int] = 5

class MusicRequest(BaseModel):
    prompt: str
    openai_api_key: Optional[str] = None
    models_lab_api_key: Optional[str] = None

class DataAnalysisRequest(BaseModel):
    data_content: str
    user_query: str
    openai_api_key: Optional[str] = None

class WebScrapeRequest(BaseModel):
    url: str
    prompt: str

class WebSearchRequest(BaseModel):
    query: str

# Math Operations
@app.post("/api/math/add")
async def add_numbers(request: MathRequest):
    """Add two numbers"""
    try:
        result = request.a + request.b
        return {"result": result, "operation": "addition", "inputs": [request.a, request.b]}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/api/math/multiply")
async def multiply_numbers(request: MathRequest):
    """Multiply two numbers"""
    try:
        result = request.a * request.b
        return {"result": result, "operation": "multiplication", "inputs": [request.a, request.b]}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/api/math/subtract")
async def subtract_numbers(request: MathRequest):
    """Subtract two numbers"""
    try:
        result = request.a - request.b
        return {"result": result, "operation": "subtraction", "inputs": [request.a, request.b]}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/api/math/divide")
async def divide_numbers(request: MathRequest):
    """Divide two numbers"""
    try:
        if request.b == 0:
            raise HTTPException(status_code=400, detail="Cannot divide by zero")
        result = request.a / request.b
        return {"result": result, "operation": "division", "inputs": [request.a, request.b]}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# Finance Tools
@app.post("/api/finance/stock-price")
async def get_stock_price_api(request: StockRequest):
    """Get stock price"""
    try:
        result = get_stock_price(request.symbol)
        return {"symbol": request.symbol, "result": result, "timestamp": datetime.now().isoformat()}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/api/finance/stock-fundamentals")
async def get_stock_fundamentals_api(request: StockRequest):
    """Get stock fundamentals"""
    try:
        result = get_stock_fundamentals(request.symbol)
        return {"symbol": request.symbol, "result": result, "timestamp": datetime.now().isoformat()}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/api/finance/crypto-price")
async def get_crypto_price_api(request: StockRequest):
    """Get cryptocurrency price"""
    try:
        result = get_crypto_price(request.symbol)
        return {"symbol": request.symbol, "result": result, "timestamp": datetime.now().isoformat()}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# News Tools
@app.post("/api/news/search")
async def search_news_articles_api(request: NewsRequest):
    """Search news articles"""
    try:
        max_results = request.max_results or 5
        result = search_news_articles(request.topic, max_results)
        return {"topic": request.topic, "result": result, "timestamp": datetime.now().isoformat()}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/api/news/breaking")
async def search_breaking_news_api():
    """Get breaking news"""
    try:
        result = search_breaking_news()
        return {"result": result, "timestamp": datetime.now().isoformat()}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# Music Generation
@app.post("/api/music/generate")
async def generate_music_api(request: MusicRequest):
    """Generate music"""
    try:
        openai_key = request.openai_api_key or os.getenv("OPENAI_API_KEY")
        models_lab_key = request.models_lab_api_key or os.getenv("MODELSLAB_API_KEY")
        
        if not openai_key or not models_lab_key:
            raise HTTPException(
                status_code=400, 
                detail="Both OpenAI and ModelsLab API keys are required for music generation"
            )
        
        result = generate_music(request.prompt, openai_key, models_lab_key)
        return {"prompt": request.prompt, "result": result, "timestamp": datetime.now().isoformat()}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# Data Analysis
@app.post("/api/data/analyze")
async def analyze_data_api(request: DataAnalysisRequest):
    """Analyze data"""
    try:
        openai_key = request.openai_api_key or os.getenv("OPENAI_API_KEY")
        
        if not openai_key:
            raise HTTPException(
                status_code=400, 
                detail="OpenAI API key is required for data analysis"
            )
        
        result = analyze_data_with_sql(request.data_content, request.user_query, openai_key)
        return {
            "data_content": request.data_content[:100] + "...", 
            "query": request.user_query, 
            "result": result, 
            "timestamp": datetime.now().isoformat()
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# Web Scraping
@app.post("/api/web/scrape")
async def scrape_website(request: WebScrapeRequest):
    """Scrape website content"""
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        
        response = requests.get(request.url, headers=headers, timeout=10)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Remove script and style elements
        for script in soup(["script", "style"]):
            script.decompose()
        
        text = soup.get_text()
        lines = (line.strip() for line in text.splitlines())
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        text = ' '.join(chunk for chunk in chunks if chunk)
        
        # Extract based on prompt
        prompt_lower = request.prompt.lower()
        
        if 'title' in prompt_lower:
            title = soup.find('title')
            result = title.get_text() if title else 'No title found'
        elif 'headings' in prompt_lower:
            headings = soup.find_all(['h1', 'h2', 'h3'])
            result = [h.get_text().strip() for h in headings[:5]]
        elif 'links' in prompt_lower:
            links = soup.find_all('a', href=True)
            result = [link.get_text().strip() for link in links[:10]]
        else:
            result = text[:500] + "..." if len(text) > 500 else text
        
        return {
            "url": request.url,
            "prompt": request.prompt,
            "result": result,
            "timestamp": datetime.now().isoformat()
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# Health check
@app.get("/api/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "timestamp": datetime.now().isoformat(),
        "version": "1.0.0",
        "services": ["math", "finance", "news", "music", "data_analysis", "web_scraping"]
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000) 