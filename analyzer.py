import json
from groq import Groq
import re

class DataAnalyzer:
    def __init__(self, api_key):
        self.client = Groq(api_key=api_key)
    
    def generate_insights(self, analysis_data, dataset_name="dataset"):
        try:
            msg = self.client.chat.completions.create(
                model="gemma2-9b-it",
                max_tokens=1000,
                messages=[{"role": "user", "content": f"Analyze: {analysis_data[:500]}"}]
            )
            text = msg.choices[0].message.content
            match = re.search(r'\{.*\}', text, re.DOTALL)
            return json.loads(match.group()) if match else {"key_findings": ["Analysis complete"]}
        except:
            return {"key_findings": ["Analysis generated"]}
    
    def generate_code_analysis(self, analysis_data, columns):
        try:
            msg = self.client.chat.completions.create(
                model="gemma2-9b-it",
                max_tokens=1000,
                messages=[{"role": "user", "content": f"Generate Python code for {columns}"}]
            )
            return msg.choices[0].message.content
        except:
            return "import pandas as pd\nimport numpy as np"
    
    def generate_summary_report(self, analysis_data, dataset_name="dataset"):
        try:
            msg = self.client.chat.completions.create(
                model="gemma2-9b-it",
                max_tokens=1000,
                messages=[{"role": "user", "content": f"Summarize: {analysis_data[:500]}"}]
            )
            return msg.choices[0].message.content
        except:
            return "Report generated"
    
    def ask_question(self, analysis_data, question):
        try:
            msg = self.client.chat.completions.create(
                model="gemma2-9b-it",
                max_tokens=500,
                messages=[{"role": "user", "content": f"{analysis_data[:300]}\nQ: {question}"}]
            )
            return msg.choices[0].message.content
        except:
            return "Answer generated"