## Animals
A template Python project structure, using animals as an example :lion:

# A simple structure for one script

animal/
    rhino.py
    .gitignore
    README.md   
    LICENCE
    requirements.txt
    setup.py
    tests.py

# A structure for a package

animals/
    animals/
        __init__.py
        rhino.py
        helpers.py
    tests/
        rhino_tests.py
        helpers_tests.py
.gitignore
README.md   
LICENCE
requirements.txt
setup.py
Makefile

# A structure for multiple packages

animals/
    __init__.py
    rhino/
        rhino.py
        helpers.py
    tiger/
        tiger.py
        helpers.py
tests/
    rhino
        rhino_tests.py
        helpers_tests.py
    tiger
        tiger_tests.py
        helpers_tests.py
.gitignore
README.md   
LICENCE
requirements.txt
setup.py

# Structure of a complex application with multiple packages

animals/
    animals/
        __init__.py
        land/
            __init__.py
            rhino/
                __init__.py
                rhino.py
                rhino_tests.py
            tiger/
            __init__.py
                tiger.py
                tiger_tests.py
        water/
            __init__.py
            shark.py
            shark_tests.py
    tests/
        land/
            rhino/
                rhino_tests.py
                helpers_tests.py
            tiger/
                tiger_tests.py
                helpers_tests.py
        water/
            shark/
                shark_tests.py
                helpers_tests.py
    docs/
        land.md
        water.md
    .gitignore
    README.md
    LICENCE
    requirements.txt
    setup.py
    