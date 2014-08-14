# coding: utf-8

import click


def nbewarn(text):
    return click.style(text, fg='yellow')


def nbeerror(text):
    return click.style(text, fg='red', bold=True)


def nbenormal(text):
    return click.style(text, fg='white')


def nbeinfo(text):
    return click.style(text, fg='green')
