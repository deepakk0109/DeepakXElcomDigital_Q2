# Task 1: Imported the packages
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Task 2: Get the information from the user by taking inputs
def get_user_info():
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    age = input("Enter your age: ")
    return name, email, age

# Task 3: Create a function that pushes the information into the Google sheet
def update_google_sheet(name, email, age):
    scope = ['https://spreadsheets.google.com/feeds',
             'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name('service_account_credentials.json', scope)
    client = gspread.service_account(filename='E:\Interns\Elcom Digital\service_account_credentials.json')
    client = gspread.authorize(creds)

    sheet = client.open('Elcom-digital').sheet1

    sheet.append_row([name, email, age])
    print("Data has been successfully added to the Google Sheet.")

if __name__ == "__main__":
    name, email, age = get_user_info()
    update_google_sheet(name, email, age)
