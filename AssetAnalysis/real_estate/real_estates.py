import pandas as pd

def generate_housing_index(
    usd_df: pd.DataFrame,
    window: int = 12
) -> pd.DataFrame:

    df = usd_df.copy()

    smoothed = df["Price"].rolling(
        window=window,
        min_periods=1
    ).mean()

    index_0_100 = 100 * (smoothed - smoothed.min()) / (smoothed.max() - smoothed.min())

    df["Price"] = index_0_100.round(2)

    return df[["Date", "Price"]]
