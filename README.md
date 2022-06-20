# faker-geoscience
Fake data generators for everything Earth (and beyond!)

`faker-geoscience` is a Community Provider for the Python [faker](https://github.com/joke2k/faker) package, intended to provide generators for data relating to the Earth sciences.

## Install

    pip install faker-geoscience

## Use

Base `faker` does not currently support locale resolution for dynamically linked providers, therefore
locale-specific Provider classes have to be linked explicitly using `Faker.add_provider()`,
or the containing module has to be passed to the Faker constructor (examples below).

    from faker import Faker
    from faker_geoscience import flora
    
    # Example 1: Using Faker.add_provider()
    f = Faker()
    f.add_provider(flora.el_GR.Provider)
    
    # Example 2: Passing to constructor
    f = Faker(locale='el-GR', providers=['flora'])
    
    # Module generators available - may be called
    f.plant_name()

## Build

    python3 -m build

## Test

    tox

## Contribute

`faker-geoscience` is in early development - we accept any and all relevant contributions! Check out 
[base faker's contributing guidelines](https://github.com/joke2k/faker/blob/master/CONTRIBUTING.rst)
for further information.

## Acknowledgements

Tox/GitHub Actions configuration strongly influenced by [faker-airtravel](https://github.com/dkotschessa/faker_airtravel) and [faker_wifi_essid](https://github.com/SkypLabs/faker-wifi-essid).
