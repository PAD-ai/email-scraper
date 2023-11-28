import gspread
from oauth2client.service_account import ServiceAccountCredentials

input_file = "../results/Results_2023-11-28_09-20-57.txt"

scope = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/drive",
]
creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
client = gspread.authorize(creds)

sheet_title = "mails-ajuntaments"
sheet = client.open(sheet_title).sheet1

data_to_save = [
    ["municipi", "email"],
]

with open(input_file, "r") as f:
    lines = f.readlines()

for line in lines:
    data_to_save.append(line.replace("\n", "").strip().split("->"))


sheet.clear()

sheet.update("A1", data_to_save)

print(f"Data has been successfully saved in {sheet_title}.")
