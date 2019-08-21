#git init
git add *
#git config --global user.email "david.feany@gmail.com"
#git config --global user.name "David Feany"
date | xargs -I {} git commit -m "{}"
git push https://github.com/davidfeany/advanced_python_20190819_pyapivz master

