 
export PYTHONPATH=$PWD 
export FLASK_APP=__init__.py 
export FLASK_DEBUG=1 
. venv/bin/activate 

python -m flask run --host=localhost --port=3000 
