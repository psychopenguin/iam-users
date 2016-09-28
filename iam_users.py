#!/usr/bin/env python
# -*- coding: utf-8 -*-
import boto3
import sys
import logging
import json
import click
from botocore.exceptions import NoCredentialsError

iam = boto3.client('iam')


def list_users():
    try:
        users = [u['UserName'] for u in iam.list_users()['Users']]
        return users
    except NoCredentialsError:
        logging.error('Unable to locate credentials')
        sys.exit(1)


def get_user_keys(u):
    keys = [k['AccessKeyId']
            for k in iam.list_access_keys(UserName=u)['AccessKeyMetadata']]
    return keys


def get_all_users_and_keys():
    output = dict((u, get_user_keys(u)) for u in list_users())
    return output


@click.command()
@click.option('--pretty', is_flag=True, default=False,
              help="easier for humans read")
@click.option('--filename', type=click.File('w'),
              help="Save output to a file instead of stdout")
def generate_output(pretty, filename):
    all_users = get_all_users_and_keys()
    if pretty:
        output = json.dumps(all_users, indent=4)
    else:
        output = json.dumps(all_users)
    if not filename:
        print(output)
    else:
        filename.write(output)


if __name__ == '__main__':
    generate_output()
