# coding: utf-8

import click

from .actions import add_app, register_app
from .utils import nbeinfo


@click.group()
def nbecommands():
    pass


@nbecommands.command()
@click.argument('name')
@click.argument('host')
@click.option('--version', '-v', default='latest',
        help='version of app, default to latest')
def add(name, version, host):
    add_app(name, version, host)
    click.echo(nbeinfo('app %s:%s added to %s' % (name, version, host)))


@nbecommands.command()
@click.argument('name')
@click.argument('version')
def register(name, version):
    # TODO 这里不需要拿version应该
    # 看看gitlab有没有对应的API
    # 另外可能这里应该指定代码分支
    register_app(name, version)
    click.echo(nbeinfo('app %s:%s registered' % (name, version)))
