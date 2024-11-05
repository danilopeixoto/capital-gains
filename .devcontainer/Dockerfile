FROM python:3.10-buster

ENV SETUPTOOLS_SCM_PRETEND_VERSION=0.0.0

RUN groupadd --gid 1000 developer \
    && useradd --uid 1000 --gid developer --shell /bin/bash --create-home developer

WORKDIR /workspaces/capital-gains
