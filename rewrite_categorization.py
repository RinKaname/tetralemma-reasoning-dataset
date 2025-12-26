import csv
import re

def rewrite_categorization():
    input_file = 'tetralemma-reasoning-train.csv'
    output_file = 'tetralemma-reasoning-train_fixed.csv'

    with open(input_file, 'r', newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames
        rows = list(reader)

    fixed_count = 0

    # Regex to capture Tension terms
    # Pattern: tension between 'Term A' (optional context) and 'Term B' (optional context)
    # We use non-greedy .*? to handle the capture
    tension_pattern = re.compile(r"<tension>\s*This is a tension between '(.*?)'(.*?) and '(.*?)'(.*?)\.\s*(.*?)</tension>", re.DOTALL | re.IGNORECASE)
    # Fallback pattern if "This is a tension between" logic varies
    tension_fallback = re.compile(r"<tension>\s*(.*?)\s*</tension>", re.DOTALL)

    # Regex to capture existing Category domain
    # Pattern: This is a 'Domain' problem... or This is a 'Domain' dilemma...
    cat_pattern = re.compile(r"<categorization>\s*This is an? '(.*?)' (problem|dilemma|scenario|situation)(.*?)\.?\s*</categorization>", re.DOTALL | re.IGNORECASE)

    for i in range(410, len(rows)):
        row = rows[i]
        content = row['Reasoning']

        # Extract Tension
        # Note: My generated text sometimes says "There is a tension between..." and sometimes "This is a tension between..."
        # I need to normalize the input string for matching

        # 1. Find Tension Block
        t_match = re.search(r"<tension>(.*?)</tension>", content, re.DOTALL)
        if not t_match:
            print(f"Row {i}: No tension tag found.")
            continue

        tension_text = t_match.group(1).strip()

        # 2. Extract Terms
        # Try to find 'A' and 'B' quoted
        terms = re.findall(r"'(.*?)'", tension_text)
        if len(terms) >= 2:
            term_a = terms[0]
            term_b = terms[1]
        else:
            # Fallback if no quotes found or weird format
            # print(f"Row {i}: Could not parse terms from tension: {tension_text[:50]}...")
            term_a = "the primary thesis"
            term_b = "the antithesis"

        # 3. Find Category Block
        c_match = re.search(r"<categorization>(.*?)</categorization>", content, re.DOTALL)
        if not c_match:
            print(f"Row {i}: No categorization tag found.")
            continue

        cat_text = c_match.group(1).strip()

        # Extract Domain from existing category text
        # Usually: "This is a 'Distressed Asset Management' dilemma..."
        domain_match = re.search(r"'(.*?)'", cat_text)
        if domain_match:
            domain = domain_match.group(1)
            # Keep the rest of the text as context?
            # "dilemma involving Capital Structure optimization..."
            # Let's just use the whole text but rephrase the start.
            context = cat_text.replace(f"This is a '{domain}'", "").replace(f"This is an '{domain}'", "").strip()
            # Clean up leading "problem" or "dilemma"
            context = re.sub(r"^(problem|dilemma|scenario|situation)\s*", "", context, flags=re.IGNORECASE)
        else:
            domain = "Complex"
            context = cat_text

        # 4. Construct New Categorization
        new_cat = (
            f"<categorization>\n"
            f"We categorize this as a '{domain}' dispute. "
            f"The Reason prioritizes '{term_a}', focusing on standard operating logic, "
            f"while the Exception argues for '{term_b}', highlighting the structural or edge-case constraints. "
            f"This creates a divergence that requires synthesizing {context if context else 'the competing frameworks'}.\n"
            f"</categorization>"
        )

        # 5. Replace
        row['Reasoning'] = content.replace(c_match.group(0), new_cat)
        fixed_count += 1

    with open(output_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    print(f"Rewrote categorization for {fixed_count} rows.")

if __name__ == "__main__":
    rewrite_categorization()
