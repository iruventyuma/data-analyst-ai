# GenAI Data Analysis Assistant - Complete Setup Guide

## 🚀 Getting Started

### Step 1: Clone the Repository
```bash
git clone https://github.com/iruventyuma/data-analyst-ai
cd data-analyst-ai
```

### Step 2: Create Virtual Environment
```bash
# Create virtual environment
python -m venv venv

# Activate it
# On Linux/Mac:
source venv/bin/activate

# On Windows:
venv\Scripts\activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Set Up API Key
**Get your Anthropic API key:**
1. Go to https://console.anthropic.com
2. Sign up/login
3. Create API key from dashboard
4. Copy the key

**Add to environment:**
```bash
# Create .env file
cp .env.example .env

# Edit .env and paste your API key
ANTHROPIC_API_KEY=sk-ant-xxxxx...
```

### Step 5: Run the App
```bash
streamlit run app.py
```

The app will open at `http://localhost:8501`

---

## 📊 Features Explained

### Tab 1: Overview
- **Dataset Overview**: Shape, data types, missing values
- **Column Information**: Detailed column statistics
- **Data Preview**: First 10 rows
- **Statistical Summary**: Mean, median, std, min, max for numeric columns

### Tab 2: Insights
- **AI-Powered Analysis**: Claude analyzes your data and provides:
  - Key findings and patterns
  - Data quality issues
  - Correlations and relationships
  - Actionable recommendations
  - Visualization suggestions

### Tab 3: Visualizations
- **Distributions**: Histograms and boxplots for numeric columns
- **Categories**: Bar charts for categorical columns
- **Correlations**: Heatmap showing relationships between variables
- **Missing Data**: Visualization of missing value patterns

### Tab 4: Code
- **Reproducible Python Code**: Claude generates analysis code
- **Download**: Save code to file for local execution
- **Modification**: Adapt code for your specific needs

### Tab 5: Ask Questions
- **Interactive Q&A**: Ask Claude questions about your data
- **Natural Language**: Use plain English queries
- **Data-Driven Answers**: Responses based on actual analysis

---

## 💡 Example Use Cases

### Sales Data Analysis
1. Upload sales.csv
2. Generate insights → Find top products, seasonal patterns
3. Visualize revenue trends
4. Ask: "What's driving sales growth?"
5. Download analysis code

### Customer Data
1. Upload customers.csv
2. Detect churn patterns, segment analysis
3. Visualize customer distributions
4. Ask: "Which customer segments are most valuable?"

### Financial Data
1. Upload financial_data.csv
2. Identify anomalies and outliers
3. Analyze correlations between metrics
4. Ask: "Are there any concerning financial trends?"

---

## 🔧 Technical Details

### Data Processing (data_processor.py)
- Automatic exploration of dataset structure
- Statistical analysis for numeric columns
- Category value counting
- Anomaly detection using IQR method
- Correlation analysis
- Missing data pattern detection
- Distribution insights (skewness, kurtosis)

### Visualization (visualization.py)
- Histograms with 30 bins
- Boxplots with mean/std
- Correlation heatmaps
- Bar charts for categories
- Scatter plot matrices
- Missing data visualization
- All using interactive Plotly charts

### Analysis (analyzer.py)
- Claude 3.5 Sonnet integration via LangChain
- Generates insights from analysis results
- Creates reproducible Python code
- Answers custom questions
- Generates comprehensive reports

### Frontend (app.py)
- Streamlit-based web interface
- Multi-tab layout for organization
- Session state management
- API key handling
- File upload with validation
- Responsive design

---

## 📈 Project Structure

```
data-analyst-ai/
├── app.py                    # Main Streamlit app
├── analyzer.py              # Claude + LangChain integration
├── data_processor.py        # Data analysis logic
├── visualization.py         # Chart generation
├── requirements.txt         # Python dependencies
├── .env.example            # Environment template
├── .gitignore              # Git ignore file
├── README.md               # Project readme
└── SETUP_GUIDE.md         # This file
```

---

## 🚀 Deployment

### Deploy to Streamlit Cloud (Free)

1. Push code to GitHub:
```bash
git init
git add .
git commit -m "Initial commit"
git push origin main
```

2. Go to https://share.streamlit.io
3. Click "New app"
4. Select repository, branch, and file
5. Set secrets (ANTHROPIC_API_KEY)
6. Deploy!

### Deploy to Other Platforms
- Heroku
- AWS
- Google Cloud
- Azure

---

## 📝 Tips & Best Practices

### Data Preparation
- Ensure CSV has proper column headers
- Clean data before uploading
- Handle missing values appropriately
- Remove duplicates if applicable

### API Key Security
- Never commit .env file
- Use GitHub secrets for CI/CD
- Rotate keys regularly
- Monitor API usage

### Performance
- Large datasets (>100k rows) may be slow
- Consider sampling for initial analysis
- Optimize visualizations for your data size

### Custom Extensions
- Add your own visualization types
- Create specialized analyzers
- Build domain-specific prompts
- Integrate with other data sources

---

## ❓ FAQ

**Q: What CSV formats are supported?**
A: Standard CSV files with comma delimiters. Excel files need to be saved as CSV first.

**Q: How much does it cost to use?**
A: The app itself is free (open source). You only pay for Claude API usage (~$0.003 per 1K tokens).

**Q: What's the maximum file size?**
A: Theoretically unlimited, but larger files may timeout. Test with 1M+ rows.

**Q: Can I use other LLMs?**
A: Yes! Modify analyzer.py to use Groq, Cohere, or other providers.

**Q: How do I customize the insights?**
A: Edit the prompts in analyzer.py to match your needs.

---

## 🤝 Contributing

Want to improve the project?
1. Fork the repository
2. Create feature branch
3. Make changes
4. Submit pull request

---

## 📚 Resources

- [Streamlit Docs](https://docs.streamlit.io)
- [LangChain Docs](https://python.langchain.com)
- [Claude API Docs](https://docs.anthropic.com)
- [Plotly Python](https://plotly.com/python)
- [Pandas Documentation](https://pandas.pydata.org)

---

## 📧 Support

Issues? Questions?
- Open GitHub issue
- Check existing discussions
- Review error messages carefully

---

Happy analyzing! 📊✨
