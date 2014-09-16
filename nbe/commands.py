# coding: utf-8

import os
import click

from .actions import add_app, register_app, list_app, remove_app, test_app, build_image
from .git import GitRepository
from .utils import nbeinfo


@click.group()
def nbecommands():
    pass


@nbecommands.command()
@click.argument('host')
@click.option('--version', '-v', default='latest')
def add(host, version):
    r = GitRepository(os.path.abspath('.'))
    name = r.origin.name

    if version == 'latest':
        version = r.version

    click.echo(nbeinfo('add %s @ %s to %s' % (name, version, host)))
    add_app(name, version, host)


@nbecommands.command()
def register():
    r = GitRepository(os.path.abspath('.'))
    name = r.origin.name
    version = r.version

    click.echo(nbeinfo('register %s @ %s' % (name, version)))
    register_app(name, version)


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
    click.echo(nbeinfo('%s @ %s removed from %s' % (name, version, host)))


@nbecommands.command()
@click.argument('host')
@click.option('--version', '-v', default='latest')
def test(host, version):
    r = GitRepository(os.path.abspath('.'))
    name = r.origin.name
    version = r.version

    test_app(name, version, host)
    click.echo(nbeinfo('test %s @ %s on %s' % (name, version, host)))


@nbecommands.command()
@click.argument('host')
@click.argument('group')
@click.argument('base')
@click.option('--version', '-v', default='latest')
def build(host, group, base, version):
    r = GitRepository(os.path.abspath('.'))
    name = r.origin.name
    version = r.version

    build_image(name, version, host)
    click.echo(nbeinfo('build %s @ %s on %s' % (name, version, host)))
