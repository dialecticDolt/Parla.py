# Parla

Parla is a prototype high level tasking system for orchestrating many heterogeneous kernel calls.

# Installation

Parla is available as a conda package. It requires Python 3.7, numpy, and cupy. The examples also make extensive use of numba.

To install miniconda you can follow the instructions available at [https://docs.conda.io/en/latest/miniconda.html](https://docs.conda.io/en/latest/miniconda.html).
If you are running Linux and have `wget` available, you can download and install miniconda into the miniconda subdirectory of your home directory by running

```
wget https://repo.continuum.io/miniconda/Miniconda2-latest-Linux-x86_64.sh -O miniconda.sh
bash miniconda.sh -b -p $HOME/miniconda
rm miniconda.sh
```

To make miniconda available on your path in a given terminal session run
```
export PATH=$HOME/miniconda/bin:$PATH
source activate
```

Once that's done, you can install parla by running

```
conda install -c insertinterestingnamehere parla
```

If you have already installed parla but need to access your miniconda installation from a new terminal session just run (as before)
```
export PATH=$HOME/miniconda/bin:$PATH
source activate
```

Once parla is installed and your environment is configured to use it, all the scripts in this repository's examples directory are runnable as normal python scripts.
If git is installed you can clone the repository and run the inner product example by running:

```
git clone https://github.com/ut-parla/Parla.py
python Parla.py/examples/inner.py
```

If git is not available, you can just install it as a conda package alongside parla by running `conda install git` once the miniconda installation is accessible from a given terminal session.

