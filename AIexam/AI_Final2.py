# from pgmpy.models import BayesianModel
# from pgmpy.factors.discrete import TabularCPD

# # Define the structure of the Bayesian network
# model = BayesianModel([
#     ('PF', 'IW'),  # Physical Fitness to Immunity Challenge Wins
#     ('SG', 'HI'),  # Strategic Gameplay to Hidden Immunity Idols
#     ('SS', 'PO'),  # Social Skills to Perception by Others
#     ('IW', 'SW'),  # Immunity Challenge Wins to Survive the Week
#     ('HI', 'SW'),  # Hidden Immunity Idols to Survive the Week
#     ('PO', 'SW')   # Perception by Others to Survive the Week
# ])

# # Define the Conditional Probability Distributions (CPDs)
# cpd_pf = TabularCPD(variable='PF', variable_card=3, values=[[0.1], [0.6], [0.3]], state_names={'PF': ['Low', 'Moderate', 'High']})
# cpd_sg = TabularCPD(variable='SG', variable_card=3, values=[[0.3], [0.4], [0.3]], state_names={'SG': ['Weak', 'Average', 'Strong']})
# cpd_ss = TabularCPD(variable='SS', variable_card=3, values=[[0.4], [0.4], [0.2]], state_names={'SS': ['Weak', 'Moderate', 'Strong']})
# cpd_iw = TabularCPD(variable='IW', variable_card=2, evidence=['PF'], evidence_card=[3], 
#                     values=[[0.95, 0.8, 0.5],  # Won
#                             [0.05, 0.2, 0.5]],  # Lost
#                     state_names={'IW': ['Won', 'Lost'], 'PF': ['Low', 'Moderate', 'High']})
# cpd_hi = TabularCPD(variable='HI', variable_card=2, evidence=['SG'], evidence_card=[3], 
#                     values=[[0.1, 0.3, 0.6],  # Found
#                             [0.9, 0.7, 0.4]],  # Not Found
#                     state_names={'HI': ['Found', 'Not Found'], 'SG': ['Weak', 'Average', 'Strong']})
# cpd_po = TabularCPD(variable='PO', variable_card=2, evidence=['SS'], evidence_card=[3], 
#                     values=[[0.2, 0.6, 0.8],  # Threat
#                             [0.8, 0.4, 0.2]],  # Ally
#                     state_names={'PO': ['Threat', 'Ally'], 'SS': ['Weak', 'Moderate', 'Strong']})
# cpd_sw = TabularCPD(variable='SW', variable_card=2, evidence=['IW', 'HI', 'PO'], evidence_card=[2, 2, 2], 
#                     values=[[0.99, 0.95, 0.95, 0.6, 0.95, 0.6, 0.6, 0.3],  # Survive
#                             [0.01, 0.05, 0.05, 0.4, 0.05, 0.4, 0.4, 0.7]],  # Don't Survive
#                     state_names={'SW':["Survive', 'Don't Survive"], 'IW': ['Won', 'Lost'], 
#                                  'HI': ['Found','Not Found'], 'PO': ['Threat', 'Ally']})

# # Add CPDs to the model
# model.add_cpds(cpd_pf, cpd_sg, cpd_ss, cpd_iw, cpd_hi, cpd_po, cpd_sw)

# # Validate the model
# assert model.check_model()

# # Performing inference
# from pgmpy.inference import VariableElimination
# inference = VariableElimination(model)

# # Query the network for John's probability of survival with high physical fitness, strong gameplay, and moderate social skills
# result = inference.query(variables=['SW'], evidence={'PF': 'High', 'SG': 'Strong', 'SS': 'Moderate'})
# print(result)

from pgmpy.models import BayesianNetwork as BayesianModel  # Updated class name
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

# Create the Bayesian Network
model = BayesianModel([
    ('PF', 'IW'),
    ('SG', 'HI'),
    ('SS', 'PO'),
    ('IW', 'SW'),
    ('HI', 'SW'),
    ('PO', 'SW')
])

# Define CPDs
cpd_pf = TabularCPD('PF', 3, [[0.1], [0.6], [0.3]], state_names={'PF': ['Low', 'Moderate', 'High']})
cpd_sg = TabularCPD('SG', 3, [[0.3], [0.4], [0.3]], state_names={'SG': ['Weak', 'Average', 'Strong']})
cpd_ss = TabularCPD('SS', 3, [[0.4], [0.4], [0.2]], state_names={'SS': ['Weak', 'Moderate', 'Strong']})
cpd_iw = TabularCPD('IW', 2, [[0.95, 0.8, 0.5], [0.05, 0.2, 0.5]], evidence=['PF'], evidence_card=[3], state_names={'IW': ['Won', 'Lost'], 'PF': ['Low', 'Moderate', 'High']})
cpd_hi = TabularCPD('HI', 2, [[0.1, 0.3, 0.6], [0.9, 0.7, 0.4]], evidence=['SG'], evidence_card=[3], state_names={'HI': ['Found', 'Not Found'], 'SG': ['Weak', 'Average', 'Strong']})
cpd_po = TabularCPD('PO', 2, [[0.2, 0.6, 0.8], [0.8, 0.4, 0.2]], evidence=['SS'], evidence_card=[3], state_names={'PO': ['Threat', 'Ally'], 'SS': ['Weak', 'Moderate', 'Strong']})
cpd_sw = TabularCPD('SW', 2, [[0.99, 0.95, 0.95, 0.6, 0.95, 0.6, 0.6, 0.3], [0.01, 0.05, 0.05, 0.4, 0.05, 0.4, 0.4, 0.7]], evidence=['IW', 'HI', 'PO'], evidence_card=[2, 2, 2], 
                    state_names={'SW': ['Survive', "Don't Survive"], 'IW': ['Won', 'Lost'], 'HI': ['Found', 'Not Found'], 'PO': ['Threat', 'Ally']})

# Add CPDs to the model and validate
model.add_cpds(cpd_pf, cpd_sg, cpd_ss, cpd_iw, cpd_hi, cpd_po, cpd_sw)
assert model.check_model()

# Performing inference
inference = VariableElimination(model)

# Query the network
query_result = inference.query(variables=['SW'], evidence={'PF': 'High', 'SG': 'Strong', 'SS': 'Moderate'})

# Properly extract and print the probability distribution from the query result
for state in query_result.state_names['SW']:
    print(f"Probability of {state}: {query_result.values[query_result.state_names['SW'].index(state)]:.4f}")
