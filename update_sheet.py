import gspread
from oauth2client.service_account import ServiceAccountCredentials

def update_sheet(permalink, spreadsheet_id, api_key_file, sheet_title, sheet_url_column_letter):
    # Authenticate with the Google Sheets API
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name(api_key_file, scope)
    client = gspread.authorize(creds)

    # Open the sheet by its ID and specify the worksheet by its title
    sheet = client.open_by_key(spreadsheet_id).worksheet(sheet_title)

    # Convert the column letter to a column index (e.g., 'B' to 2)
    column_index = gspread.utils.a1_to_rowcol(sheet_url_column_letter + '1')[1]

    # Find the first empty row in the specified column
    first_empty_row = len(sheet.col_values(column_index)) + 1

    # Update the sheet with the permalink
    sheet.update_cell(first_empty_row, column_index, permalink)
