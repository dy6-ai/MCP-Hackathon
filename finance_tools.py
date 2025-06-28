"""
Finance tools for MCP server
"""

import yfinance as yf
import requests
from typing import Dict, List, Any
import json

def get_stock_price(symbol: str) -> str:
    """Get current stock price for a given symbol. Use this when users ask about stock prices, share prices, or current market value."""
    try:
        ticker = yf.Ticker(symbol.upper())
        info = ticker.info
        
        if 'regularMarketPrice' in info and info['regularMarketPrice']:
            price = info['regularMarketPrice']
            currency = info.get('currency', 'USD')
            company_name = info.get('longName', symbol.upper())
            
            return f"""
**Stock Price for {company_name} ({symbol.upper()})**
- **Current Price**: {price} {currency}
- **Previous Close**: {info.get('previousClose', 'N/A')} {currency}
- **Market Cap**: {info.get('marketCap', 'N/A')} {currency}
- **Volume**: {info.get('volume', 'N/A')}
- **52 Week High**: {info.get('fiftyTwoWeekHigh', 'N/A')} {currency}
- **52 Week Low**: {info.get('fiftyTwoWeekLow', 'N/A')} {currency}
"""
        else:
            return f"Could not retrieve stock price for {symbol.upper()}. Please check the symbol and try again."
            
    except Exception as e:
        return f"Error retrieving stock price for {symbol}: {str(e)}"

def get_stock_fundamentals(symbol: str) -> str:
    """Get fundamental financial data for a stock. Use this when users ask about financial ratios, earnings, revenue, or fundamental analysis."""
    try:
        ticker = yf.Ticker(symbol.upper())
        info = ticker.info
        
        fundamentals = f"""
**Fundamental Analysis for {info.get('longName', symbol.upper())} ({symbol.upper()})**

**Valuation Metrics:**
- **P/E Ratio**: {info.get('trailingPE', 'N/A')}
- **Forward P/E**: {info.get('forwardPE', 'N/A')}
- **PEG Ratio**: {info.get('pegRatio', 'N/A')}
- **Price to Book**: {info.get('priceToBook', 'N/A')}
- **Enterprise Value**: {info.get('enterpriseValue', 'N/A')}

**Financial Performance:**
- **Revenue**: {info.get('totalRevenue', 'N/A')}
- **Profit Margin**: {info.get('profitMargins', 'N/A')}
- **Operating Margin**: {info.get('operatingMargins', 'N/A')}
- **Return on Equity**: {info.get('returnOnEquity', 'N/A')}
- **Return on Assets**: {info.get('returnOnAssets', 'N/A')}

**Dividend Information:**
- **Dividend Yield**: {info.get('dividendYield', 'N/A')}
- **Dividend Rate**: {info.get('dividendRate', 'N/A')}
- **Payout Ratio**: {info.get('payoutRatio', 'N/A')}
"""
        
        return fundamentals
        
    except Exception as e:
        return f"Error retrieving fundamentals for {symbol}: {str(e)}"

def get_analyst_recommendations(symbol: str) -> str:
    """Get analyst recommendations and ratings for a stock. Use this when users ask about analyst opinions, buy/sell ratings, or investment recommendations."""
    try:
        ticker = yf.Ticker(symbol.upper())
        recommendations = ticker.recommendations
        
        if recommendations is not None and not recommendations.empty:
            # Get the latest recommendations
            latest = recommendations.tail(10)
            
            result = f"**Analyst Recommendations for {symbol.upper()}**\n\n"
            
            for _, row in latest.iterrows():
                result += f"- **{row['To Grade']}** by {row['Firm']} on {row.name.strftime('%Y-%m-%d')}\n"
                if 'Action' in row and pd.notna(row['Action']):
                    result += f"  Action: {row['Action']}\n"
                result += "\n"
            
            return result
        else:
            return f"No analyst recommendations found for {symbol.upper()}"
            
    except Exception as e:
        return f"Error retrieving analyst recommendations for {symbol}: {str(e)}"

