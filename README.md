# rename-files

```pyinstaller --onefile rename_files.py```

```python3 prepare_test.py```

```python3 rename_files.py```



```pip install py2app```

```from setuptools import setup```

```
APP = ['rename_files.py']
DATA_FILES = []
OPTIONS = {'argv_emulation': True}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
```

```python3 setup.py py2app```

