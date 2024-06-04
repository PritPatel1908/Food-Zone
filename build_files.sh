set -o errexit

python3 -m pip install -r requirements.txt

python3 -m manage.py collectstatic --no-input
python manage.py makemigrations
python manage.py migrate