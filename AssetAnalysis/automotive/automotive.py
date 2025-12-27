import pandas as pd
import numpy as np

def generate_car_index(
    usd_df: pd.DataFrame,
    window: int = 3,
    noise_std: float = 0.03,
    seed: int = 42
) -> pd.DataFrame:

    np.random.seed(seed)

    df = usd_df.copy()

    smoothed = df["Price"].rolling(
        window=window,
        min_periods=1
    ).mean()

    noise = np.random.normal(0, noise_std, len(df))

    raw_index = smoothed * (1 + noise)

    # نرمال‌سازی 0–100
    index_0_100 = 100 * (raw_index - raw_index.min()) / (raw_index.max() - raw_index.min())

    df["Price"] = index_0_100.round(2)

    return df[["Date", "Price"]]
