# Credentials

To run this script you should set the following environment properly or provide other credencial setup as required by boto3 library - http://boto3.readthedocs.io/en/latest/guide/configuration.html

```
AWS_ACCESS_KEY_ID=<ACCESS_KEY>
AWS_SECRET_ACCESS_KEY=<SECRET_ACCESS_KEY>
```

# Setup

You need python3 to run this script. It's recommended to use a virtualenv (virtualenvwrapper #FTW).

`python -m virtualenv --python=$(which python3) venv`

`source venv/bin/activate`

`pip install -r requirements.txt`

# Usage

`python iam-users.py --help`

```
Usage: iam_users.py [OPTIONS]

Options:
  --pretty             easier for humans read
  --filename FILENAME  Save output to a file instead of stdout
  --help               Show this message and exit.
```
