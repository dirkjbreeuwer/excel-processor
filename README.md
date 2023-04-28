# Access Log Processor

This is a simple Python script to process access logs stored in an Excel file, identify and mark unique and duplicate entries, and save the result in a CSV file.
## Features 
- Reads data from an Excel file (`.xlsx` format)
- Processes the data to find and mark unique and duplicate entries based on certain criteria
- Exports the processed data to a CSV file
## Requirements
- Python 3.6 or newer
- pandas
- openpyxl

To install the required libraries, run:

```sh

pip install pandas openpyxl
```


## How to use 
1. Update the `input_file` variable with the path to the Excel file containing the access logs you want to process. 
2. Update the `output_file` variable with the path to the CSV file where you want to save the processed results.
3. Run the script:

```sh

python access_log_processor.py
```


1. The script will print "Results saved to {output_file}" once it has completed processing and saving the results.
## Functions 
- `process_table(table: List[Dict[str, Union[str, int]]], timeframe: int = 5) -> List[Dict[str, Union[str, int]]]`: Processes the access log table, identifying and marking unique and duplicate entries. 
- `read_xlsx_data(file_path: str) -> List[Dict[str, Union[str, int]]]`: Reads data from an Excel file and returns it as a list of dictionaries. 
- `write_csv_data(file_path: str, data: List[Dict[str, Union[str, int]]]) -> None`: Writes data to a CSV file.
## License

This project is licensed under the MIT License.