"""Module for listing down additional custom functions required for the notebooks."""

import pandas as pd

def binned_sales_dollars_value(final_df):
    """Bin the selling price column using quantiles."""
    return pd.qcut(final_df["sales_units_value"], q=10)

# from sklearn.base import BaseEstimator, TransformerMixin

