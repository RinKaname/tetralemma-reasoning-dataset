#!/usr/bin/env python3
"""
Script to generate 50 STEM questions in tetralemma format and append to qwen-suggestion.txt
"""

import random

def generate_stem_question():
    """Generate a STEM question with tetralemma reasoning structure"""
    
    # STEM categories
    stem_categories = [
        ("Physics", [
            "Calculate the energy of a photon with wavelength 500 nm and explain its interaction with matter.",
            "A particle moves with velocity v(t) = 3t² + 2t. Find its acceleration and displacement at t=5s.",
            "Explain the principle of electromagnetic induction and calculate the induced EMF in a coil.",
            "A heat engine operates between 400K and 300K. Calculate its maximum efficiency and explain Carnot's theorem.",
            "An electron moves in a magnetic field. Calculate the radius of its circular path and explain the Lorentz force."
        ]),
        ("Chemistry", [
            "Balance the equation for the combustion of methane and calculate the enthalpy change.",
            "Explain the hybridization in SF₆ and predict its molecular geometry.",
            "Calculate the pH of a 0.1 M acetic acid solution with Ka = 1.8×10⁻⁵.",
            "Explain the mechanism of nucleophilic substitution in organic chemistry.",
            "Calculate the cell potential for a galvanic cell with Zn/Zn²⁺ and Cu/Cu²⁺ half-cells."
        ]),
        ("Mathematics", [
            "Solve the differential equation dy/dx = 2x + 3 and find the particular solution with y(0)=1.",
            "Find the eigenvalues and eigenvectors of the matrix [[2, 1], [1, 2]].",
            "Calculate the volume of a solid of revolution formed by rotating y=x² around the x-axis.",
            "Prove that the sum of the first n natural numbers is n(n+1)/2.",
            "Find the Taylor series expansion of f(x) = e^x around x=0."
        ]),
        ("Biology", [
            "Explain the process of photosynthesis and calculate the energy efficiency of converting light to glucose.",
            "Describe the lac operon and explain how gene expression is regulated in prokaryotes.",
            "Explain the mechanism of DNA replication and the role of key enzymes.",
            "Calculate the Hardy-Weinberg equilibrium for a population with allele frequencies p=0.7 and q=0.3.",
            "Explain the structure and function of the human heart and blood circulation."
        ]),
        ("Computer Science", [
            "Explain the time complexity of merge sort and compare it with quicksort.",
            "Design an algorithm to detect cycles in a directed graph.",
            "Explain how hash tables work and calculate the load factor for a given implementation.",
            "Describe the difference between depth-first search and breadth-first search in graphs.",
            "Explain the concept of recursion and provide an example with factorial calculation."
        ]),
        ("Engineering", [
            "Calculate the stress and strain in a steel rod under a given load.",
            "Explain the principles of fluid dynamics and calculate the flow rate through a pipe.",
            "Design a simple electronic circuit with resistors in series and parallel.",
            "Explain the concept of resonance in mechanical systems.",
            "Calculate the efficiency of a Carnot engine operating between two temperatures."
        ])
    ]
    
    # Select a random category and question
    category, questions = random.choice(stem_categories)
    question = random.choice(questions)
    
    # Tetralemma reasoning template
    tetralemma_template = """<reason>
{reason}
</reason>

<exception>
{exception}
</exception>

<tension>
{tension}
</tension>

<categorization>
{categorization}
</categorization>

<deconstruction>
{deconstruction}
</deconstruction>

<conclusion>
{conclusion}
</conclusion>"""
    
    # Generate reasoning components based on the question
    reason = f"The fundamental principle behind this {category.lower()} problem involves established scientific laws and mathematical frameworks that provide a clear solution pathway. Using well-established formulas and concepts in {category.lower()}, we can systematically approach this problem."
    
    exception = f"However, there are important limitations and edge cases to consider. The model assumptions may not hold in certain conditions - for instance, quantum effects at very small scales, relativistic effects at high speeds, or environmental factors that could affect the outcome. These exceptions challenge the straightforward application of the basic principles."
    
    tension = f"This creates a tension between the theoretical solution based on ideal conditions and the practical complexities that arise in real-world applications. The mathematical solution provides one perspective, while the physical or practical constraints provide another, seemingly contradictory perspective."
    
    categorization = f"We can categorize the problem as belonging to {category.lower()} fundamentals, but it also intersects with related fields. This question demonstrates how {category.lower()} concepts connect with mathematics, physics, or other sciences depending on the specific application."
    
    deconstruction = f"Upon deeper analysis, the apparent contradiction between theoretical and practical solutions dissolves when we consider the multi-layered nature of scientific problems. The ideal solution and the real-world complexities are not mutually exclusive but rather represent different levels of approximation and different contexts of application."
    
    conclusion = f"The comprehensive solution acknowledges both the fundamental theoretical principles and the practical considerations. In {category.lower()}, as in most STEM fields, solutions exist at multiple levels of complexity, and the most complete understanding incorporates both the mathematical precision and the real-world applicability."
    
    reasoning = tetralemma_template.format(
        reason=reason,
        exception=exception,
        tension=tension,
        categorization=categorization,
        deconstruction=deconstruction,
        conclusion=conclusion
    )
    
    return question, reasoning

def main():
    # Generate 50 STEM questions with tetralemma reasoning
    with open('qwen-suggestion.txt', 'a', encoding='utf-8') as f:
        for i in range(50):
            question, reasoning = generate_stem_question()
            
            # Write the question and reasoning to the file
            f.write(f"Question: {question}\n")
            f.write(f"Reasoning: {reasoning}\n")
            f.write("\n" + "="*80 + "\n\n")  # Separator between questions
            
            print(f"Generated question {i+1}/50")

if __name__ == "__main__":
    main()