# coding: utf-8

import os
import click

from .utils import nbeerror


DEFAULT_ENV = {
    'NBE_MASTER_URL': 'http://10.1.201.99:45000'
}


class Config(object):

    def __getattr__(self, name):
        key = name.upper()
        c = os.environ.get(key, None)
        if c is None:
            click.echo(nbeerror('need %s in os.environ.' % key))
            c = DEFAULT_ENV[key]
        return c


config = Config()
