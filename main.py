import openpyxl

def print_first_row(filename):
    # Load the workbook
    workbook = openpyxl.load_workbook(filename)

    # Select the first sheet
    sheet = workbook.active

    # Get the values from the first row
    first_row = sheet[1]

    # Print the values separated by commas
    print(','.join([cell.value for cell in first_row]))

# Usage example
filename = 'test-data/test-file.xlsx'
print_first_row(filename)