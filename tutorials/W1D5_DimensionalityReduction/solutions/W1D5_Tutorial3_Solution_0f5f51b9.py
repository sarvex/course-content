def get_variance_explained(evals):
  """
  Plots eigenvalues.

  Args:
    (numpy array of floats) : Vector of eigenvalues

  Returns:
    Nothing.

  """

  # cumulatively sum the eigenvalues
  csum = np.cumsum(evals)
  return csum / np.sum(evals)


# calculate the variance explained
variance_explained = get_variance_explained(evals)
with plt.xkcd():
  plot_variance_explained(variance_explained)