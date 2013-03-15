# -*- coding:utf-8 -*-


import sys, argparse

#sys.path.insert(1, os.path.dirname(os.path.realpath(__file__)) + os.path.sep + 'subdir')


def parseArguments() :

    parser = argparse.ArgumentParser(description = 'List the programs configured to run automatically on a Windows machine.',
                                     formatter_class = argparse.RawTextHelpFormatter)

    parser.add_argument('MACHINE', help='''Container representing a Windows machine. It can be :\n  - a root directory of a Windows arborescence\n  - a Wolf archive''')
    parser.add_argument('-a', '--all', action='store_true', help='Show all entries')

    args = parser.parse_args()
    return(args)


def main() :

    args = parseArguments()

    print args

    return(0)


if __name__ == '__main__' :
    main()