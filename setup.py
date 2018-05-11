from setuptools import setup, find_packages

setup(
        name = "pysnake",
        author = "Matthijs Tadema",
        packages = find_packages(),
        scripts = ["pysnake/pysnake.py"],
        install_requires = ["pygame"]
        )
