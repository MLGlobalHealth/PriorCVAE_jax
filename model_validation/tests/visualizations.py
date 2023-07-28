"""
File contains functions for saving visualizations to wandb.
"""

import wandb
import numpy as np

from priorCVAE.diagnostics import sample_covariance
from .utils import plot_realizations, plot_heatmap


def plot_vae_realizations(samples, grid, **kwargs):
    fig, _ = plot_realizations(grid, samples, "VAE samples")
    wandb.log({"vae_realizations": wandb.Image(fig)})

    # remove media metadata from wandb summary
    del wandb.run.summary["vae_realizations"]


def plot_covariance(samples, **kwargs):
    cov_matrix = sample_covariance(samples)
    fig, ax = plot_heatmap(cov_matrix, "Empirical covariance")
    wandb.log({"covariance": wandb.Image(fig)})
    del wandb.run.summary["covariance"]


def plot_correlation(samples, **kwargs):
    corr = np.corrcoef(np.transpose(samples))
    fig, ax = plot_heatmap(corr, "Correlation")
    wandb.log({"correlation": wandb.Image(fig)})
    del wandb.run.summary["correlation"]


def plot_kernel(kernel, kernel_name, grid, **kwargs):
    K = kernel(grid, grid)
    fig, ax = plot_heatmap(K, kernel_name)
    wandb.log({"kernel": wandb.Image(fig)})
    del wandb.run.summary["kernel"]
