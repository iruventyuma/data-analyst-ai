import streamlit as st
import pandas as pd
import os
from dotenv import load_dotenv
from data_processor import DataProcessor
from analyzer import DataAnalyzer
from visualization import Visualizer

load_dotenv()
st.set_page_config(page_title="GenAI Data Analyzer", page_icon="📊", layout="wide")

if 'df' not in st.session_state: st.session_state.df = None
if 'api_key' not in st.session_state: st.session_state.api_key = os.getenv('GROQ_API_KEY', '')

st.sidebar.title("⚙️ Configuration")
st.sidebar.success("✅ API Key Loaded")
st.sidebar.title("📁 Data Upload")

uploaded = st.sidebar.file_uploader("Upload CSV", type=['csv'])
if uploaded:
    st.session_state.df = pd.read_csv(uploaded)
    st.session_state.file_name = uploaded.name.replace('.csv', '')
    st.sidebar.success(f"✅ Loaded {st.session_state.df.shape[0]} rows")

st.title("📊 GenAI Data Analysis Assistant")
st.markdown("*Powered by Groq AI*")

if st.session_state.df is None:
    st.info("👈 Upload a CSV file to begin")
    st.stop()

df = st.session_state.df
file_name = st.session_state.get('file_name', 'dataset')

tab1, tab2, tab3, tab4, tab5 = st.tabs(["📈 Overview", "🔍 Insights", "📊 Visualizations", "💻 Code", "❓ Ask Questions"])

with tab1:
    st.header("Dataset Overview")
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Rows", df.shape[0])
    c2.metric("Columns", df.shape[1])
    c3.metric("Missing", df.isnull().sum().sum())
    c4.metric("Duplicates", df.duplicated().sum())
    st.divider()
    st.subheader("Data Preview")
    st.dataframe(df.head(10), use_container_width=True)
    st.divider()
    st.subheader("Statistics")
    numeric_df = df.select_dtypes(include=['number'])
    if not numeric_df.empty:
        st.dataframe(numeric_df.describe().T, use_container_width=True)

with tab2:
    st.header("AI-Generated Insights")
    if st.button("🚀 Generate Insights"):
        with st.spinner("Analyzing..."):
            try:
                processor = DataProcessor(df)
                analysis = processor.get_analysis_for_prompt()
                analyzer = DataAnalyzer(st.session_state.api_key)
                insights = analyzer.generate_insights(analysis, file_name)
                st.session_state.insights = insights
                st.success("✅ Analysis Complete!")
                
                if 'key_findings' in insights:
                    st.subheader("🎯 Key Findings")
                    findings = insights['key_findings']
                    if isinstance(findings, list):
                        for f in findings:
                            st.write(f"• {f}")
                    else:
                        st.write(findings)
                
                if 'data_quality' in insights:
                    st.subheader("✅ Data Quality")
                    quality = insights['data_quality']
                    if isinstance(quality, list):
                        for q in quality:
                            st.write(f"• {q}")
            except Exception as e:
                st.error(f"Error: {str(e)[:150]}")

with tab3:
    st.header("Interactive Visualizations")
    viz = Visualizer(df)
    
    if viz.numeric_cols:
        st.subheader("📈 Numeric Column Distributions")
        col = st.selectbox("Select column", viz.numeric_cols, key="dist")
        fig_hist = viz.create_distribution_plot(col)
        if fig_hist:
            st.plotly_chart(fig_hist, use_container_width=True)
        
        fig_box = viz.create_boxplot(col)
        if fig_box:
            st.plotly_chart(fig_box, use_container_width=True)
    
    if viz.categorical_cols:
        st.subheader("📊 Categorical Columns")
        cat_col = st.selectbox("Select category", viz.categorical_cols, key="cat")
        fig_cat = viz.create_category_counts(cat_col)
        if fig_cat:
            st.plotly_chart(fig_cat, use_container_width=True)
    
    if len(viz.numeric_cols) >= 2:
        st.subheader("🔗 Correlation Matrix")
        fig_corr = viz.create_correlation_heatmap()
        if fig_corr:
            st.plotly_chart(fig_corr, use_container_width=True)
    
    fig_missing = viz.create_missing_data_plot()
    if fig_missing:
        st.subheader("Missing Data")
        st.plotly_chart(fig_missing, use_container_width=True)

with tab4:
    st.header("Download Analysis Code")
    if st.button("📝 Generate & Download Code"):
        with st.spinner("Generating code..."):
            try:
                processor = DataProcessor(df)
                analysis = processor.get_analysis_for_prompt()
                analyzer = DataAnalyzer(st.session_state.api_key)
                code = analyzer.generate_code_analysis(analysis, df.columns.tolist())
                
                st.download_button(
                    label="⬇️ Download Python Code",
                    data=code,
                    file_name=f"{file_name}_analysis.py",
                    mime="text/plain"
                )
                st.success("✅ Code ready to download!")
            except Exception as e:
                st.error(f"Error: {str(e)[:150]}")

with tab5:
    st.header("Ask Questions About Your Data")
    question = st.text_area("Ask a question:", placeholder="What are the key patterns?", height=100)
    
    if st.button("🔍 Ask Groq"):
        if question.strip():
            with st.spinner("Thinking..."):
                try:
                    processor = DataProcessor(df)
                    analysis = processor.get_analysis_for_prompt()
                    analyzer = DataAnalyzer(st.session_state.api_key)
                    answer = analyzer.ask_question(analysis, question)
                    
                    st.subheader("Answer:")
                    st.write(answer)
                except Exception as e:
                    st.error(f"Error: {str(e)[:150]}")
        else:
            st.warning("Please enter a question")

st.divider()
st.markdown("""
<div style='text-align: center; color: #666; font-size: 0.9rem;'>
    <p>GenAI Data Analysis Assistant | Built with Streamlit + Groq AI</p>
    <p><a href='https://github.com/iruventyuma/data-analyst-ai'>GitHub</a> | <a href='https://console.groq.com'>Groq Console</a></p>
</div>
""", unsafe_allow_html=True)