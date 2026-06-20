# 📊 GenAI Data Analysis Assistant

An intelligent data analysis tool that uses **Groq AI** to automatically explore datasets, generate insights, detect anomalies, and create interactive visualizations.

**Live Demo:** [GitHub Repository](https://github.com/iruventyuma/data-analyst-ai)

---

## ✨ Features

- **📈 Automatic Data Exploration** - Upload CSV → AI explores structure, types, distributions
- **🧠 AI-Powered Insights** - Detects trends, correlations, anomalies, and patterns
- **📊 Interactive Visualizations** - Auto-generates relevant Plotly charts and graphs
- **💻 Code Generation** - Produces reproducible Python analysis code
- **❓ Smart Q&A** - Ask natural language questions about your data
- **🎯 Data Quality Reports** - Identifies missing data, outliers, and inconsistencies

---

## 🛠️ Tech Stack

| Component | Technology |
|-----------|-----------|
| **AI/LLM** | Groq API (gemma2-9b-it) |
| **Frontend** | Streamlit |
| **Data Processing** | Pandas, NumPy |
| **Visualization** | Plotly |
| **Language** | Python 3.9+ |

--

## 📁 Project Structure

```
data-analyst-ai/
├── app.py                 # Main Streamlit application (5 tabs)
├── analyzer.py            # Groq AI integration & analysis
├── data_processor.py      # Data exploration & statistics
├── visualization.py       # Interactive Plotly charts
├── requirements.txt       # Python dependencies
├── .env                   # API keys (create from .env.example)
├── .gitignore            # Git configuration
└── README.md             # This file
```

---

## 🎯 5 Main Features

### 📈 Overview Tab
- Dataset shape, columns, data types
- Missing values & duplicates count
- Data preview (first 10 rows)
- Statistical summaries

### 🔍 Insights Tab
- **AI-powered analysis** using Groq
- Key findings and patterns
- Data quality assessment
- Correlations & relationships
- Actionable recommendations

### 📊 Visualizations Tab
- Distribution plots (histograms, boxplots)
- Categorical value counts
- Correlation heatmaps
- Missing data visualization
- All interactive with Plotly

### 💻 Code Tab
- **One-click code generation**
- Reproducible Python code
- Download as `.py` file
- Ready to use locally

### ❓ Ask Questions Tab
- Natural language queries about data
- Example: "What are the top factors affecting sales?"
- AI-powered answers based on analysis

---

## 💡 How It Works

```
1. Upload CSV File
        ↓
2. Data Processing (Pandas)
   ├── Structure analysis
   ├── Statistics calculation
   └── Anomaly detection
        ↓
3. Groq AI Analysis
   ├── Pattern detection
   ├── Insight generation
   └── Trend identification
        ↓
4. Visualization (Plotly)
   ├── Interactive charts
   ├── Correlation heatmaps
   └── Distribution plots
        ↓
5. User Interaction
   ├── View insights
   ├── Generate code
   └── Ask questions
```

---


## 👤 Author

**Uma Iruventyu**
- GitHub: [@iruventyuma](https://github.com/iruventyuma)
- Portfolio: [iruventyuma.github.io](https://iruventyuma.github.io)

---


