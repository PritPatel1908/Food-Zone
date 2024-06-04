set -o errexit

python3 pip install -r requirements.txt

python3 manage.py collectstatic --no-input
python3 manage.py makemigrations
python3 manage.py migrate