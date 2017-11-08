# Chapter 9 – Organizing Files

> Q: 1. What is the difference between `shutil.copy()` and `shutil.copytree()`?

`shutil.copy()` copies the file, `shutil.copytree()` copies the directory.

> Q: 2. What function is used to rename files?

`shutil.move()`

> Q: 3. What is the difference between the delete functions in the `send2trash` and `shutil` modules?

`send2trash` will move file to recycle bin, while `shutil` functions will permanently delete files and folders.

> Q: 4. `ZipFile` objects have a `close()` method just like `File` objects’ `close()` method. What `ZipFile` method is equivalent to `File` objects’ `open()` method?

`zipfile.ZipFile()`.