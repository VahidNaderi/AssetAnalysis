# gold/gold.py
import pandas as pd

def generate_missing_gold(
    usd_df: pd.DataFrame,
    start_date: str,
    ratio: float
) -> pd.DataFrame:

    missing_df = usd_df[usd_df["Date"] < start_date].copy()

    if missing_df.empty:
        return pd.DataFrame(columns=["Date", "Price"])

    smoothed_usd = missing_df["Price"].rolling(
        window=3,
        center=True,
        min_periods=1
    ).mean()

    missing_df["Price"] = (smoothed_usd * ratio).round()

    return missing_df[["Date", "Price"]].reset_index(drop=True)
