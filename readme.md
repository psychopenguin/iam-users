# Credentials

To run this script you should set the following environment properly or provide other credencial setup as required by boto3 library - http://boto3.readthedocs.io/en/latest/guide/configuration.html

```
AWS_ACCESS_KEY_ID=<ACCESS_KEY>
AWS_SECRET_ACCESS_KEY=<SECRET_ACCESS_KEY>
```

# Run

You need python3 to run this script. It's recommended to use a virtualenv (virtualenvwrapper #FTW).

`python -m virtualenv --python=$(which python3) venv`

`source venv/bin/activate`

`pip install -r requirements.txt`

`python iam-users.py`
