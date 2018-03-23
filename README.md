# Cylon
> Python object that allows you to access **next()** and **prev()** items from a list.

![Python version][python-version]
[![GitHub issues][issues-image]][issues-url]
[![GitHub forks][fork-image]][fork-url]
[![GitHub Stars][stars-image]][stars-url]
[![License][license-image]][license-url]

Why Cylon? Well it was either that or KITT and Cylon just sounded cooler! For those of you not old enough, both Cylons and KITT had a light that moved left to right, just like you can access the items in this object.

## How to set it all up
Clone the project to your computer. Assuming you have a *Projects* folder:

```bash
cd Projects
git clone https://github.com/clamytoe/Cylon.git
cd Cylon
pip install -e .
```

## How to use
For now, just put the script into your project folder and import it:

```bash
from cylon import Cylon

models = [
    'U-87 Cyber Combat Unit',
    'Civilian Cylon',
    'Cylon War-Era Centurion',
    'Cython',
    'Djerba Centurion',
    'Modern Centurion',
    'Inorganic Humanoids',
    'Cylon Spacecraft',
    'Cylon Hybrids',
    'Humanoid Cylons',
]
cylon_models = Cylon(models)
```

### Accessing current item
```bash
cylon_models.current
```
You can also print the current item by simply printing the object:
```bash
print(cylon_models)
```

### Accessing next item
```bash
cylon_models.next()
```

### Accessing prev item
```bash
cylon_models.prev()
```

[python-version]:https://img.shields.io/badge/python-3.6.4-brightgreen.svg
[issues-image]:https://img.shields.io/github/issues/clamytoe/Cylon.svg
[issues-url]:https://github.com/clamytoe/Cylon/issues
[fork-image]:https://img.shields.io/github/forks/clamytoe/Cylon.svg
[fork-url]:https://github.com/clamytoe/Cylon/network
[stars-image]:https://img.shields.io/github/stars/clamytoe/Cylon.svg
[stars-url]:https://github.com/clamytoe/Cylon/stargazers
[license-image]:https://img.shields.io/github/license/clamytoe/Cylon.svg
[license-url]:https://github.com/clamytoe/Cylon/blob/master/LICENSE
