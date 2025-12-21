import pandas as pd
import random

char_set = ["0","0","0","0", "a", "b", "c", "d", "e", "f", "g"]
data = []
data_subsets = 10
for i in range(10):
    row = {"Participant_ID": i}
    row["Submission_ID"]= f"Submission_{i}_Sub_i"
    for j in range(data_subsets):
        row[f"{j}"] = random.choice(char_set)
    data.append(row)
df = pd.DataFrame(data)
df.to_csv("ranking.csv",index=False)
print(df)