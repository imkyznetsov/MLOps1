from setuptools import setup
with open("setup.py") as f:
    setup(setup(f))
class Setup(object):
    def __init__(self, distribution, **kwargs):
        self.distribution = distribution
        self.kwargs = kwargs
    def run(self):
        self.distribution.run_pytest()