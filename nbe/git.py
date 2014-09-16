# coding: utf-8

from urlparse import urlparse
from pygit2 import Repository


class NBEGitError(Exception):

    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return '<NBEGitError: %s>' % self.msg


class GitUrl(object):

    def __init__(self, url):
        self.url = url
        if url.startswith('git'):
            self._parse_git_url()
        elif url.startswith('http'):
            self._parse_http_url()
        else:
            raise NBEGitError('url must start with git or http(s)')

    def _parse_git_url(self):
        prefix, self.path = self.url.split(':', 1)
        self.scheme, self.netloc = prefix.split('@', 1)
        repo_path = self.path[:-len('.git')]
        self.group, self.name = repo_path.rsplit('/', 1)

    def _parse_http_url(self):
        try:
            ps = urlparse(self.url)
            self.scheme = ps.scheme
            self.netloc = ps.netloc
            self.path = ps.path[1:] # remove first /
            repo_path = self.path[:-len('.git')]
            self.group, self.name = repo_path.rsplit('/', 1)
        except:
            raise NBEGitError('url not validated')

    def __repr__(self):
        attrs = [a for a in self.__dict__ if not a.startswith('_')]
        return '<GitUrl(%s)>' % ', '.join("%s='%s'" % (a, getattr(self, a)) for a in attrs)


class GitRepository(object):

    def __init__(self, path):
        self.path = path
        self.repo = Repository(path)
        self.remotes = {r.name: r for r in self.repo.remotes}

    @property
    def version(self):
        # 7 will be ok
        return self.repo.head.target[:7]

    def __getattr__(self, name):
        if name in self.remotes:
            remote = self.remotes[name]
            return GitUrl(remote.url)
        raise AttributeError('this repo has no remote called %s' % name)
