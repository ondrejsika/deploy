#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name = "deploy",
    version = "1.9.1",
    url = 'https://github.com/ondrejsika/deploy',
    license = 'MIT',
    description = "Easy deploy Python WSGI apps",
    author = 'Ondrej Sika',
    author_email = 'ondrej@ondrejsika.com',
    packages = find_packages(),
    scripts = [
        "deploy/bin/deploy",
        "deploy/bin/deploy-startserver",
        "deploy/bin/deploy-serverconf",
        "deploy/bin/deploy-init",
        "deploy/bin/deploy-restart",
        "deploy/bin/deploy-remove",
    ],
    install_requires = [],
)
