import json
import tempfile
import csv
import pandas as pd
from typing import Optional, Dict, Any
import re
import os
from io import StringIO

def analyze_data_with_sql(data_content: str, user_query: str, openai_api_key: Optional[str] = None) -> str:
    """
    Analyze data using pandas operations and basic SQL-like queries. Use this when users want to analyze data, 
    perform data analysis, query datasets, generate insights from data, or create data reports.
    
    Args:
        data_content: CSV data content as string
        user_query: User's analysis question or request
        openai_api_key: OpenAI API key for the agent (not used in this simplified version)
    
    Returns:
        Analysis results and insights
    """
    try:
        # Import required dependencies
        try:
            import pandas as pd
        except ImportError:
            return """Error: Required dependencies not installed. Please install:
pip install pandas"""
        
        # Read the CSV content into a DataFrame
        df = pd.read_csv(StringIO(data_content), encoding='utf-8', na_values=['NA', 'N/A', 'missing'])
        
        # Analyze the query and perform appropriate operations
        query_lower = user_query.lower()
        
        # Basic data exploration
        if any(word in query_lower for word in ['first', 'rows', 'head', 'show']):
            if 'first' in query_lower or 'head' in query_lower:
                num_rows = 5
                # Extract number if specified
                numbers = re.findall(r'\d+', user_query)
                if numbers:
                    num_rows = min(int(numbers[0]), len(df))
                return f"""📊 First {num_rows} rows of the data:

{df.head(num_rows).to_string()}

**Data Shape**: {df.shape[0]} rows × {df.shape[1]} columns"""
        
        # Column information
        elif any(word in query_lower for word in ['columns', 'column names', 'data types']):
            col_info = []
            for col in df.columns:
                dtype = str(df[col].dtype)
                null_count = df[col].isnull().sum()
                col_info.append(f"- **{col}**: {dtype} ({null_count} null values)")
            
            return f"""📋 Column Information:

**Total Columns**: {len(df.columns)}
**Data Shape**: {df.shape[0]} rows × {df.shape[1]} columns

**Column Details**:
{chr(10).join(col_info)}"""
        
        # Summary statistics
        elif any(word in query_lower for word in ['summary', 'statistics', 'describe', 'mean', 'median', 'std']):
            numeric_cols = df.select_dtypes(include=['number']).columns
            if len(numeric_cols) > 0:
                summary = df[numeric_cols].describe()
                return f"""📈 Summary Statistics for Numeric Columns:

**Numeric Columns**: {list(numeric_cols)}

{summary.to_string()}"""
            else:
                return "❌ No numeric columns found in the dataset for statistical analysis."
        
        # Missing values
        elif any(word in query_lower for word in ['missing', 'null', 'na']):
            missing_data = df.isnull().sum()
            missing_percent = (missing_data / len(df)) * 100
            missing_info = pd.DataFrame({
                'Column': missing_data.index,
                'Missing Count': missing_data.values,
                'Missing Percentage': missing_percent.values
            })
            missing_info = missing_info[missing_info['Missing Count'] > 0]
            
            if len(missing_info) > 0:
                return f"""🔍 Missing Values Analysis:

{missing_info.to_string(index=False)}

**Total Missing Values**: {missing_data.sum()}"""
            else:
                return "✅ No missing values found in the dataset!"
        
        # Unique values
        elif any(word in query_lower for word in ['unique', 'distinct', 'values']):
            unique_counts = df.nunique()
            return f"""🎯 Unique Values Count:

{unique_counts.to_string()}"""
        
        # Correlations
        elif any(word in query_lower for word in ['correlation', 'correlate']):
            numeric_cols = df.select_dtypes(include=['number']).columns
            if len(numeric_cols) > 1:
                corr_matrix = df[numeric_cols].corr()
                return f"""🔗 Correlation Matrix:

{corr_matrix.to_string()}"""
            else:
                return "❌ Need at least 2 numeric columns for correlation analysis."
        
        # Group by operations
        elif any(word in query_lower for word in ['group', 'groupby', 'count', 'average', 'mean']):
            # Try to identify grouping column and aggregation
            words = user_query.split()
            for i, word in enumerate(words):
                if word.lower() in ['by', 'group'] and i + 1 < len(words):
                    group_col = words[i + 1]
                    if group_col in df.columns:
                        if any(agg in query_lower for agg in ['count', 'sum']):
                            result = df.groupby(group_col).size()
                        elif any(agg in query_lower for agg in ['mean', 'average']):
                            numeric_cols = df.select_dtypes(include=['number']).columns
                            if len(numeric_cols) > 0:
                                result = df.groupby(group_col)[numeric_cols].mean()
                            else:
                                return "❌ No numeric columns found for averaging."
                        else:
                            result = df.groupby(group_col).agg(['count', 'mean']).round(2)
                        
                        return f"""📊 Grouped Analysis by '{group_col}':

{result.to_string()}"""
            
            return "❌ Could not identify grouping column. Please specify 'group by [column_name]'."
        
        # Top values
        elif any(word in query_lower for word in ['top', 'highest', 'maximum', 'largest']):
            numbers = re.findall(r'\d+', user_query)
            n = int(numbers[0]) if numbers else 10
            
            # Try to identify the column to sort by
            for col in df.columns:
                if col.lower() in query_lower:
                    if df[col].dtype in ['number']:
                        result = df.nlargest(n, col)
                    else:
                        result = df.head(n)
                    return f"""🏆 Top {n} values by '{col}':

{result.to_string()}"""
            
            # Default to first numeric column
            numeric_cols = df.select_dtypes(include=['number']).columns
            if len(numeric_cols) > 0:
                result = df.nlargest(n, numeric_cols[0])
                return f"""🏆 Top {n} values by '{numeric_cols[0]}':

{result.to_string()}"""
            else:
                return f"""🏆 Top {n} rows:

{df.head(n).to_string()}"""
        
        # Default response
        else:
            return f"""📊 Data Overview:

**Dataset Shape**: {df.shape[0]} rows × {df.shape[1]} columns
**Columns**: {list(df.columns)}
**Data Types**: {dict(df.dtypes)}
**Missing Values**: {df.isnull().sum().sum()} total

**Sample Data**:
{df.head(5).to_string()}

💡 **Try asking for:**
- "Show me the first 10 rows"
- "What are the column names and data types?"
- "Calculate summary statistics"
- "Find missing values"
- "Show correlations between numeric columns"
- "Group by [column] and calculate averages"
- "Show top 5 values by [column]"
"""
                
    except Exception as e:
        return f"Error analyzing data: {str(e)}"

