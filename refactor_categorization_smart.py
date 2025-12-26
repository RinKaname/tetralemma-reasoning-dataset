import csv
import re

def clean_snippet(text):
    # Remove newlines and extra spaces
    text = text.replace('\n', ' ').strip()
    # Remove XML tags if any remaining
    text = re.sub(r'<[^>]+>', '', text)
    # Get first sentence or first 100 chars
    if '.' in text:
        text = text.split('.')[0]
    if len(text) > 100:
        text = text[:100] + "..."
    # Lowercase start unless it's a proper noun (heuristic)
    if text and text[0].isupper() and not text[0:2].isupper():
        # Simple heuristic: lowercase unless the second letter is also upper (acronym)
        # or it looks like a proper noun. For safety, keep it as is or lowercase?
        # Let's keep as is to avoid breaking names like "Facebook".
        pass
    return text.strip()

def refactor_categorization():
    input_file = 'tetralemma-reasoning-train.csv'
    output_file = 'tetralemma-reasoning-train_smart.csv'

    with open(input_file, 'r', newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames
        rows = list(reader)

    fixed_count = 0

    # Tension extraction (Term A and Term B)
    # Matches: "We categorize this as a 'X' dispute. The Reason prioritizes 'A'..., while the Exception argues for 'B'..."
    # OR Matches original: "This is a tension between 'A' and 'B'..."

    for i in range(410, len(rows)):
        row = rows[i]
        content = row['Reasoning']

        # 1. Extract Terms from Tension (preferred source)
        tension_match = re.search(r"<tension>(.*?)</tension>", content, re.DOTALL)
        term_a = "the thesis"
        term_b = "the antithesis"

        if tension_match:
            tension_text = tension_match.group(1)
            terms = re.findall(r"'(.*?)'", tension_text)
            if len(terms) >= 2:
                term_a = terms[0]
                term_b = terms[1]

        # 2. Extract Snippets from Reason and Exception
        reason_match = re.search(r"<reason>(.*?)</reason>", content, re.DOTALL)
        exception_match = re.search(r"<exception>(.*?)</exception>", content, re.DOTALL)

        reason_snippet = "standard logic"
        exception_snippet = "counter-intuitive logic"

        if reason_match:
            reason_snippet = clean_snippet(reason_match.group(1))

        if exception_match:
            exception_snippet = clean_snippet(exception_match.group(1))
            # Remove leading "However, " or "But "
            exception_snippet = re.sub(r"^(However|But|Conversely|Yet),?\s*", "", exception_snippet, flags=re.IGNORECASE)

        # 3. Construct New Categorization
        new_cat = (
            f"<categorization>\n"
            f"We must segregate **{term_a}** from **{term_b}**. "
            f"The former prioritizes *{reason_snippet}*, "
            f"while the latter prioritizes *{exception_snippet}*.\n"
            f"</categorization>"
        )

        # 4. Replace the old categorization block
        # The old block might be multi-line, so use DOTALL regex replacement
        row['Reasoning'] = re.sub(r"<categorization>.*?</categorization>", new_cat, content, flags=re.DOTALL)
        fixed_count += 1

    with open(output_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    print(f"Refactored categorization for {fixed_count} rows.")

if __name__ == "__main__":
    refactor_categorization()
