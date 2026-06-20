# 📊 GenAI Data Analysis Assistant

An intelligent data analysis tool that uses Claude AI to automatically explore datasets, generate insights, detect anomalies, and create visualizations.

## ✨ Features

- **Automatic Data Exploration** - Upload CSV → AI explores structure, types, distributions
- **Intelligent Insights** - Detects trends, correlations, anomalies, patterns
- **Smart Visualizations** - Auto-generates relevant charts and graphs
- **Code Generation** - Produces reproducible Python analysis code
- **Detailed Reports** - Structured analysis with key findings and recommendations

## 🛠️ Tech Stack

- **Backend**: Claude API (via LangChain)
- **Frontend**: Streamlit
- **Data Processing**: Pandas, NumPy
- **Visualization**: Plotly
- **Language**: Python 3.9+

## 🚀 Quick Start

### 1. Clone & Setup
```bash
git clone https://github.com/iruventyuma/data-analyst-ai
cd data-analyst-ai
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Set Environment Variables
```bash
export ANTHROPIC_API_KEY="your-api-key-here"
```

### 3. Run the App
```bash
streamlit run app.py
```

Visit `http://localhost:8501` in your browser.

## 📁 Project Structure

```
data-analyst-ai/
├── app.py                 # Main Streamlit app
├── analyzer.py            # LangChain + Claude integration
├── data_processor.py      # Data exploration & processing
├── visualization.py       # Chart generation
├── utils.py              # Helper functions
├── requirements.txt      # Dependencies
├── .env.example          # Environment template
└── README.md
```

## 💡 How It Works

1. **Upload CSV** → App reads and validates data
2. **Explore Data** → Analyzer examines structure, stats, data types
3. **Generate Insights** → Claude identifies patterns, trends, anomalies
4. **Create Visualizations** → System generates relevant plots
5. **Generate Report** → Structured findings + code artifacts

## 🎯 Example Use Cases

- Sales data analysis → Identify top performers, seasonal trends
- Customer data → Detect churn patterns, segment analysis
- Financial data → Anomaly detection, correlation analysis
- Survey responses → Sentiment analysis, key themes
- Time series data → Trend forecasting, seasonality detection

## 📈 Deployment

Deploy to **Streamlit Cloud** (free):
```bash
git push origin main
# Visit share.streamlit.io → Connect GitHub repo
```

## 🔑 API Keys

Get free Anthropic API key: https://console.anthropic.com

## 📝 License

MIT

## 👤 Author

Created by [iruventyuma](https://github.com/iruventyuma)
