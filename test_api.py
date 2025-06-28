#!/usr/bin/env python3
"""
Test script for MCP AI Assistant API
"""

import requests
import json
import time

def test_api_endpoints():
    """Test all API endpoints"""
    base_url = "http://localhost:8000"
    
    print("🧪 Testing MCP AI Assistant API...")
    print("=" * 50)
    
    # Test health endpoint
    try:
        response = requests.get(f"{base_url}/api/health")
        if response.status_code == 200:
            print("✅ Health check: PASSED")
            health_data = response.json()
            print(f"   Status: {health_data.get('status')}")
            print(f"   Services: {health_data.get('services')}")
        else:
            print(f"❌ Health check: FAILED (Status: {response.status_code})")
    except Exception as e:
        print(f"❌ Health check: ERROR - {e}")
    
    print()
    
    # Test math endpoints
    math_tests = [
        ("add", {"operation": "add", "a": 10, "b": 5}),
        ("multiply", {"operation": "multiply", "a": 6, "b": 7}),
        ("subtract", {"operation": "subtract", "a": 20, "b": 8}),
        ("divide", {"operation": "divide", "a": 15, "b": 3})
    ]
    
    for operation, data in math_tests:
        try:
            response = requests.post(f"{base_url}/api/math/{operation}", json=data)
            if response.status_code == 200:
                result = response.json()
                print(f"✅ Math {operation}: PASSED (Result: {result.get('result')})")
            else:
                print(f"❌ Math {operation}: FAILED (Status: {response.status_code})")
        except Exception as e:
            print(f"❌ Math {operation}: ERROR - {e}")
    
    print()
    
    # Test finance endpoints
    try:
        response = requests.post(f"{base_url}/api/finance/stock-price", json={"symbol": "AAPL"})
        if response.status_code == 200:
            result = response.json()
            print("✅ Stock price: PASSED")
            print(f"   Symbol: {result.get('symbol')}")
        else:
            print(f"❌ Stock price: FAILED (Status: {response.status_code})")
    except Exception as e:
        print(f"❌ Stock price: ERROR - {e}")
    
    print()
    
    # Test news endpoints
    try:
        response = requests.post(f"{base_url}/api/news/breaking")
        if response.status_code == 200:
            result = response.json()
            print("✅ Breaking news: PASSED")
        else:
            print(f"❌ Breaking news: FAILED (Status: {response.status_code})")
    except Exception as e:
        print(f"❌ Breaking news: ERROR - {e}")
    
    print()
    
    # Test web scraping
    try:
        response = requests.post(f"{base_url}/api/web/scrape", 
                               json={"url": "https://example.com", "prompt": "title"})
        if response.status_code == 200:
            result = response.json()
            print("✅ Web scraping: PASSED")
        else:
            print(f"❌ Web scraping: FAILED (Status: {response.status_code})")
    except Exception as e:
        print(f"❌ Web scraping: ERROR - {e}")
    
    print()
    print("=" * 50)
    print("🎯 API Testing Complete!")

def test_tools_directly():
    """Test tools directly without API"""
    print("\n🔧 Testing Tools Directly...")
    print("=" * 50)
    
    # Test finance tools
    try:
        from finance_tools import get_stock_price
        result = get_stock_price("AAPL")
        print("✅ Finance tools: PASSED")
        print(f"   Result preview: {result[:100]}...")
    except Exception as e:
        print(f"❌ Finance tools: ERROR - {e}")
    
    # Test news tools
    try:
        from news_tools import search_breaking_news
        result = search_breaking_news()
        print("✅ News tools: PASSED")
        print(f"   Result preview: {result[:100]}...")
    except Exception as e:
        print(f"❌ News tools: ERROR - {e}")
    
    # Test music tools
    try:
        from music_tools import get_music_generation_status
        result = get_music_generation_status()
        print("✅ Music tools: PASSED")
        print(f"   Result preview: {result[:100]}...")
    except Exception as e:
        print(f"❌ Music tools: ERROR - {e}")
    
    # Test data analysis tools
    try:
        from data_analysis_tools import preprocess_csv_data
        test_data = "name,age,city\nJohn,25,NYC\nJane,30,LA"
        result = preprocess_csv_data(test_data)
        print("✅ Data analysis tools: PASSED")
        print(f"   Result preview: {result[:100]}...")
    except Exception as e:
        print(f"❌ Data analysis tools: ERROR - {e}")

if __name__ == "__main__":
    # Test tools directly first
    test_tools_directly()
    
    # Test API endpoints (if server is running)
    print("\n🌐 Testing API Endpoints...")
    print("Note: Make sure the API server is running (python start_server.py)")
    print("=" * 50)
    
    try:
        test_api_endpoints()
    except Exception as e:
        print(f"❌ API testing failed: {e}")
        print("💡 Make sure to start the server with: python start_server.py") 