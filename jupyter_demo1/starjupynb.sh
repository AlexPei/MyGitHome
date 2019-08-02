echo "start jupyter notebook "
# jupyter notebook > jupyter.log
source /etc/profile

python --version

jupyter notebook --ip="*" --allow-root  --no-browser > jupyter.log &