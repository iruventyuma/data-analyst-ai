import pandas as pd
import numpy as np
from typing import Dict, List, Tuple
import json

class DataProcessor:
    """Handles data exploration, cleaning, and statistical analysis"""
    
    def __init__(self, df: pd.DataFrame):
        self.df = df
        self.numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
        self.categorical_cols = df.select_dtypes(include=['object', 'category']).columns.tolist()
        self.datetime_cols = df.select_dtypes(include=['datetime64']).columns.tolist()
    
    def get_basic_info(self) -> Dict:
        """Get basic dataset information"""
        return {
            "shape": self.df.shape,
            "columns": self.df.columns.tolist(),
            "dtypes": self.df.dtypes.to_dict(),
            "missing_values": self.df.isnull().sum().to_dict(),
            "duplicates": self.df.duplicated().sum(),
            "memory_usage_mb": round(self.df.memory_usage(deep=True).sum() / 1024**2, 2)
        }
    
    def get_statistical_summary(self) -> Dict:
        """Get statistical summary for numeric columns"""
        summary = {}
        for col in self.numeric_cols:
            summary[col] = {
                "mean": round(self.df[col].mean(), 2),
                "median": round(self.df[col].median(), 2),
                "std": round(self.df[col].std(), 2),
                "min": round(self.df[col].min(), 2),
                "max": round(self.df[col].max(), 2),
                "q1": round(self.df[col].quantile(0.25), 2),
                "q3": round(self.df[col].quantile(0.75), 2),
            }
        return summary
    
    def get_categorical_summary(self) -> Dict:
        """Get summary for categorical columns"""
        summary = {}
        for col in self.categorical_cols:
            value_counts = self.df[col].value_counts().head(10).to_dict()
            summary[col] = {
                "unique_values": self.df[col].nunique(),
                "top_values": value_counts,
                "missing": int(self.df[col].isnull().sum())
            }
        return summary
    
    def detect_anomalies(self) -> Dict:
        """Detect outliers using IQR method"""
        anomalies = {}
        for col in self.numeric_cols:
            Q1 = self.df[col].quantile(0.25)
            Q3 = self.df[col].quantile(0.75)
            IQR = Q3 - Q1
            lower_bound = Q1 - 1.5 * IQR
            upper_bound = Q3 + 1.5 * IQR
            
            outlier_count = len(self.df[(self.df[col] < lower_bound) | (self.df[col] > upper_bound)])
            if outlier_count > 0:
                anomalies[col] = {
                    "outlier_count": outlier_count,
                    "percentage": round(outlier_count / len(self.df) * 100, 2),
                    "lower_bound": round(lower_bound, 2),
                    "upper_bound": round(upper_bound, 2)
                }
        return anomalies
    
    def detect_correlations(self, threshold=0.5) -> Dict:
        """Detect strong correlations between numeric columns"""
        if len(self.numeric_cols) < 2:
            return {}
        
        corr_matrix = self.df[self.numeric_cols].corr()
        correlations = {}
        
        for i in range(len(corr_matrix.columns)):
            for j in range(i+1, len(corr_matrix.columns)):
                corr_value = corr_matrix.iloc[i, j]
                if abs(corr_value) > threshold:
                    col1 = corr_matrix.columns[i]
                    col2 = corr_matrix.columns[j]
                    correlations[f"{col1} ↔ {col2}"] = round(corr_value, 3)
        
        return dict(sorted(correlations.items(), key=lambda x: abs(x[1]), reverse=True))
    
    def get_missing_data_patterns(self) -> Dict:
        """Analyze missing data patterns"""
        missing = self.df.isnull().sum()
        missing_percent = (missing / len(self.df) * 100).round(2)
        
        return {
            col: {
                "missing_count": int(missing[col]),
                "percentage": float(missing_percent[col])
            }
            for col in missing[missing > 0].index
        }
    
    def get_distribution_insights(self) -> Dict:
        """Get insights about distributions"""
        insights = {}
        for col in self.numeric_cols:
            skewness = self.df[col].skew()
            kurtosis = self.df[col].kurtosis()
            
            if abs(skewness) > 1:
                distribution = "highly skewed"
            elif abs(skewness) > 0.5:
                distribution = "moderately skewed"
            else:
                distribution = "approximately normal"
            
            insights[col] = {
                "distribution": distribution,
                "skewness": round(skewness, 3),
                "kurtosis": round(kurtosis, 3)
            }
        
        return insights
    
    def get_all_analysis(self) -> Dict:
        """Get complete analysis in one call"""
        return {
            "basic_info": self.get_basic_info(),
            "statistical_summary": self.get_statistical_summary(),
            "categorical_summary": self.get_categorical_summary(),
            "anomalies": self.detect_anomalies(),
            "correlations": self.detect_correlations(),
            "missing_patterns": self.get_missing_data_patterns(),
            "distributions": self.get_distribution_insights()
        }
    
    def get_analysis_for_prompt(self) -> str:
        """Format analysis as string for Claude prompt"""
        analysis = self.get_all_analysis()
        return json.dumps(analysis, indent=2, default=str)
