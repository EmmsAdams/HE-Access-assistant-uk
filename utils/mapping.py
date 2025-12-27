def normalize(text):
    return (text or "").strip().lower()

def find_mapping(df, country, qualification):
    if df.empty:
        return None

    c = normalize(country)
    q = normalize(qualification)

    matches = df[
        df["country"].str.lower().str.contains(c, na=False) &
        df["qualification_name"].str.lower().str.contains(q, na=False)
    ]

    if matches.empty:
        return None

    row = matches.iloc[0]
    return {
        "likely_uk_level": row["likely_uk_level"],
        "note": row["uk_equiv_note"],
        "confidence": row["confidence"]
    }
