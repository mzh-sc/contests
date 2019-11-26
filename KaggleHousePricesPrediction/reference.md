# Python
python -m unittest discover -v -s ./tests -p *_test.py


# CONDA

## Environment
* conda env create --file environment.yml</br>
* conda remove --name becoming-data-scientist --all</br>
* conda env update --file environment.yml</br>
Note: --prune option doesn't remove unused packages anymore.

## Basic 
* conda search [package] --info

# JUPYTER

jupyter notebook list  
jupyter notebook stop 8888
taskkill /IM jupyter-notebook.exe /F

pip install --editable .

# GIT

git log -p -1 <file name> - to show changes for specific file

## To ignore changes of versioned files 
git update-index --assume-unchanged "main/dontcheckmein.txt"
git update-index --no-assume-unchanged "main/dontcheckmein.txt"