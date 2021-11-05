"""
BEFORE RUNNING:
---------------
1. If not already done, enable the Google Sheets API
   and check the quota for your project at
   https://console.developers.google.com/apis/api/sheets
2. Install the Python client library for Google APIs by running
   `pip install --upgrade google-api-python-client`
"""
from pprint import pprint

from googleapiclient import discovery

import os

from dotenv import load_dotenv

load_dotenv()
WEB_DRIVER_PATH = os.getenv('WEB_DRIVER_PATH')
LOAN_URL = os.getenv('LOAN_URL')
SPREAD_SHEET_ID = os.getenv('SPREAD_SHEET_ID')


# https://developers.google.com/sheets/quickstart/python#step_3_set_up_the_sample
#
# Authorize using one of the following scopes:
#     'https://www.googleapis.com/auth/drive'
#     'https://www.googleapis.com/auth/drive.file'
#     'https://www.googleapis.com/auth/spreadsheets'

credentials = 'https://www.googleapis.com/auth/spreadsheets'



service = discovery.build('sheets', 'v4', credentials=credentials)

# The spreadsheet to request.
spreadsheet_id = SPREAD_SHEET_ID  

get_spreadsheet_by_data_filter_request_body = {
    # The DataFilters used to select which ranges to retrieve from
    # the spreadsheet.
    'data_filters': [

        {
            
        }
    
    ],  # TODO: Update placeholder value.

    # True if grid data should be returned.
    # This parameter is ignored if a field mask was set in the request.
    'include_grid_data': True,  # TODO: Update placeholder value.

    # TODO: Add desired entries to the request body.
}

request = service.spreadsheets().getByDataFilter(spreadsheetId=spreadsheet_id, body=get_spreadsheet_by_data_filter_request_body)
response = request.execute()

# TODO: Change code below to process the `response` dict:
pprint(response)