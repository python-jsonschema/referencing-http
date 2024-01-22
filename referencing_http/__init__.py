"""
Serve your JSON registries over HTTP, for humans and machines alike!
"""
from importlib.resources import files

import yaml

SPEC = yaml.safe_load(files(__package__).joinpath("api.yaml").read_text())
