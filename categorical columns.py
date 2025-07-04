
ct_cols = ['gender', 'city', 'education']

# ct_cols = categorical columns yani kategorik sütunlar.

Burada ct = "categorical"
cols = "columns" (sütunlar)
👉 Kısaca: ct_cols, veri çerçevesindeki kategorik sütunların listesidir.

def encode_categoricals(df, ct_cols):
    return pd.get_dummies(df, columns=ct_cols)

# Bu fonksiyon, ct_cols olarak verilen sütunları one-hot encode eder.
