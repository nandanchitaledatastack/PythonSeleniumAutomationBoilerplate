import pandas as pd
import logging

log = logging.getLogger(__name__)

class InputReader:
    def __init__(self, file_path, sheet_name) -> None:
        self.input_file = file_path
        self.sheet_name = sheet_name

    def getInputData(self) -> dict:
        '''
            Method to read data from excel sheet
        '''

        returnValue = None
        try:
            excel_data = pd.read_excel(self.input_file, sheet_name = self.sheet_name)
            returnValue = excel_data
        except Exception as e:
            error_message = f"InputReader > getInputData : {e}"
            log.error(error_message)
        return returnValue

        