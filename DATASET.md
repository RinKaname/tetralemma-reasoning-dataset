# Dataset Description

## Overview
Where does this data come from? What does it represent?
Original source: RinKana/tetralemma-reasoning-dataset-V5

This dataset is designed to train and evaluate Large Language Models (LLMs) in advanced "deconstructivist" and "lateral" reasoning. It specifically trains models to navigate complex, non-binary "wicked problems" using a 4-fold logic system (Tetralemma), rejecting simple Aristotelian/binary (Yes/No) outputs in favor of nuanced meta-cognition.

The dataset contains deep, intersectional dilemmas across diverse domains such as Philosophy, Political Science, Theoretical Physics, AI Alignment, Economics, Corporate Finance, Bioethics, and Game Theory. It teaches the model that strategic best practices and moral judgments are highly context-dependent.

## File Structure
- `tetralemma-reasoning-train.csv` / `.parquet` — The primary training dataset containing both the complex questions and the structured, 6-tag Tetralemma reasoning answers.
- `tetralemma-reasoning-test.csv` / `.parquet` — The testing dataset containing **only the questions**, used for direct model evaluation and benchmarking.
- `solution/solution.csv` / `.parquet` — The complete evaluation dataset containing the test questions mapped to their ground-truth Tetralemma reasoning answers.
- `sample_submission.csv` — A template file demonstrating the expected format for competition submissions. It contains all test questions paired with placeholder XML reasoning blocks.

## Features

### Training and Solution Files (`tetralemma-reasoning-train.csv`, `solution/solution.csv`)
| Column    | Type | Description |
|-----------|------|-------------|
| Question  | str  | A complex, intersectional scenario or dilemma designed to challenge binary reasoning. |
| Reasoning | str  | The ground-truth answer, strictly formatted using six specific XML tags to enforce the Tetralemma logic structure. |

### Test Files (`tetralemma-reasoning-test.csv`)
| Column    | Type | Description |
|-----------|------|-------------|
| Question  | str  | The evaluation input for the model. |

## Notes
**Tetralemma XML Structure:**
When training or evaluating, the target output (`Reasoning`) must adhere to the following six tags to successfully deconstruct the problem:
1. `<reason>`: The thesis or primary justification for one side of the argument.
2. `<exception>`: The antithesis, negation, or exception to the thesis.
3. `<tension>`: The divergence or underlying conflict between the thesis and antithesis.
4. `<categorization>`: The rule/exception segregation or synthesis. It must synthesize specific arguments (e.g., "prioritizes avoiding Sunk Cost Fallacy") rather than generic extractions like "prioritizes Yes."
5. `<deconstruction>`: The refutation or breaking down of the binary premise of the question itself.
6. `<conclusion>`: The final recap and nuanced resolution of the dilemma.

**Training Constraints:**
For fine-tuning SLMs/LLMs using LoRA/QLoRA on this dataset, it is recommended to use a learning rate of `2e-4` and run for `3` to `5` epochs to avoid overfitting while ensuring strict adherence to the complex XML tag format. The data contains scenarios deliberately framed to teach constraint-based reasoning (e.g., differing strategies based on scale or context).
