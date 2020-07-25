# Getiing started

```bash
ostap -h
```

Optionally one can specify the list of python files to be executed before appearance of the interactive command prompt:
```bash
ostap ostap a.py b.py c.py d.py
```

The list of optional arguments can include also root-files, in this case the files will be opened and their 
handlers will be available via local list `root_files`
```bash
ostap a.py b.py c.py d.py file1.root file2.root e.py file3.root
```

Also ROOT macros can be specified on the command line:
```bash
ostap a.py b.py c.py d.py file1.root q1.C file2.root q2.C e.py file3.root q4.C
```

The script automatically opens `TCanvas` window (unless `--no-canvas` option is specified) 
with (a little bit modified) LHCb style. It also loads necessary decorators for ROOT classes. 
At last it executes the python scripts and opens root-files, specified as command line arguments.
