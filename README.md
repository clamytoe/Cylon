# Cylon
> Python object that allows you to access **next()** and **prev()** items from a list.

![Python version][python-version]
[![Build Status][travis-image]][travis-url]
[![BCH compliance][bch-image]][bch-url]
[![GitHub issues][issues-image]][issues-url]
[![GitHub forks][fork-image]][fork-url]
[![GitHub Stars][stars-image]][stars-url]
[![License][license-image]][license-url]

Why **Cylon**? Well it was either that or KITT and Cylon just sounded cooler! For those of you not old enough, both Cylons and KITT had a light that moved left to right, just like you can access the items in this object.

Normal *list()* operations are supported as well.

## How to set it all up
Clone the project to your computer. Assuming you have a *Projects* folder:

```bash
cd Projects
git clone https://github.com/clamytoe/Cylon.git
cd Cylon
python setup.py install
```

## How to use
For now, just put the script into your project folder and import it:

```bash
>>> from cylon import Cylon
>>> models = [
...    'U-87 Cyber Combat Unit',
...    'Civilian Cylon',
...    'Cylon War-Era Centurion',
...    'Cython',
...    'Djerba Centurion',
...    'Modern Centurion',
...    'Inorganic Humanoids',
...    'Cylon Spacecraft',
...    'Cylon Hybrids',
...    'Humanoid Cylons',
...]
>>> cylon_models = Cylon(models)
```

### Accessing current item
```bash
>>> cylon_models.current
'U-87 Cyber Combat Unit'
```
You can also print the current item by simply printing the object:

```bash
>>> print(cylon_models)
U-87 Cyber Combat Unit
```

### Accessing next item
```bash
>>> cylon_models.next
'Civilian Cylon'
```

### Accessing prev item
```bash
>>> cylon_models.prev
'U-87 Cyber Combat Unit'
>>> cylon_models.prev
'Humanoid Cylons'
```

### Accessing nearby neighbors
I was recently made aware that in the world of High Performance Computing (HPC) the concept of neighbors is called a "stencil". So that's what I called it. By default it will show the two items before and after the currently selected item.

```bash
>>> cylon_models.stencil()
['Cylon Hybrids', 'Humanoid Cylons', 'U-87 Cyber Combat Unit', 'Civilian Cylon', 'Cylon War-Era Centurion']
>>> cylon_models.stencil(7)
['Cython', 'Djerba Centurion', 'Modern Centurion', 'Inorganic Humanoids', 'Cylon Spacecraft', 'Cylon Hybrids', 'Humanoid Cylons', 'U-87 Cyber Combat Unit', 'Civilian Cylon', 'Cylon War-Era Centurion', 'Cython', 'Djerba Centurion', 'Modern Centurion', 'Inorganic Humanoids', 'Cylon Spacecraft']
```

### For further features review help()
Here's a snippet of what's available:

```bash
Help on class Cylon in module cylon.cylon:

class Cylon(collections.abc.MutableSequence)
 |  Provides .next() and .prev() methods
 |  
 |  If you need to traverse your list object in either direction,
 |  then this is the module to use.
 |  
 |  Methods defined here:
 |  
 |  stencil(self, count=2)
 |      Return a list with the before and after elements
 |      
 |      Count determines how many of each are displayed.
 |  
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |  
 |  current
 |      Return the current item
 |  
 |  next
 |      Return the next item in the object
 |  
 |  prev
 |      Return the previous item in the object
 |  
 |  show_next
 |      Display the next item without changing current
 |  
 |  show_prev
 |      Display the previous item without changing current
 |  


```

[python-version]:https://img.shields.io/badge/python-3.6.4-brightgreen.svg
[travis-image]:https://travis-ci.org/clamytoe/Cylon.svg?branch=master
[travis-url]:https://travis-ci.org/clamytoe/Cylon
[bch-image]:https://bettercodehub.com/edge/badge/clamytoe/Cylon?branch=master
[bch-url]:https://bettercodehub.com/
[issues-image]:https://img.shields.io/github/issues/clamytoe/Cylon.svg
[issues-url]:https://github.com/clamytoe/Cylon/issues
[fork-image]:https://img.shields.io/github/forks/clamytoe/Cylon.svg
[fork-url]:https://github.com/clamytoe/Cylon/network
[stars-image]:https://img.shields.io/github/stars/clamytoe/Cylon.svg
[stars-url]:https://github.com/clamytoe/Cylon/stargazers
[license-image]:https://img.shields.io/github/license/clamytoe/Cylon.svg
[license-url]:https://github.com/clamytoe/Cylon/blob/master/LICENSE
