import pandas as pd
from datetime import datetime
from typing import List, Dict, Union

def process_table(table: List[Dict[str, Union[str, int]]], timeframe: int = 5) -> List[Dict[str, Union[str, int]]]:
    # Sort the table by AccessPoint (ascending) and DateTime (ascending)
    table.sort(key=lambda x: (x['AccessPoint'], datetime.fromisoformat(x['DateTime']) if isinstance(x['DateTime'], str) else x['DateTime']))


    # Add the Custom column with "Unique" or "Duplicate" values
    processed_table = []
    for index, row in enumerate(table):
        if index == 0:
            processed_table.append({**row, 'Status': 'Unique'})
            continue

        prev_row = table[index - 1]
        time_difference = (datetime.fromisoformat(row['DateTime'] if isinstance(row['DateTime'], str) else row['DateTime'].isoformat()) - datetime.fromisoformat(prev_row['DateTime'] if isinstance(prev_row['DateTime'], str) else prev_row['DateTime'].isoformat())).seconds // 60
  # Convert to minutes

        is_duplicate = (
            row['AccessPoint'] == prev_row['AccessPoint'] and
            row['Name'] == prev_row['Name'] and
            row['Gate'] == prev_row['Gate'] and
            time_difference <= timeframe
        )

        processed_table.append({**row, 'Status': 'Duplicate' if is_duplicate else 'Unique'})

    return processed_table

def read_xlsx_data(file_path: str) -> List[Dict[str, Union[str, int]]]:
    df = pd.read_excel(file_path, engine='openpyxl')
    data = df.to_dict('records')
    return data

def write_csv_data(file_path: str, data: List[Dict[str, Union[str, int]]]) -> None:
    df = pd.DataFrame(data)
    df.to_csv(file_path, index=False)

if __name__ == "__main__":
    input_file = "AccessLog.xlsx"
    output_file = "output.csv"
    data = read_xlsx_data(input_file)
    processed_data = process_table(data)
    write_csv_data(output_file, processed_data)
    print("Results saved to", output_file)
