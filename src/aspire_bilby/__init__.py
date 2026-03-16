"""aspire-bilby: A Bilby wrapper for aspire."""

from importlib.metadata import PackageNotFoundError, version
try:
    import jax
    jax.config.update("jax_enable_x64", True)
except ImportError:
    pass

try:
    import torch
    torch.set_default_dtype(torch.float64)
except ImportError:
    pass

try:
    __version__ = version(__name__)
except PackageNotFoundError:
    # package is not installed
    __version__ = "unknown"