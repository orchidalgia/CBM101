
df.columns = [c.strip() for c in df.columns]
df.columns = [c.replace(' ', '_') for c in df.columns]
