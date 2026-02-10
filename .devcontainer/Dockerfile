FROM mcr.microsoft.com/devcontainers/miniconda

RUN conda install -n base -c conda-forge mamba && conda init
COPY .binder/environment.yml /tmp/conda-tmp/

RUN if [ -f "/tmp/conda-tmp/environment.yml" ]; then umask 0002 && /opt/conda/bin/mamba env create -f /tmp/conda-tmp/environment.yml; fi \
    && rm -rf /tmp/conda-tmp
