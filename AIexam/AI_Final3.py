import numpy as np
from sklearn.svm import SVC
import matplotlib.pyplot as plt

# Linear SVM Example
# Define data points
X_cat = np.array([[3, -1], [6, 1], [3, 1], [6, -1]])
X_dog = np.array([[1, 0], [-1, 0], [0, 1], [0, -1]])
X = np.vstack((X_cat, X_dog))
y = np.array([1, 1, 1, 1, 0, 0, 0, 0])  # 1 for CAT, 0 for DOG

# Train a linear SVM
svm_linear = SVC(kernel='linear', C=1)
svm_linear.fit(X, y)

# Non-linear SVM Example using polynomial kernel
X_cat_nl = np.array([[2, -2], [2, 2], [-2, -2], [-2, 2]])
X_dog_nl = np.array([[1, 1], [-1, 1], [-1, -1], [1, -1]])
X_nl = np.vstack((X_cat_nl, X_dog_nl))
y_nl = np.array([1, 1, 1, 1, 0, 0, 0, 0])  # 1 for CAT, 0 for DOG

# Train a non-linear SVM
svm_non_linear = SVC(kernel='rbf', gamma='auto', C=1)  # Using RBF kernel
svm_non_linear.fit(X_nl, y_nl)

# Plotting function to visualize the decision boundaries
def plot_svc_decision_function(model, ax=None, plot_support=True):
    """Plot the decision function for a 2D SVC"""
    if ax is None:
        ax = plt.gca()
    xlim = ax.get_xlim()
    ylim = ax.get_ylim()
    
    # create grid to evaluate model
    xx = np.linspace(xlim[0], xlim[1], 30)
    yy = np.linspace(ylim[0], ylim[1], 30)
    YY, XX = np.meshgrid(yy, xx)
    xy = np.vstack([XX.ravel(), YY.ravel()]).T
    Z = model.decision_function(xy).reshape(XX.shape)

    # plot decision boundary and margins
    ax.contour(XX, YY, Z, colors='k', levels=[-1, 0, 1], alpha=0.5,
               linestyles=['--', '-', '--'])
    
    # plot support vectors
    if plot_support:
        ax.scatter(model.support_vectors_[:, 0],
                   model.support_vectors_[:, 1],
                   s=300, linewidth=1, facecolors='none', edgecolors='k')
    ax.set_xlim(xlim)
    ax.set_ylim(ylim)

# Plot results
plt.figure(figsize=(12, 6))
plt.subplot(121)
plt.scatter(X[:, 0], X[:, 1], c=y, cmap='autumn')
plot_svc_decision_function(svm_linear)
plt.title("Linear SVM")

plt.subplot(122)
plt.scatter(X_nl[:, 0], X_nl[:, 1], c=y_nl, cmap='autumn')
plot_svc_decision_function(svm_non_linear)
plt.title("Non-linear SVM with RBF Kernel")

plt.show()