def get_market_news(query: str = "stock market") -> str:
    """Get latest financial and market news. Use this when users ask about market news, financial news, or current events affecting the market."""
    try:
        # Simple news search using DuckDuckGo (no API key needed)
        search_url = f"https://api.duckduckgo.com/?q={query}&format=json&no_html=1&skip_disambig=1"
        
        response = requests.get(search_url, timeout=10)
        response.raise_for_status()
        
        data = response.json()
        
        if 'AbstractText' in data and data['AbstractText']:
            return f"""
**Latest Financial News: {query}**

**Summary:**
{data['AbstractText']}

**Source:** {data.get('AbstractSource', 'DuckDuckGo')}
**URL:** {data.get('AbstractURL', 'N/A')}
"""
        else:
            return f"Could not retrieve news for '{query}'. Please try a different search term."
            
    except Exception as e:
        return f"Error retrieving market news: {str(e)}"

def calculate_portfolio_value(holdings: str) -> str:
    """Calculate the current value of a portfolio. Use this when users want to calculate portfolio value, track investments, or analyze holdings."""
    try:
        # Parse holdings (format: "AAPL:100,GOOGL:50,MSFT:75")
        holdings_dict = {}
        for holding in holdings.split(','):
            if ':' in holding:
                symbol, shares = holding.strip().split(':')
                holdings_dict[symbol.strip().upper()] = int(shares)
        
        total_value = 0
        portfolio_details = []
        
        for symbol, shares in holdings_dict.items():
            try:
                ticker = yf.Ticker(symbol)
                price = ticker.info.get('regularMarketPrice', 0)
                value = price * shares
                total_value += value
                
                portfolio_details.append(f"- **{symbol}**: {shares} shares @ ${price:.2f} = ${value:.2f}")
                
            except Exception as e:
                portfolio_details.append(f"- **{symbol}**: Error retrieving data - {str(e)}")
        
        result = f"""
**Portfolio Analysis**

**Holdings:**
{chr(10).join(portfolio_details)}

**Total Portfolio Value: ${total_value:.2f}**
"""
        
        return result
        
    except Exception as e:
        return f"Error calculating portfolio value: {str(e)}"

def get_crypto_price(symbol: str) -> str:
    """Get current cryptocurrency price. Use this when users ask about crypto prices, Bitcoin, Ethereum, or other digital currencies."""
    try:
        # Add USD suffix for crypto symbols
        if not symbol.endswith('-USD'):
            symbol = f"{symbol.upper()}-USD"
        
        ticker = yf.Ticker(symbol)
        info = ticker.info
        
        if 'regularMarketPrice' in info and info['regularMarketPrice']:
            price = info['regularMarketPrice']
            
            return f"""
**Cryptocurrency Price: {symbol.replace('-USD', '')}**

- **Current Price**: ${price:,.2f} USD
- **24h Change**: {info.get('regularMarketChangePercent', 'N/A')}%
- **24h Volume**: {info.get('volume', 'N/A')}
- **Market Cap**: ${info.get('marketCap', 'N/A'):,.0f} USD
- **Circulating Supply**: {info.get('circulatingSupply', 'N/A'):,.0f}
"""
        else:
            return f"Could not retrieve price for {symbol.replace('-USD', '')}. Please check the symbol."
            
    except Exception as e:
        return f"Error retrieving crypto price for {symbol}: {str(e)}"

def get_economic_indicators() -> str:
    """Get key economic indicators and market data. Use this when users ask about economic data, market indicators, or macroeconomic trends."""
    try:
        # Get key economic indicators using Yahoo Finance
        indicators = {
            '^GSPC': 'S&P 500',
            '^DJI': 'Dow Jones',
            '^IXIC': 'NASDAQ',
            '^VIX': 'Volatility Index',
            'GC=F': 'Gold Futures',
            'CL=F': 'Crude Oil Futures',
            'DX-Y.NYB': 'US Dollar Index'
        }
        
        result = "**Key Economic Indicators**\n\n"
        
        for symbol, name in indicators.items():
            try:
                ticker = yf.Ticker(symbol)
                info = ticker.info
                
                if 'regularMarketPrice' in info and info['regularMarketPrice']:
                    price = info['regularMarketPrice']
                    change = info.get('regularMarketChangePercent', 0)
                    change_symbol = "📈" if change > 0 else "📉" if change < 0 else "➡️"
                    
                    result += f"{change_symbol} **{name}**: ${price:,.2f} ({change:+.2f}%)\n"
                    
            except Exception as e:
                result += f"❌ **{name}**: Error retrieving data\n"
        
        return result
        
    except Exception as e:
        return f"Error retrieving economic indicators: {str(e)}" 