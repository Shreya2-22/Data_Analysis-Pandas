import pandas as pd

data = {
    "Name": ['Shreya', 'Sraddha', 'Safal'],
    "Age": [25, 30, 22],
    "City": ['New York', 'Los Angeles', 'Chicago']
}

df = pd.DataFrame(data)
print(df)

df.to_json('output.json', index=False)