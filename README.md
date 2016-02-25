# boids

boids is a python 2.7 program that generates an animation of flocking
boids which can be saved as a movie. This program is an implementation
of the Boids model described in the article by Reynolds (1987).

Please refer to
[CITATION](https://github.com/jdfoster/boids/blob/master/CITATION.md)
for information regarding cite this package.

© Joshua D. Foster 2015-2016 under
[MIT License](https://github.com/jdfoster/boids/blob/master/LICENSE.md).

### Installation

Install using pip with:

``` sh
pip install -e git+https://github.com/jdfoster/boids.git#egg=boids
```

Alternatively, this repository can be cloned and then installed with:

``` sh
python setup.py install
```


### Usage

``` sh
boids [--save/-s SAVE] [--config/-c CONFIG] [--generate/-g GENERATE]
```

All switches are optional. In the absence of any switch the program is
use the default configuration.

| Argument  | Description |
| --------- | ----------- |
| SAVE      | Filename for the returned MPEG movie of the generated animation. Given filename needs to have the extension mp4/MP4. Animation is shown in window in the absence of this switch.|
| CONFIG    | Filename for the given configuration file. The given file should in YAML format with the extension yml/YML. This file can be generated using the --save switch. Defaults are used in the absence of this switch. |
| GENERATE  | Filename for a generated configuration file. Generated file is populated with default values. Use without other switches. |


### Examples

Open a window to showing boids animation using the default values:

``` sh
boids
```


Create and save a MP4 movie (boids.mp4) of the boids animation:

``` sh
boids --save boids.mp4
```


Generate a configuration files (conf.yml) populated with the default settings:

``` sh
boids --generate conf.yml
```

Using a modified configuration file (conf.yml) and override the defaults:

``` sh
boids --config conf.yml
```

### Reference
__Reynolds, C.W.__ (1987). Flocks, herds, and schools: a distributed behavioural
model. SIGGRAPH Comput. Graph. 21(4) 25-34.
