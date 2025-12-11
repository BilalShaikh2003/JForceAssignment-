import pandas as pd


data = {
    "Roll No": [1,1,2,2,1,2],
    "Subject": ["DS","Java","DS","Java","DS","Java"],
    "Marks": [25,40,30,26,40,50],
    "Date": ["01-01-23","02-01-23","01-01-23","02-01-23","15-01-23","15-01-23"]
}

df = pd.DataFrame(data)


df["Date"] = pd.to_datetime(df["Date"], format="%d-%m-%y")

print('Input Data \n' ,df)
print("\n")

df = df.sort_values(["Roll No", "Subject", "Date"], ascending=[True, True, False])

df["AttemptNo"] = df.groupby(["Roll No", "Subject"]).cumcount() + 1

df = df[df["AttemptNo"] <= 3]

result = df.pivot_table(
    index=["Roll No", "Subject"],
    columns="AttemptNo",
    values="Marks",
    aggfunc="first"
)

result = result.rename(columns={1: "M1", 2: "M2", 3: "M3"})

result = result.fillna(0).reset_index()

latest_date = df[df["AttemptNo"] == 1][["Roll No", "Subject", "Date"]]

final_output = result.merge(latest_date, on=["Roll No", "Subject"], how="left")

final_output = final_output.sort_values(["Roll No", "Subject"]).reset_index(drop=True)

print('Out put data \n',final_output)
