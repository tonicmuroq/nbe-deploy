# coding: utf-8

import os
import yaml
import click

from .actions import (add_app, register_app, list_app, remove_app,
        test_app, build_image, deploy_app, update_app)
from .git import GitRepository
from .utils import nbeinfo
from collections import OrderedDict

@click.group()
def nbecommands():
    pass

@nbecommands.command()
@click.argument('appname')
@click.argument('runtime')
def create(appname, runtime):
    appyaml = OrderedDict({
        'appname': appname, \
        'runtime': runtime, \
        'cmd': [
            'python -c "print \'Hello World\'"',
        ], \
        'services': [
            'python -c "print \'Hello World\'"',
        ], \
        'build': [
            'python -c "print \'Hello World\'"',
        ], \
        'test': [
            'python -c "print \'Hello World\'"',
        ], \
        'static': '', \
    })
    yaml.safe_dump(appyaml, open('app.yaml', 'w'), default_flow_style=False)

@nbecommands.command()
@click.argument('host')
@click.option('--version', '-v', default='latest')
@click.option('--daemon', '-d', default='false')
def add(host, version, daemon):
    r = GitRepository(os.path.abspath('.'))
    name = r.origin.name

    if version == 'latest':
        version = r.version

    click.echo(nbeinfo('add %s @ %s to %s' % (name, version, host)))
    add_app(name, version, host, daemon)


@nbecommands.command()
@click.argument('host')
@click.option('--version', '-v', default='latest')
@click.option('--daemon', '-d', default='false')
def deploy(host, version, daemon):
    r = GitRepository(os.path.abspath('.'))
    name = r.origin.name

    if version == 'latest':
        version = r.version

    click.echo(nbeinfo('add %s @ %s to %s' % (name, version, host)))
    deploy_app(name, version, host, daemon)


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
    if version == 'latest':
        version = r.version

    remove_app(name, version, host)
    click.echo(nbeinfo('%s @ %s removed from %s' % (name, version, host)))


@nbecommands.command()
@click.argument('host')
@click.option('--version', '-v', default='latest')
def test(host, version):
    r = GitRepository(os.path.abspath('.'))
    name = r.origin.name
    if version == 'latest':
        version = r.version

    test_app(name, version, host)
    click.echo(nbeinfo('test %s @ %s on %s' % (name, version, host)))


@nbecommands.command()
@click.argument('host')
@click.argument('base')
@click.option('--version', '-v', default='latest')
def build(host, base, version):
    r = GitRepository(os.path.abspath('.'))
    name = r.origin.name
    if version == 'latest':
        version = r.version

    build_image(name, version, r.origin.group, base, host)
    click.echo(nbeinfo('build %s @ %s on %s' % (name, version, host)))


@nbecommands.command()
@click.argument('host')
@click.option('--fv', '-f')
@click.option('--tv', '-t', default='latest')
def update(host, fv, tv):
    r = GitRepository(os.path.abspath('.'))
    name = r.origin.name
    if tv == 'latest':
        tv = r.version

    update_app(name, fv, tv, host)
    click.echo(nbeinfo('update %s @ %s on %s to %s' % (name, fv, host, tv)))
