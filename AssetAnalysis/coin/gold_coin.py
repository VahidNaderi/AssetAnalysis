# coin/coin.py
import pandas as pd
import numpy as np

def generate_missing_imami(
    usd_df: pd.DataFrame,
    start_date: str,
    ratio: float,
    noise_std: float = 0.02,
    seed: int = 42
) -> pd.DataFrame:

    np.random.seed(seed)

    missing_df = usd_df[usd_df["Date"] < start_date].copy()

    if missing_df.empty:
        return pd.DataFrame(columns=["Date", "Price"])

    noise = np.random.normal(
        loc=0,
        scale=noise_std,
        size=len(missing_df)
    )

    missing_df["Price"] = (
        missing_df["Price"] * ratio * (1 + noise)
    ).round()

    return missing_df[["Date", "Price"]].reset_index(drop=True)
