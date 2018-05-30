from setuptools import setup
import json

with open('package.json') as f:
    package = json.load(f)

package_name = package["name"].replace(" ", "_").replace("-", "_")

setup(
    name=package_name,
    version=package["version"],
    author=package['author'],
    packages=[package_name],
    include_package_package=True,
    license=package['license'],
    description=package['description'] if 'desciption' in package else package_name,
    install_requires=[]
)
