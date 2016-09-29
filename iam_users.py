#!/usr/bin/env python
# -*- coding: utf-8 -*-
import boto3
import sys
import logging
import json
import click
from botocore.exceptions import NoCredentialsError, EndpointConnectionError

iam = boto3.client('iam')


def list_users():
    try:
        logging.info('Retrieving users...')
        users = [u['UserName'] for u in iam.list_users()['Users']]
        logging.info('Got {} users: {}'.format(len(users), ', '.join(users)))
        return users
    except NoCredentialsError:
        logging.exception('Unable to locate credentials')
        sys.exit(1)
    except EndpointConnectionError:
        logging.exception('Unable to connect to IAM endpoint')
        sys.exit(1)


def get_user_keys(u):
    logging.info('Retrieving keys for {}'.format(u))
    keys = [k['AccessKeyId']
            for k in iam.list_access_keys(UserName=u)['AccessKeyMetadata']]
    logging.info('Got {} {}'.format(len(keys),
                                    'key' if len(keys) == 1 else 'keys'))
    return keys


def get_all_users_and_keys():
    output = dict((u, get_user_keys(u)) for u in list_users())
    return output


@click.command()
@click.option('-p', '--pretty', is_flag=True, default=False,
              help="easier for humans read")
@click.option('--filename', type=click.File('w'),
              help="Save output to a file instead of stdout")
@click.option('-v', '--verbose', count=True,
              help="Set verbosity level (use twice to increase)")
def generate_output(pretty, filename, verbose):
    if verbose == 1:
        logging.basicConfig(level='INFO')
    elif verbose >= 2:
        logging.basicConfig(level='DEBUG')
    all_users = get_all_users_and_keys()
    if pretty:
        logging.info('Formating output')
        output = json.dumps(all_users, indent=4)
    else:
        output = json.dumps(all_users)
    if not filename:
        logging.info('Sending output to stdout')
        print(output)
    else:
        logging.info('Saving output to {}'.format(filename.name))
        filename.write(output)


if __name__ == '__main__':
    generate_output()
