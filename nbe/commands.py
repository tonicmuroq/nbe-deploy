# coding: utf-8

import os
import click

from .actions import add_app, register_app, list_app, remove_app
from .git import GitRepository
from .utils import nbeinfo


@click.group()
def nbecommands():
    pass


@nbecommands.command()
@click.argument('host')
@click.option('--version', '-v', default='latest',
        help='version of app, default to latest')
def add(host, version):
    r = GitRepository(os.path.abspath('.'))
    name = r.origin.name

    if version == 'latest':
        version = r.version

    add_app(name, version, host)
    click.echo(nbeinfo('app %s:%s added to %s' % (name, version, host)))


@nbecommands.command()
def register():
    r = GitRepository(os.path.abspath('.'))
    name = r.origin.name
    version = r.version

    click.echo(nbeinfo('register %s @ %s' % (name, version)))
    register_app(name, version)
    click.echo(nbeinfo('app %s:%s registered' % (name, version)))


@nbecommands.command()
@click.option('--version', '-v', default='latest')
def list(version):
    r = GitRepository(os.path.abspath('.'))
    name = r.origin.name
    
    if version == 'latest':
        version = r.version

    list_app(name, version)


@nbecommands.command()
@click.argument('host')
@click.option('--version', '-v', default='latest')
def remove(host, version):
    r = GitRepository(os.path.abspath('.'))
    name = r.origin.name
    version = r.version

    remove_app(name, version, host)
    click.echo(nbeinfo('app %s:%s removed from %s' % (name, version, host)))
