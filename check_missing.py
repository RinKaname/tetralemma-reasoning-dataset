import csv
import glob

def find_missing():
    # 1. Read current questions
    current_questions = set()
    try:
        with open('tetralemma-reasoning-train.csv', 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                current_questions.add(row['Question'].strip())
    except Exception as e:
        print(f"Error reading CSV: {e}")
        return

    print(f"Current unique questions in CSV: {len(current_questions)}")

    # 2. Read batch files
    # I will manually reconstruct the lists since I can't import the scripts easily
    # (they are standalone scripts that run on execution).
    # Instead, I will read the .py files and extract the questions using regex/eval.

    # Actually, simpler way: I will just re-read the scripts as text
    # and extract the "Question": "..." strings.

    import re

    missing_entries = []

    batch_files = [
        'append_batch_1.py',
        'append_batch_1_part2.py',
        'append_batch_2_part1.py',
        'append_batch_2_part2.py',
        'append_batch_3_part1.py',
        'append_batch_3_part2.py',
        'append_batch_4_part1.py',
        'append_batch_4_part2.py'
    ]

    total_batch_questions = 0

    for fname in batch_files:
        try:
            with open(fname, 'r') as f:
                content = f.read()
                # Find the list block
                matches = re.findall(r'"Question":\s*"(.*?)"', content, re.DOTALL)

                print(f"{fname}: Found {len(matches)} questions.")
                total_batch_questions += len(matches)

                for q in matches:
                    q_clean = q.replace('\\"', '"') # unescape quotes
                    if q_clean not in current_questions:
                        print(f"MISSING: {q_clean[:50]}...")
                        # We need to extract the full entry for this question.
                        # This is getting complicated to parse via regex.
                        # Better to just re-run the append logic for missing ones.
        except FileNotFoundError:
            print(f"File not found: {fname}")

    print(f"Total questions in batches: {total_batch_questions}")

if __name__ == "__main__":
    find_missing()
