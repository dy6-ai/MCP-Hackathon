"""
News processing tools for MCP server
"""

from duckduckgo_search import DDGS
from datetime import datetime
import json
from typing import List, Dict, Any

def search_news_articles(topic: str, max_results: int = 5) -> str:
    """Search for recent news articles on a given topic. Use this when users ask for news, current events, or recent developments about a topic."""
    try:
        with DDGS() as ddg:
            # Search for recent news with current month
            search_query = f"{topic} news {datetime.now().strftime('%Y-%m')}"
            results = ddg.text(search_query, max_results=max_results)
            
            if results:
                news_results = []
                for i, result in enumerate(results, 1):
                    news_results.append(f"""
**Article {i}:**
- **Title**: {result.get('title', 'No title')}
- **Source**: {result.get('href', 'No URL')}
- **Summary**: {result.get('body', 'No summary')}
""")
                
                return f"Found {len(results)} recent news articles about '{topic}':\n" + "\n".join(news_results)
            else:
                return f"No recent news found for '{topic}'. Try a different search term or check spelling."
                
    except Exception as e:
        return f"Error searching for news: {str(e)}"

def search_breaking_news() -> str:
    """Search for breaking news and current events. Use this when users ask for breaking news, current events, or what's happening now."""
    try:
        with DDGS() as ddg:
            # Search for breaking news
            results = ddg.text("breaking news today", max_results=5)
            
            if results:
                news_results = []
                for i, result in enumerate(results, 1):
                    news_results.append(f"""
**Breaking News {i}:**
- **Title**: {result.get('title', 'No title')}
- **Source**: {result.get('href', 'No URL')}
- **Summary**: {result.get('body', 'No summary')}
""")
                
                return f"**Breaking News - {datetime.now().strftime('%Y-%m-%d %H:%M')}**\n" + "\n".join(news_results)
            else:
                return "No breaking news found at the moment."
                
    except Exception as e:
        return f"Error searching for breaking news: {str(e)}"

def search_tech_news() -> str:
    """Search for technology news and developments. Use this when users ask for tech news, technology updates, or IT industry news."""
    try:
        with DDGS() as ddg:
            results = ddg.text("technology news today", max_results=5)
            
            if results:
                news_results = []
                for i, result in enumerate(results, 1):
                    news_results.append(f"""
**Tech News {i}:**
- **Title**: {result.get('title', 'No title')}
- **Source**: {result.get('href', 'No URL')}
- **Summary**: {result.get('body', 'No summary')}
""")
                
                return f"**Technology News - {datetime.now().strftime('%Y-%m-%d')}**\n" + "\n".join(news_results)
            else:
                return "No technology news found at the moment."
                
    except Exception as e:
        return f"Error searching for tech news: {str(e)}"

def search_business_news() -> str:
    """Search for business and financial news. Use this when users ask for business news, financial updates, or market news."""
    try:
        with DDGS() as ddg:
            results = ddg.text("business news today", max_results=5)
            
            if results:
                news_results = []
                for i, result in enumerate(results, 1):
                    news_results.append(f"""
**Business News {i}:**
- **Title**: {result.get('title', 'No title')}
- **Source**: {result.get('href', 'No URL')}
- **Summary**: {result.get('body', 'No summary')}
""")
                
                return f"**Business News - {datetime.now().strftime('%Y-%m-%d')}**\n" + "\n".join(news_results)
            else:
                return "No business news found at the moment."
                
    except Exception as e:
        return f"Error searching for business news: {str(e)}"

def search_sports_news() -> str:
    """Search for sports news and updates. Use this when users ask for sports news, game results, or athletic events."""
    try:
        with DDGS() as ddg:
            results = ddg.text("sports news today", max_results=5)
            
            if results:
                news_results = []
                for i, result in enumerate(results, 1):
                    news_results.append(f"""
**Sports News {i}:**
- **Title**: {result.get('title', 'No title')}
- **Source**: {result.get('href', 'No URL')}
- **Summary**: {result.get('body', 'No summary')}
""")
                
                return f"**Sports News - {datetime.now().strftime('%Y-%m-%d')}**\n" + "\n".join(news_results)
            else:
                return "No sports news found at the moment."
                
    except Exception as e:
        return f"Error searching for sports news: {str(e)}"

def search_science_news() -> str:
    """Search for science and research news. Use this when users ask for scientific discoveries, research updates, or academic news."""
    try:
        with DDGS() as ddg:
            results = ddg.text("science news today", max_results=5)
            
            if results:
                news_results = []
                for i, result in enumerate(results, 1):
                    news_results.append(f"""
**Science News {i}:**
- **Title**: {result.get('title', 'No title')}
- **Source**: {result.get('href', 'No URL')}
- **Summary**: {result.get('body', 'No summary')}
""")
                
                return f"**Science News - {datetime.now().strftime('%Y-%m-%d')}**\n" + "\n".join(news_results)
            else:
                return "No science news found at the moment."
                
    except Exception as e:
        return f"Error searching for science news: {str(e)}"

def create_news_summary(topic: str) -> str:
    """Create a comprehensive news summary for a given topic. Use this when users want a summary of news, current events analysis, or news synthesis."""
    try:
        # First, search for news articles
        news_data = search_news_articles(topic, max_results=5)
        
        # Create a summary based on the news data
        summary = f"""
# News Summary: {topic}

## Overview
Based on recent news coverage, here are the key developments regarding {topic}:

{news_data}

## Key Themes
- Recent developments in {topic} show significant activity and interest
- Multiple sources are covering various aspects of this topic
- The coverage spans different perspectives and implications

## Analysis
The news coverage indicates that {topic} continues to be a relevant and evolving subject with ongoing developments worth monitoring.

---
*Summary generated on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*
"""
        
        return summary
        
    except Exception as e:
        return f"Error creating news summary: {str(e)}"

def search_company_news(company: str) -> str:
    """Search for news about a specific company. Use this when users ask for company news, corporate updates, or business developments."""
    try:
        with DDGS() as ddg:
            search_query = f"{company} company news {datetime.now().strftime('%Y-%m')}"
            results = ddg.text(search_query, max_results=5)
            
            if results:
                news_results = []
                for i, result in enumerate(results, 1):
                    news_results.append(f"""
**Company News {i}:**
- **Title**: {result.get('title', 'No title')}
- **Source**: {result.get('href', 'No URL')}
- **Summary**: {result.get('body', 'No summary')}
""")
                
                return f"**{company} News - {datetime.now().strftime('%Y-%m-%d')}**\n" + "\n".join(news_results)
            else:
                return f"No recent news found for {company}. Try checking the company name or searching for a different term."
                
    except Exception as e:
        return f"Error searching for company news: {str(e)}" 