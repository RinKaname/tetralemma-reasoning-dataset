import csv
import re

def repair_csv():
    input_file = 'tetralemma-reasoning-train.csv'
    output_file = 'tetralemma-reasoning-train_fixed.csv'

    tags = {
        '<reason>': '</reason>',
        '<exception>': '</exception>',
        '<tension>': '</tension>',
        '<categorization>': '</categorization>',
        '<deconstruction>': '</deconstruction>',
        '<conclusion>': '</conclusion>'
    }

    # Order matters for parsing logic
    tag_order = ['reason', 'exception', 'tension', 'categorization', 'deconstruction', 'conclusion']

    with open(input_file, 'r') as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames
        rows = list(reader)

    fixed_count = 0

    for i, row in enumerate(rows):
        content = row['Reasoning']
        original_content = content

        # Simple heuristic repair: if opening tag exists but closing doesn't,
        # try to find the start of the NEXT tag and insert closing tag before it,
        # or append to end if it's the last tag.

        for idx, tag_name in enumerate(tag_order):
            open_tag = f"<{tag_name}>"
            close_tag = f"</{tag_name}>"

            if open_tag in content and close_tag not in content:
                # Missing closing tag
                # Look for the next expected tag to know where to cut
                next_start = -1
                for next_tag_name in tag_order[idx+1:]:
                    next_open = f"<{next_tag_name}>"
                    if next_open in content:
                        next_start = content.find(next_open)
                        break

                if next_start != -1:
                    # Insert closing tag before the next opening tag
                    content = content[:next_start].rstrip() + "\n" + close_tag + "\n" + content[next_start:]
                else:
                    # No next tag found, so this must be the last section (or others are missing too)
                    # For conclusion, it's definitely at the end
                    content = content.rstrip() + "\n" + close_tag

        if content != original_content:
            row['Reasoning'] = content
            fixed_count += 1
            print(f"Fixed Row {i+1}")

    with open(input_file, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    print(f"Total rows fixed: {fixed_count}")

if __name__ == "__main__":
    repair_csv()
