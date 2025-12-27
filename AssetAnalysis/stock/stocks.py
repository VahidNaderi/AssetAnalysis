# stock/stock.py
import pandas as pd
import numpy as np

def generate_missing_stock(
    usd_df: pd.DataFrame,
    start_date: str,
    ratio: float,
    gap_factor: float = 0.1,
    gap_prob: float = 0.3,
    seed: int = 42
) -> pd.DataFrame:

    np.random.seed(seed)

    missing_df = usd_df[usd_df["Date"] < start_date].copy()

    if missing_df.empty:
        return pd.DataFrame(columns=["Date", "Price"])

    gaps = np.random.rand(len(missing_df)) < gap_prob
    gap_effect = np.where(gaps, gap_factor, 0)

    missing_df["Price"] = (
        missing_df["Price"] * ratio * (1 + gap_effect)
    ).round()

    return missing_df[["Date", "Price"]].reset_index(drop=True)