def get_data_analysis_status() -> str:
    """
    Check the status of data analysis capabilities and API key availability.
    Use this to verify if data analysis is properly configured.
    """
    openai_api_key = os.getenv("OPENAI_API_KEY")
    
    status = "📊 Data Analysis Status:\n\n"
    
    if openai_api_key:
        status += "✅ OpenAI API key: Configured\n"
    else:
        status += "❌ OpenAI API key: Not configured\n"
    
    try:
        import pandas
        status += "✅ Pandas library: Installed\n"
    except ImportError:
        status += "❌ Pandas library: Not installed (run: pip install pandas)\n"
    
    try:
        import duckdb
        status += "✅ DuckDB library: Installed\n"
    except ImportError:
        status += "❌ DuckDB library: Not installed (run: pip install duckdb)\n"
    
    if openai_api_key:
        status += "\n🎉 Data analysis is ready to use!"
    else:
        status += "\n⚠️ Please configure OpenAI API key to enable data analysis."
    
    return status

def preprocess_csv_data(csv_content: str) -> str:
    """
    Preprocess CSV data for better analysis. Use this to clean and prepare data before analysis.
    
    Args:
        csv_content: Raw CSV content as string
    
    Returns:
        Preprocessed CSV content
    """
    try:
        # Read the CSV content into a DataFrame
        df = pd.read_csv(StringIO(csv_content), encoding='utf-8', na_values=['NA', 'N/A', 'missing'])
        
        # Ensure string columns are properly quoted
        for col in df.select_dtypes(include=['object']):
            df[col] = df[col].astype(str).replace({r'"': '""'}, regex=True)
        
        # Parse dates and numeric columns
        for col in df.columns:
            if 'date' in col.lower():
                df[col] = pd.to_datetime(df[col], errors='coerce')
            elif df[col].dtype == 'object':
                try:
                    df[col] = pd.to_numeric(df[col])
                except (ValueError, TypeError):
                    # Keep as is if conversion fails
                    pass
        
        # Convert back to CSV string
        output = df.to_csv(index=False, quoting=csv.QUOTE_ALL)
        
        return f"""✅ Data preprocessing completed!

**Original columns**: {list(df.columns)}
**Data shape**: {df.shape[0]} rows × {df.shape[1]} columns
**Data types**: {dict(df.dtypes)}

**Preprocessed data**:
```csv
{output[:1000]}{'...' if len(output) > 1000 else ''}
```"""
        
    except Exception as e:
        return f"Error preprocessing data: {str(e)}" 