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

---

## 🚀 Quick Start

### 1️⃣ Clone & Setup
```bash
git clone https://github.com/iruventyuma/data-analyst-ai
cd data-analyst-ai
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 2️⃣ Set Environment Variables
Create a `.env` file:
```bash
GROQ_API_KEY=your_groq_api_key_here
```

Get your free Groq API key: https://console.groq.com

### 3️⃣ Run the App
```bash
streamlit run app.py
```

Visit `http://localhost:8501` in your browser.

---

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

## 🎓 Example Use Cases

### Sales Analysis
- Upload: `sales_2024.csv`
- Insights: Top products, regional performance, seasonal trends
- Output: Actionable recommendations for growth

### Customer Analytics
- Upload: `customers.csv`
- Analysis: Churn prediction, segment identification, lifetime value
- Code: Reproducible analysis for team

### Financial Data
- Upload: `transactions.csv`
- Detect: Anomalies, fraud patterns, spending trends
- Questions: "What are unusual transactions?" "Spending trends by category?"

### Survey Results
- Upload: `survey_responses.csv`
- Extract: Key themes, sentiment analysis, demographics
- Report: Structured findings with recommendations

---

## 🔑 Get API Keys

### Groq API (Free!)
1. Go to https://console.groq.com
2. Sign up for free account
3. Create API key
4. Add to `.env` file: `GROQ_API_KEY=your_key`

**Free tier includes:** Fast inference on multiple models!

---

## 📦 Dependencies

```
streamlit==1.40.0
pandas==2.2.0
numpy==1.26.4
plotly==5.18.0
groq==0.4.1
python-dotenv==1.0.0
```

Install all: `pip install -r requirements.txt`

---

## 🚀 Deployment Options

### **Streamlit Cloud (Recommended)**
```bash
git push origin main
# Visit share.streamlit.io → Connect GitHub repo
# Set secrets: GROQ_API_KEY in app settings
```

### **Heroku**
```bash
heroku create your-app-name
git push heroku main
# Set config vars: heroku config:set GROQ_API_KEY=your_key
```

### **Local Server**
```bash
streamlit run app.py
# Access at http://localhost:8501
```

---

## 🎯 Performance

| Metric | Performance |
|--------|-----------|
| **Upload Speed** | <2 seconds (100k+ rows) |
| **Analysis Time** | 3-5 seconds (Groq API) |
| **Visualization** | Instant (interactive Plotly) |
| **Code Generation** | 2-3 seconds |
| **Q&A Response** | 2-4 seconds |

---

## 🛡️ Security

- ✅ API keys stored in `.env` (not in code)
- ✅ No data sent to external servers except Groq API
- ✅ `.env` added to `.gitignore`
- ✅ Support for environment variables

---

## 📸 Screenshots

### Overview Tab
Shows dataset statistics, column info, and data preview

### Insights Tab
AI-generated findings, quality assessment, correlations

### Visualizations Tab
Interactive charts, heatmaps, distributions

### Code Tab
Download reproducible Python code

### Q&A Tab
Ask questions, get AI-powered answers

---

## 🤝 Contributing

Found a bug? Have a feature idea?
1. Fork the repository
2. Create feature branch: `git checkout -b feature/amazing-feature`
3. Commit changes: `git commit -m 'Add amazing feature'`
4. Push to branch: `git push origin feature/amazing-feature`
5. Open a Pull Request

---

## 📝 License

This project is licensed under the **MIT License** - see LICENSE file for details.

---

## 👤 Author

**Uma Iruventyu**
- GitHub: [@iruventyuma](https://github.com/iruventyuma)
- Portfolio: [iruventyuma.github.io](https://iruventyuma.github.io)

---



**⭐ If you find this project useful, please consider giving it a star!**

Last updated: June 2025
