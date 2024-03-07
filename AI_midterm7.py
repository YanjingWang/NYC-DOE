from pgmpy.models import BayesianModel
from pgmpy.independencies import Independencies
from pgmpy.models import BayesianNetwork
# Define the Bayesian network structure
model = BayesianNetwork([
    ('B_shmi', 'G_anakin'),  # Shmi's midi-chlorian count influences Anakin's genotype
    ('G_anakin', 'G_luke'),  # Anakin's genotype influences Luke's genotype
    ('G_anakin', 'G_leia'),  # Anakin's genotype influences Leia's genotype
    ('G_anakin', 'B_anakin'),  # Anakin's genotype influences his midi-chlorian count
    ('G_luke', 'B_luke'),  # Luke's genotype influences his midi-chlorian count
    ('G_leia', 'B_leia'),  # Leia's genotype influences her midi-chlorian count
    ('G_leia', 'G_ben'),    # Leia's genotype influences Ben's genotype
    ('G_ben', 'B_ben'),     # Ben's genotype influences his midi-chlorian count
    ('G_padme', 'G_leia'),  # Padme's genotype influences Leia's genotype
    ('G_padme', 'G_luke'),  # Padme's genotype influences Luke's genotype
    ('G_han', 'G_ben')      # Han's genotype influences Ben's genotype
])

# Check conditional independencies
independencies = Independencies()
model.get_independencies()

# Query the independencies as required
# For example, for Q 6.1.1.1:
independence_6_1_1_1 = model.is_active_trail('G_luke', ['G_shmi', 'B_shmi'], observed='G_anakin')

# Print the results
print(f"Q 6.1.1.1: {independence_6_1_1_1}")  # Should print False as G_luke is not independent of G_shmi, B_shmi given G_anakin

# Similarly, you can write queries for other questions and print the results.
# Define a function to check independence
def check_independence(X, Y, Z=None):
    return model.is_active_trail(X, Y, observed=Z)

# Check for each condition as per the questions
results = {
    'Q6.1.1.1': check_independence('G_luke', ['G_shmi', 'B_shmi'], 'G_anakin'),
    'Q6.1.1.2': check_independence('B_shmi', 'G_anakin'),
    'Q6.1.1.3': check_independence('B_shmi', 'G_anakin', 'G_shmi'),
    'Q6.1.1.4': check_independence('B_luke', 'G_anakin', 'G_luke'),
    'Q6.1.1.5': check_independence('B_luke', 'B_leia'),
    'Q6.1.1.6': check_independence('B_luke', 'B_leia', 'G_padme'),
    'Q6.1.1.7': check_independence('G_anakin', 'G_padme', 'G_luke'),
    'Q6.1.1.8': check_independence('B_ben', 'B_luke', 'G_padme'),
    'Q6.1.1.9': check_independence('B_luke', 'B_han'),
    'Q6.1.1.10': check_independence('B_leia', 'B_han'),
    'Q6.1.1.11': check_independence('G_leia', 'G_han')
}

# Print the results
for question, result in results.items():
    print(f"{question}: {'Independent' if result else 'Dependent'}")


# AttributeError: 'BayesianNetwork' object has no attribute 'is_active_trail'
# write Python code for attribute 'is_active_trail'
def is_active_trail(self, X, Y, observed=None):
    """
    Returns True if there is an active trail between the variables X and Y given the observed variables.

    Parameters
    ----------
    X: int, string (node)
        The source node for the trail.

    Y: int, string (node)
        The target node for the trail.

    observed: list, array-like
        List of variables that have been observed. If None, no variables have been observed.

    Returns
    -------
    bool: True if there is an active trail between X and Y given the observed variables, False otherwise.
    """
    if observed is None:
        observed = []
    return self._active_trail_nodes(X, observed=observed).issuperset({Y})
    