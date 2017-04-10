import pandas

df = pandas.read_json("supermarkets.json")

print(df.set_index("ID"))

print(df)