import csv
import re

def verify_tags():
    required_tags = ['<reason>', '<exception>', '<tension>', '<categorization>', '<deconstruction>', '<conclusion>']

    with open('tetralemma-reasoning-train.csv', 'r') as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    print(f"Scanning {len(rows)} entries for required tags...")

    error_count = 0
    for i, row in enumerate(rows):
        reasoning = row['Reasoning']
        missing = []
        for tag in required_tags:
            # Simple check for the opening tag
            if tag not in reasoning:
                missing.append(tag)

        if missing:
            print(f"Row {i+1} (Question: {row['Question'][:50]}...) missing tags: {missing}")
            error_count += 1

    if error_count == 0:
        print("SUCCESS: All entries contain the required Tetralemma XML tags.")
    else:
        print(f"FAILURE: {error_count} entries are malformed.")

if __name__ == "__main__":
    verify_tags()
