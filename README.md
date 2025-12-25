# Tetralemma Deconstructivist Reasoning Dataset

A comprehensive dataset for training and evaluating AI models on tetralemma-based deconstructivist reasoning tasks. This dataset explores the logical framework of the tetralemma (catuskoti), a four-valued logic system from Buddhist and Hindu philosophy that considers four possibilities: existence, non-existence, both, and neither.

## Overview

The Tetralemma Deconstructivist Reasoning Dataset is designed to challenge AI models with complex reasoning tasks that go beyond binary logic. The dataset contains carefully crafted examples that require models to navigate the four logical positions of the tetralemma:

1. **A** (Assertion) - The proposition is true
2. **¬A** (Negation) - The proposition is false  
3. **A ∧ ¬A** (Both) - The proposition is both true and false
4. **¬(A ∨ ¬A)** (Neither) - The proposition is neither true nor false

## Dataset Structure

The dataset is split into training and testing components:

- `tetralemma-reasoning-train.csv` - Training dataset (192 examples)
- `tetralemma-reasoning-test.csv` - Testing dataset (5 examples)
- `tetralemma-reasoning-train.parquet` - Training dataset in Parquet format
- `tetralemma-reasoning-test.parquet` - Testing dataset in Parquet format
- `tetralemma-reasoning-train.ipynb` - Training notebook with examples

## Data Format

Each entry in the dataset contains:

- `Question`: The philosophical or ethical question to be analyzed
- `Reasoning`: A structured response containing multiple components:
  - `<reason>`: Initial reasoning about the question
  - `<exception>`: Counter-arguments or exceptions to the initial reasoning
  - `<tension>`: Identification of tensions or contradictions
  - `<categorization>`: Categorization of different approaches or solutions
  - `<deconstruction>`: Deconstructivist analysis breaking down assumptions
  - `<conclusion>`: Final conclusion based on the analysis

## Applications

This dataset is valuable for:

- Training models in non-binary logical reasoning
- Evaluating AI's capacity for deconstructivist thought
- Research in philosophical AI and multi-valued logics
- Developing systems that can handle contradictory or paradoxical statements
- Advancing interpretability in AI reasoning systems

## Usage Examples

```python
import pandas as pd

# Load the training dataset
train_df = pd.read_csv('tetralemma-reasoning-train.csv')

# Example of reasoning task
sample = train_df.iloc[0]
print(f"Question: {sample['Question']}")
print(f"Reasoning: {sample['Reasoning']}")

# You can parse the structured reasoning components
import re

def extract_reasoning_components(reasoning_text):
    components = {}
    for tag in ['reason', 'exception', 'tension', 'categorization', 'deconstruction', 'conclusion']:
        pattern = f'<{tag}>(.*?)</{tag}>'
        match = re.search(pattern, reasoning_text, re.DOTALL)
        if match:
            components[tag] = match.group(1).strip()
    return components

# Extract components from a sample
components = extract_reasoning_components(sample['Reasoning'])
for tag, content in components.items():
    print(f"{tag.upper()}: {content[:100]}...")  # Print first 100 chars
```

## Dataset Statistics

- Total examples: 197 (192 training + 5 testing)
- Training examples: 192
- Test examples: 5
- Features: Question, Reasoning (with structured components)
- Average reasoning length: Approximately 1000+ characters per response

## Citation

If you use this dataset in your research, please cite:

```
@dataset{tetralemma_reasoning_2025,
  title={Tetralemma Deconstructivist Reasoning Dataset},
  author={Chakrabhuana Vishnu Deva},
  year={2025},
  publisher={GitHub},
  url={https://github.com/RinKaname/tetralemma-reasoning-dataset}
}
```

## License

This dataset is released under the Apache License 2.0. See the LICENSE file for more details.

## Contributing

We welcome contributions to expand and improve this dataset. Please submit pull requests or open issues for suggestions.

## Acknowledgments

This dataset draws inspiration from Buddhist and Hindu philosophical traditions, particularly the tetralemma (catuskoti) logical framework. We acknowledge the scholars and philosophers whose work has informed this project.
