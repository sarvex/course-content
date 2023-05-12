def F_inv(x, a, theta):
  """
  Args:
    x         : the population input
    a         : the gain of the function
    theta     : the threshold of the function

  Returns:
    F_inverse : value of the inverse function
  """

  return -1/a * np.log((x + (1 + np.exp(a * theta))**-1)**-1 - 1) + theta

pars = default_pars()
x = np.linspace(1e-6, 1, 100)

with plt.xkcd():
  plot_FI_inverse(x, a=1, theta=3)