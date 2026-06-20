import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from typing import List, Optional
import numpy as np

class Visualizer:
    """Generates interactive visualizations using Plotly"""
    
    def __init__(self, df: pd.DataFrame):
        self.df = df
        self.numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
        self.categorical_cols = df.select_dtypes(include=['object', 'category']).columns.tolist()
    
    def create_distribution_plot(self, column: str) -> go.Figure:
        """Create histogram for numeric column"""
        if column not in self.numeric_cols:
            return None
        
        fig = px.histogram(
            self.df,
            x=column,
            nbins=30,
            title=f"Distribution of {column}",
            labels={column: column},
            color_discrete_sequence=['#0068C9']
        )
        fig.update_layout(
            height=400,
            template='plotly_white',
            showlegend=False,
            xaxis_title=column,
            yaxis_title="Frequency"
        )
        return fig
    
    def create_boxplot(self, column: str) -> go.Figure:
        """Create boxplot for numeric column"""
        if column not in self.numeric_cols:
            return None
        
        fig = go.Figure()
        fig.add_trace(go.Box(
            y=self.df[column],
            name=column,
            marker_color='#0068C9',
            boxmean='sd'
        ))
        fig.update_layout(
            title=f"Boxplot: {column}",
            height=400,
            template='plotly_white',
            showlegend=False,
            yaxis_title=column
        )
        return fig
    
    def create_correlation_heatmap(self) -> go.Figure:
        """Create correlation heatmap"""
        if len(self.numeric_cols) < 2:
            return None
        
        corr_matrix = self.df[self.numeric_cols].corr()
        
        fig = go.Figure(data=go.Heatmap(
            z=corr_matrix.values,
            x=corr_matrix.columns,
            y=corr_matrix.columns,
            colorscale='RdBu',
            zmid=0,
            zmin=-1,
            zmax=1,
            text=np.round(corr_matrix.values, 2),
            texttemplate='%{text}',
            textfont={"size": 10},
            colorbar=dict(title="Correlation")
        ))
        
        fig.update_layout(
            title="Correlation Matrix",
            height=600,
            width=700,
            template='plotly_white'
        )
        return fig
    
    def create_category_counts(self, column: str) -> go.Figure:
        """Create bar chart for categorical column"""
        if column not in self.categorical_cols:
            return None
        
        value_counts = self.df[column].value_counts().head(15)
        
        fig = px.bar(
            x=value_counts.index,
            y=value_counts.values,
            title=f"Value Counts: {column}",
            labels={'x': column, 'y': 'Count'},
            color_discrete_sequence=['#0068C9']
        )
        fig.update_layout(
            height=400,
            template='plotly_white',
            showlegend=False,
            xaxis_title=column,
            yaxis_title="Count"
        )
        return fig
    
    def create_scatter_matrix(self, columns: Optional[List[str]] = None) -> go.Figure:
        """Create scatter plot matrix for numeric columns"""
        if len(self.numeric_cols) < 2:
            return None
        
        cols_to_plot = columns if columns else self.numeric_cols[:4]
        cols_to_plot = [c for c in cols_to_plot if c in self.numeric_cols]
        
        if len(cols_to_plot) < 2:
            return None
        
        fig = px.scatter_matrix(
            self.df,
            dimensions=cols_to_plot,
            title="Scatter Matrix",
            height=800,
            color_discrete_sequence=['#0068C9']
        )
        fig.update_traces(diagonal_visible=False, marker=dict(size=3, opacity=0.5))
        fig.update_layout(template='plotly_white')
        return fig
    
    def create_missing_data_plot(self) -> go.Figure:
        """Create bar chart showing missing data"""
        missing = (self.df.isnull().sum() / len(self.df) * 100).sort_values(ascending=False)
        missing = missing[missing > 0]
        
        if len(missing) == 0:
            return None
        
        fig = px.bar(
            x=missing.values,
            y=missing.index,
            orientation='h',
            title="Missing Data Percentage",
            labels={'x': 'Percentage (%)', 'y': 'Columns'},
            color_discrete_sequence=['#FF6B6B']
        )
        fig.update_layout(
            height=max(300, 30 * len(missing)),
            template='plotly_white',
            showlegend=False
        )
        return fig
    
    def create_summary_stats_table(self) -> pd.DataFrame:
        """Create summary statistics table"""
        if not self.numeric_cols:
            return None
        
        return self.df[self.numeric_cols].describe().round(2)
