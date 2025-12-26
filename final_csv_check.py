import csv
import sys

def check_csv_consistency():
    filename = 'tetralemma-reasoning-train.csv'
    try:
        with open(filename, 'r', newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            try:
                header = next(reader)
            except StopIteration:
                print("Error: File is empty.")
                sys.exit(1)

            if len(header) != 2:
                print(f"Error: Header has {len(header)} columns, expected 2.")
                sys.exit(1)

            if header != ['Question', 'Reasoning']:
                print(f"Warning: Header is {header}, expected ['Question', 'Reasoning'].")

            row_count = 0
            error_count = 0

            for i, row in enumerate(reader):
                row_num = i + 2 # 1-based index, +1 for header
                if not row:
                    print(f"Warning: Row {row_num} is empty.")
                    continue

                if len(row) != 2:
                    print(f"Error: Row {row_num} has {len(row)} columns. Expected 2.")
                    print(f"Content snippet: {row}")
                    error_count += 1

                row_count += 1

            print(f"Checked {row_count} data rows.")
            if error_count == 0:
                print("SUCCESS: CSV structure is consistent (2 columns per row).")
            else:
                print(f"FAILURE: Found {error_count} structural errors.")
                sys.exit(1)

    except csv.Error as e:
        print(f"CSV Parsing Error: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"General Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    check_csv_consistency()
