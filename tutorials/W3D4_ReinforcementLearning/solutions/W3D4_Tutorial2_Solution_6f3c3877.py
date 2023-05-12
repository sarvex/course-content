def epsilon_greedy(q, epsilon):
  """Epsilon-greedy policy: selects the maximum value action with probabilty
  (1-epsilon) and selects randomly with epsilon probability.

  Args:
    q (ndarray): an array of action values
    epsilon (float): probability of selecting an action randomly

  Returns:
    int: the chosen action
  """
  # write a boolean expression that determines if we should take the best action
  be_greedy = np.random.random() > epsilon
  return np.argmax(q) if be_greedy else np.random.choice(len(q))


q = [-2, 5, 0, 1]
epsilon = 0.1
with plt.xkcd():
  plot_choices(q, epsilon, epsilon_greedy)