import csv

def fix_dark_matter():
    filename = 'tetralemma-reasoning-train.csv'
    target_question = "Can 'Dark Matter' be explained by modifying gravity (MOND)?"

    rows = []
    found = False

    with open(filename, 'r', newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames

        for row in reader:
            if row['Question'] == target_question:
                content = row['Reasoning']
                # Check for double conclusion
                if content.count('<conclusion>') > 1:
                    print("Found malformed entry with double conclusion.")
                    # Split by closing tag of the first conclusion
                    parts = content.split('</conclusion>')
                    # The first part + closing tag is the correct one.
                    # The trailing part is the garbage.
                    # Dark Matter conclusion ends with "...stuff we can't see."

                    # Let's be safer. Find the specific garbage string.
                    garbage = "\n<conclusion>\nInformation is physical. It is not a ghost in the machine; it is the machine's state. Therefore, it contributes to the energy-mass budget of the universe, however slightly.\n</conclusion>"

                    if garbage in content:
                        new_content = content.replace(garbage, "")
                        row['Reasoning'] = new_content.strip()
                        print("Fixed entry.")
                        found = True
                    else:
                        print("Could not match exact garbage string. Attempting generic fix.")
                        # Generic fix: keep text until the first </conclusion>
                        first_conclusion_end = content.find('</conclusion>') + len('</conclusion>')
                        row['Reasoning'] = content[:first_conclusion_end]
                        print("Generic fix applied.")
                        found = True
            rows.append(row)

    if found:
        with open(filename, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(rows)
        print("CSV saved.")
    else:
        print("Target entry not found or no fix needed.")

if __name__ == "__main__":
    fix_dark_matter()
