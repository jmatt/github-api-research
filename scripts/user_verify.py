#!/usr/bin/env python
import argparse
import getpass
import sys

import libsaas

from gar import auth


class PasswordPromptAction(argparse.Action):
    def __init__(self,
                 option_strings,
                 dest=None,
                 nargs=0,
                 default=None,
                 required=False,
                 type=None,
                 metavar=None,
                 help=None):
        super(PasswordPromptAction, self).__init__(
            option_strings=option_strings,
            dest=dest,
            nargs=nargs,
            default=default,
            required=required,
            metavar=metavar,
            type=type,
            help=help)

    def __call__(self, parser, args, values, option_string=None):
        password = getpass.getpass()
        setattr(args, self.dest, password)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--user', required=True,
                        help='Github user to verify.')
    parser.add_argument('-p', '--password', required=False,
                        action=PasswordPromptAction, type=str,
                        help='Github user password.')
    parser.add_argument('-k', '--key', required=False,
                        help='Public key registered to Github.')
    parser.add_argument('-r', '--repo', required=True,
                        help='Repository to verify.')
    args = parser.parse_args()
    if not args.key and not args.password:
        print("Either a password or public key is required.")
        sys.exit(2)
    if args.key:
        print("Key authorized? => %s" %
              str(auth.verify_key(args.user, args.key)))
        print("Unable to verify repo, not implemented.")
    else:
        print("User authorized? => %s" %
              str(auth.verify_user(args.user, args.password)))
        print("Push permissions to repo? => %s" %
              str(auth.verify_repo(args.user,
                                   args.password,
                                   args.repo)))


if __name__ == '__main__':
    main()
