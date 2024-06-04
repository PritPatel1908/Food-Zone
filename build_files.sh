set -o errexit

python3 -m pip install -r requirements.txt

python3 -m manage.py collectstatic --no-input
python3 manage.py makemigrations
python3 manage.py migrate