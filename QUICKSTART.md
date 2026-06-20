# Quick Start - 5 Minutes ⚡

## 1️⃣ Clone & Setup
```bash
git clone https://github.com/iruventyuma/data-analyst-ai
cd data-analyst-ai
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## 2️⃣ Get API Key
- Go to https://console.anthropic.com
- Create API key
- Copy it

## 3️⃣ Run App
```bash
streamlit run app.py
```

## 4️⃣ Upload Data
- Open http://localhost:8501
- Paste API key in sidebar
- Upload CSV file
- Click "Generate Insights"

## 5️⃣ Explore
- View overview & statistics
- Generate AI insights
- Check visualizations
- Download code
- Ask questions

---

## Test with Sample Data
We've included `sample_sales_data.csv` - upload this to test all features!

---

## Expected Output

### Overview Tab
```
Dataset: 365 rows × 10 columns
Missing values: 20
Statistics for: Sales, Quantity, Age, Satisfaction Score, Profit, Revenue
```

### Insights Tab
```
🎯 Key Findings:
- Sales peak in Q4 (holiday season)
- Laptop products have highest margins
- Discount reduces profit significantly

✅ Data Quality:
- 20 missing values in Customer_Age
- No duplicates found
- 3 outliers in Sales column

🔗 Correlations:
- Sales ↔ Profit: 0.95
- Quantity ↔ Revenue: 0.92
```

### Visualizations
- Histograms for numeric columns
- Bar charts for categories
- Correlation heatmap
- Missing data overview

### Code Tab
```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv')

# Statistical analysis
print(df.describe())

# Correlation matrix
corr = df.corr(numeric_only=True)
```

### Ask Questions
```
Q: "What are the top-performing products?"
A: "Based on the data, Laptops have the highest 
   average sales at $75,432 per transaction, 
   followed by Monitors at $68,291..."
```

---

## File Sizes
- `app.py`: ~12 KB (main Streamlit app)
- `analyzer.py`: ~4 KB (Claude integration)
- `data_processor.py`: ~6 KB (data analysis)
- `visualization.py`: ~5 KB (charts)
- `sample_sales_data.csv`: ~50 KB (test data)

Total: ~80 KB (very lightweight!)

---

## Troubleshooting

**Error: "API key not valid"**
- Check API key format (should start with sk-ant-)
- Regenerate from console.anthropic.com

**Error: "No numeric columns found"**
- Ensure CSV has numeric data
- Check data types: use Overview tab to inspect

**Slow performance with large files**
- Consider sampling data first
- Upload a subset instead of full dataset

**Visualizations not showing**
- Check if columns are numeric/categorical
- Try selecting different column

---

## Next Steps

1. ✅ Test with sample_sales_data.csv
2. ✅ Upload your own dataset
3. ✅ Try all tabs and features
4. ✅ Ask different questions
5. ✅ Download generated code
6. ✅ Customize prompts in analyzer.py
7. ✅ Deploy to Streamlit Cloud
8. ✅ Share with team/colleagues

---

Happy analyzing! 📊
