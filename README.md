## Pytorch

My `pytorch` conda env came from

```bash
$ conda install -c conda-forge notebook
$ conda install -c conda-forge nb_conda_kernels
$ conda install pytorch torchvision torchaudio pytorch-cuda=11.7 -c pytorch -c nvidia  # install pytorch with cuda support
```


```py
import torch
print(torch.cuda.is_available()) # expected to print True
```


[Trouble-shooting](https://hypocrptoshit.medium.com/systematicly-fix-cuda-not-available-in-conda-4d06849fa378)
