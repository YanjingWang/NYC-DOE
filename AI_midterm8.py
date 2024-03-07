from pgmpy.models import BayesianNetwork
from pgmpy.independencies import Independencies
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

# Define the Bayesian network structure
model = BayesianNetwork([
    ('B_shmi', 'G_anakin'),
    ('G_anakin', 'G_luke'),
    ('G_anakin', 'G_leia'),
    ('G_anakin', 'B_anakin'),
    ('G_luke', 'B_luke'),
    ('G_leia', 'B_leia'),
    ('G_leia', 'G_ben'),
    ('G_ben', 'B_ben'),
    ('G_padme', 'G_leia'),
    ('G_padme', 'G_luke'),
    ('G_han', 'G_ben')
])
# Define CPDs
cpd_B_shmi = TabularCPD(variable='B_shmi', variable_card=2, values=[[0.5], [0.5]])
cpd_G_anakin = TabularCPD(variable='G_anakin', variable_card=2, 
                          values=[[0.1, 0.9], [0.9, 0.1]],
                          evidence=['B_shmi'],
                          evidence_card=[2])

# Other CPDs would be defined in a similar manner...

# Add CPDs to the model
model.add_cpds(cpd_B_shmi, cpd_G_anakin)

# Define a custom function to check for an active trail
def is_active_trail(model, start, end, observed=None):
    """
    Checks if there is an active trail between start and end given observed variables.
    
    Parameters:
    - model: A BayesianModel object.
    - start: Start node.
    - end: End node or nodes (list).
    - observed: Nodes to be observed (list).

    Returns:
    - Boolean indicating if an active trail exists.
    """
    # Ensure end is a list for consistency
    if not isinstance(end, list):
        end = [end]
    
    # Initialize VariableElimination with the model
    inference = VariableElimination(model)
    
    # Use d-separation to check for active trail
    for target in end:
        # Check if start and target are d-separated
        if observed:
            d_separated = inference.induced_graph(observed).is_dconnected(start, target, observed)
        else:
            d_separated = model.is_dconnected(start, target)
        
        # If any target is not d-separated, there's an active trail
        if d_separated:
            return True
    
    # If all targets are d-separated, no active trail exists
    return False

# Example usage
observed = ['G_anakin']
active_trail = is_active_trail(model, 'G_luke', ['G_shmi', 'B_shmi'], observed=observed)
print(f"Active trail between 'G_luke' and ['G_shmi', 'B_shmi'] given {observed}: {active_trail}")
