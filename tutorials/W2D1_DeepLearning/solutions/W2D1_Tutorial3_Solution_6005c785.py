def RDM(resp):
  """Compute the representational dissimilarity matrix (RDM)

  Args:
    resp (ndarray): S x N matrix with population responses to
      each stimulus in each row

  Returns:
    ndarray: S x S representational dissimilarity matrix
  """

  # z-score responses to each stimulus
  zresp = zscore(resp, axis=1)

  return 1 - (zresp @ zresp.T) / zresp.shape[1]

# Compute RDMs
rdm_dict = {label: RDM(resp) for label, resp in resp_dict.items()}

# Plot RDMs
with plt.xkcd():
  plot_multiple_rdm(rdm_dict)