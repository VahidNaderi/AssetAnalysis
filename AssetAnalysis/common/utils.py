import pandas as pd 



def daily_to_monthly(df: pd.DataFrame) -> pd.DataFrame:
    if "Date" not in df.columns or "Price" not in df.columns:
        raise ValueError("DataFrame must contain 'Date' and 'Price' columns.")
    
    # Validate date format: mu|st be exactly 10 characters (YYYY/MM/DD)
    date_lengths = df["Date"].astype(str).str.len()
    if not (date_lengths == 10).all():
        invalid_dates = df["Date"][date_lengths != 10].unique()
        raise ValueError(
            f"Invalid date format. Expected 'YYYY/MM/DD' (10 characters).\n"
            f"Invalid examples: {invalid_dates[:5]}"
        )
    
    df_monthly = df.copy()
    df_monthly["Date"] = df_monthly["Date"].str[:7]
    
    result = (
        df_monthly.groupby("Date")["Price"]
        .mean()
        .round()
        .reset_index()
    )
    
    return result


def calculate_change(df: pd.DataFrame) -> pd.DataFrame:

    if "Price" not in df.columns:
        raise ValueError("DataFrame must contain 'Price' column.")
    
    df = df.copy()
    df["change"] = df["Price"].pct_change().fillna(0.0).round(4)
    
    return df



