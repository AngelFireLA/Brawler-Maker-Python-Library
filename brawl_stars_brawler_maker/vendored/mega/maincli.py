import argparse
import os

from mega import Mega

def maincli():
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--direct',
                        action='store_true',
                        dest='noTempFile',
                        help='Do not write to a temp file (write directly to output file)')
    parser.add_argument('downloadUrl', nargs=1)
    parser.add_argument('destinationDirectory', nargs='?', default=os.path.realpath(''))
    args = parser.parse_args()
    m = Mega().login()
    m.download_url(url=args.downloadUrl[0], dest_path=args.destinationDirectory, no_temp_file=args.noTempFile)


if __name__ == '__main__':
    maincli()