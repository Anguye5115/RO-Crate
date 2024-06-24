# SURF 2024 Project

## Main Resources

 - [Phase Field Schema WG GitHub Repository](https://github.com/marda-alliance/phase-field-schema)
 - [Google Drive Material](https://drive.google.com/drive/u/1/folders/1zhUi3A-CXxrkh4gTkLVUOncdqAMIAXND)
 - [Overleaf Paper](https://www.overleaf.com/project/663e34cc1c8095115e0de913)
 - [Recording provenance of workflow runs with RO-Crate](https://doi.org/10.48550/arXiv.2312.07852)
 - [RO-Crate Tutorial](https://www.researchobject.org/packaging_data_with_ro-crate/01-introduction/index.html)
 - [Workflow Run RO-Crate Introduction](https://training.galaxyproject.org/training-material/topics/fair/tutorials/ro-crate-workflow-run-ro-crate/tutorial.html)
 - [RO-Crate - Introduction](https://training.galaxyproject.org/training-material/topics/fair/tutorials/ro-crate-intro/tutorial.html)
 - [Presentation about RO-Crate](https://gallantries.github.io/video-library/videos/ro-crates/intro/slides/)
 - [Shared metadata for data-centric materials science](https://doi.org/10.1038/s41597-023-02501-8)
 - [The role of metadata in reproducible computational research](202404011304-role-of-metadata.md)
 - [The Semantic Data Dictionary](https://doi.org/10.1162/dint_a_00058)
 - [The Materials Cloud Platform](https://doi.org/10.1038/s41597-020-00637-5)
 - [Recording provenance of workflow runs with RO-Crate](https://doi.org/10.48550/arXiv.2312.07852)
 
## CTCMS Help

- [Access](https://ctcms.ipages.nist.gov)
- [CTCMS wiki](https://gitlab.nist.gov/gitlab/ctcms/ctcms.ipages.nist.gov/-/wikis/CTCMS-Wiki)

## Other Resources

- https://asistdl.onlinelibrary.wiley.com/doi/10.1002/asi.24744
- [ir_metadata](https://www.ir-metadata.org)

## Installation and Run Instructions

1) [Install Micromamba](https://mamba.readthedocs.io/en/latest/installation/micromamba-installation.html)

2) Run the following:

```
$ eval "$(micromamba shell hook -s bashx)"
$ micromamba create -n bm8-env python=3.11 poetry=1.8.2
$ micromamba activate bm8-env
```
3) Run `poetry install` from the `benchmark8` directory

4) Test that the python simulation runs with 

```
$ cd benchmark8
$ python benchmark8a.py params8a.yaml`
```

5) Test that the ro-crate build works

```
$ cd example
$ python build_rocrate.py
```
