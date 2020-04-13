# Python
python -m unittest discover -v -s ./tests -p *_test.py


# CONDA

## Environment
* conda info --envs - to list env  
* conda env create --file environment.yml  
* conda remove --name becoming-data-scientist --all  
* conda env update --file environment.yml  
Note: --prune option doesn't remove unused packages anymore.

## Basic 
* conda search [package] --info

# JUPYTER

jupyter notebook list  
jupyter notebook stop 8888
taskkill /IM jupyter-notebook.exe /F

pip install --editable .  

## spell checking
pip install jupyter_contrib_nbextensions
jupyter contrib nbextension install --user
jupyter nbextension enable spellchecker/main
jupyter nbextension list -- to list extensions

# GIT

git pull origin develop - in case of "There is no tracking information for the current branch"
git status -u

git checkout <hash> filename or git reset <hash> filename - to revert changes of specific file

git log -p -1 <file name> - to show changes for specific file
git log -- <file name> - list commits

git diff <commit>

## To ignore changes of versioned files 
git update-index --assume-unchanged "main/dontcheckmein.txt"
git update-index --no-assume-unchanged "main/dontcheckmein.txt"

ls -a - list files in git bash
cd folder

#VS CODE

Ctrl+K Ctrl+I - show method documetation
