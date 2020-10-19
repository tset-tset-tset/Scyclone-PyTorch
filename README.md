<div align="center">

# Scyclone-PyTorch <!-- omit in toc -->
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)][notebook]
[![Paper](http://img.shields.io/badge/paper-arxiv.2005.03334-B31B1B.svg)][paper]  

</div>

Reimplmentation of voice conversion system "Scyclone" with PyTorch.

- [Demo](#demo)
- [How to run](#how-to-run)
- [Install](#install)
- [Original paper](#original-paper)
- [Difference from original research](#difference-from-original-research)
- [Dependency Notes](#dependency-notes)

## Demo
Link super great impressive high-quatity audio demo.

## How to run
### Training <!-- omit in toc -->
Jump to **[Notebook in Google Colaboratory][notebook]**, then Run. that's all!!  

## Install
(If your machine needs specific PyTorch version (e.g. old CUDA compatible version), install it before Scyclone installation.)  

```bash
pip install git+https://github.com/tarepan/Scyclone-PyTorch
```

## Original paper
[![Paper](http://img.shields.io/badge/paper-arxiv.2005.03334-B31B1B.svg)][paper]  
<!-- https://arxiv2bibtex.org/?q=2005.03334&format=bibtex -->
```
@misc{2005.03334,
Author = {Masaya Tanaka and Takashi Nose and Aoi Kanagaki and Ryohei Shimizu and Akira Ito},
Title = {Scyclone: High-Quality and Parallel-Data-Free Voice Conversion Using Spectrogram and Cycle-Consistent Adversarial Networks},
Year = {2020},
Eprint = {arXiv:2005.03334},
}
```

**[Original Paper's Demo](http://www.spcom.ecei.tohoku.ac.jp/nose/research/scyclone_202001/)**

## Difference from original research
- Datum length is based on a paper, not poster (G160/D128 in paper, G240/D240 in poster. Detail is in my summary blog)
- Use Automatic Mixed Precision training (FP32 training is also supported through `no_amp` flag)

## Dependency Notes
### PyTorch version <!-- omit in toc -->
PyTorch version: PyTorch v1.6 is working (We checked with v1.6.0).  

For dependency resolution, we do **NOT** explicitly specify the compatible versions.  
PyTorch have several distributions for various environment (e.g. compatible CUDA version.)  
Unfortunately it make dependency version management complicated for dependency management system.  
In our case, the system `poetry` cannot handle cuda variant string (e.g. `torch>=1.6.0` cannot accept `1.6.0+cu101`.)  
In order to resolve this problem, we use `torch==*`, it is equal to no version specification.  
`Setup.py` could resolve this problem (e.g. `torchaudio`'s `setup.py`), but we will not bet our effort to this hacky method.  

[paper]:https://arxiv.org/abs/2005.03334
[notebook]:https://colab.research.google.com/github/tarepan/Scyclone-PyTorch/blob/main/Scyclone_PyTorch.ipynb