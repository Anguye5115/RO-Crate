# Installation and Run Instructions

1) [Install Micromamba](https://mamba.readthedocs.io/en/latest/installation/micromamba-installation.html)

2) Run the following:

```
$ eval "$(micromamba shell hook -s ${SHELL})"
$ micromamba create -n bm8-env python=3.10 poetry
$ micromamba activate bm8-env
```
3) Run `poetry install` from the `benchmark8` directory

4) Run `python benchmark8a.py params8a.yaml` in the `benchmark8` directory
