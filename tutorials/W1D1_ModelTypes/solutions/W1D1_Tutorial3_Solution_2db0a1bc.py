def pmf_from_counts(counts):
  """Given counts, normalize by the total to estimate probabilities."""
  return counts / np.sum(counts)


# Get neuron index
neuron_idx = 283

# Get counts of ISIs from Steinmetz data
isi = np.diff(steinmetz_spikes[neuron_idx])
bins = np.linspace(*isi_range, n_bins + 1)
counts, _ = np.histogram(isi, bins)

# Compute pmf
pmf = pmf_from_counts(counts)

# Visualize
with plt.xkcd():
  plot_pmf(pmf,isi_range)