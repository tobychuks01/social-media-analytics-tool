# src/engagement.py

def weighted_engagement(df):
    return df["likes"] + df["shares"]*2 + df["saves"]*3 + df["comments"]*2

def engagement_score(df):
    return (weighted_engagement(df) / df["views"]) * 100

def classify(score):
    if score > 10:
        return "SCALE"
    elif score < 3:
        return "KILL"
    return "ITERATE"