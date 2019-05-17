# Go Google api -> google drive api enable -> create credentials
# go to google sheets share csv wtih client email from last step
# Install pip install gspread oauth2client
import pip
pip.main(["install","gspread"])
import gspread 
from oauth2client.service_account import ServiceAccountCredentials
import pprint
import json
import jsonobject


scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']

creds= ServiceAccountCredentials.from_json_keyfile_name('googleSheets_secret.json', scope)
client = gspread.authorize(creds)

pp = pprint.PrettyPrinter()
#Be sure to create a CSV frist
sheet = client.open('Database Project').sheet1

response = sheet.get_all_records()
result = response.__getitem__(0)
pp.pprint(json.dumps(result).__getattribute__("value"))