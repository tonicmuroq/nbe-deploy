# coding: utf-8

import click
import json
import requests
import yaml
from urlparse import urljoin

from .utils import nbeerror, nbeinfo
from .config import config


def yaml_to_json(filename):
    try:
        with open(filename, 'r') as f:
            return json.dumps(yaml.load(f))
    except IOError:
        click.echo(nbeerror('file %s not exist.' % filename))
        return ''


def register_app(name, version):
    app_yaml = yaml_to_json('app.yaml')
    config_yaml = yaml_to_json('config.yaml')
    if not app_yaml:
        return

    data = {
        'appyaml': app_yaml,
        'configyaml': config_yaml,
    }
    url = urljoin(config.nbe_master_url,
            '/app/{name}/{version}'.format(name=name, version=version))
    r = requests.post(url, data=data)
    click.echo(nbeinfo('request sent to %s' % url))
    click.echo(nbeinfo(str(r.json())))
    return r.status_code == 200


def add_app(name, version, host, daemon):
    data = {
        'host': host,
        'daemon': daemon,
    }
    url = urljoin(config.nbe_master_url,
        'app/{name}/{version}/add'.format(name=name, version=version))
    r = requests.post(url, data)
    click.echo(nbeinfo('request sent to %s' % url))
    click.echo(nbeinfo(str(r.json())))
    return r.status_code == 200


def list_app(name, version='latest'):
    r = requests.get(urljoin(config.nbe_master_url,
        'app/{name}/{version}'.format(name=name, version=version)))
    if r.status_code == 200:
        rs = json.loads(r.content)
        if not rs['r']:
            click.echo(nbeinfo(rs['name']))
            click.echo(nbeinfo(rs['version']))
        else:
            click.echo(nbeerror(rs['msg']))
    else:
        click.echo(nbeerror('Error: %s' % r.status_code))


def remove_app(name, version, host):
    data = {
        'host': host
    }
    url = urljoin(config.nbe_master_url,
        'app/{name}/{version}/remove'.format(name=name, version=version))
    r = requests.post(url, data)
    click.echo(nbeinfo('request sent to %s' % url))
    click.echo(nbeinfo(str(r.json())))
    return r.status_code == 200


def test_app(name, version, host):
    data = {
        'host': host
    }
    url = urljoin(config.nbe_master_url,
        'app/{name}/{version}/test'.format(name=name, version=version))
    r = requests.post(url, data)
    click.echo(nbeinfo('request sent to %s' % url))
    click.echo(nbeinfo(str(r.json())))
    return r.status_code == 200


def build_image(name, version, group, base, host):
    data = {
        'host': host,
        'group': group,
        'base': base,
    }
    url = urljoin(config.nbe_master_url,
        'app/{name}/{version}/build'.format(name=name, version=version))
    r = requests.post(url, data)
    click.echo(nbeinfo('request sent to %s' % url))
    click.echo(nbeinfo(str(r.json())))
    return r.status_code == 200


def deploy_app(name, version, host, daemon):
    data = {
        'hosts': host,
        'daemon': daemon,
    }
    url = urljoin(config.nbe_master_url,
        'app/{name}/{version}/deploy'.format(name=name, version=version))
    r = requests.post(url, data)
    click.echo(nbeinfo('request sent to %s' % url))
    click.echo(nbeinfo(str(r.json())))
    return r.status_code == 200
