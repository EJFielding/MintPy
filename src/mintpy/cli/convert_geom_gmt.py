#!/usr/bin/env python3
############################################################
# Program is part of MintPy                                #
# Copyright (c) 2013, Zhang Yunjun, Heresh Fattahi         #
# Author: Antonio Valentino, Heresh Fattahi, Aug 2022      #
#  modified from save_gmt.py Eric Fielding Jan. 2023       #
############################################################


import sys

from mintpy.utils.arg_utils import create_argument_parser

####################################################################################
EXAMPLE = """example:
  convert_geom_gmt.py  geo_geometryRadar.h5
  convert_geom_gmt.py  geo/geo_geometryRadar.h5
"""


def create_parser(subparsers=None):
    synopsis = 'Convert geocoded geometry LOS angles to East, North, Up, and write to GMT grd files'
    epilog = EXAMPLE
    name = __name__.split('.')[-1]
    parser = create_argument_parser(
        name, synopsis=synopsis, description=synopsis, epilog=epilog, subparsers=subparsers)

    parser.add_argument('file', help='geometry file to be converted, in geo coordinate.')
    parser.add_argument('-o', '--output', dest='outfile',
                        help='output file base name. Extension is fixed with .grd')
    return parser


def cmd_line_parse(iargs=None):
    # parse
    parser = create_parser()
    inps = parser.parse_args(args=iargs)

    # import
    from mintpy.utils import readfile

    # check
    atr = readfile.read_attribute(inps.file)

    # check: input file coordinate system
    if 'Y_FIRST' not in atr.keys():
        raise Exception('ERROR: input file is not geocoded.')

    # check: dset for certain file types (timeseries and ifgramStack)
    ftype = atr['FILE_TYPE']
   
    return inps


####################################################################################
def main(iargs=None):
    # parse
    inps = cmd_line_parse(iargs)

    # import
    from mintpy.convert_geom_gmt import convert_geom_gmt

    # run
    convert_geom_gmt(inps)


####################################################################################
if __name__ == '__main__':
    main(sys.argv[1:])
