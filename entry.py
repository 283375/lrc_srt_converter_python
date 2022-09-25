from convert import lrc2srt, srt2lrc
from codecs import lookup as codec_lookup
from os.path import splitext, isdir, exists, abspath
from sys import exit
import argparse

parser = argparse.ArgumentParser(description='lrc2srt converter.')
parser.add_argument('files', nargs='+')
parser.add_argument('-o', '--output-dir',
                    help='output file destination, e.g. X:/Music/lyrics')
parser.add_argument('-lenc', '--lrc-encoding',  default='utf-8',
                    help='lrc file encoding, e.g. utf-8, gbk, shiftjis, ...')
parser.add_argument('-senc', '--srt-encoding',  default='utf-8',
                    help='srt file encoding, e.g. utf-8, gbk, shiftjis, ...')

if __name__ == '__main__':
    args = parser.parse_args()
    try:
        codec_lookup(args.lrc_encoding)
    except LookupError:
        print('Unknown encoding "%s" for lrc, please check your input.' %
              args.srt_encoding)
        exit(3)
    try:
        codec_lookup(args.srt_encoding)
    except LookupError:
        print('Unknown encoding "%s" for srt, please check your input.' %
              args.srt_encoding)
        exit(3)

    if args.output_dir:
        if isdir(args.output_dir) and exists(args.output_dir):
            args.output_dir = abspath(args.output_dir)
        else:
            print('Invalid output directory "%s". Exitting.' % args.output_dir)
            exit(1)

    for file in args.files:
        try:
            if splitext(file)[1] == '.srt':
                srt2lrc(
                    srt_path=file,
                    lrc_path=args.output_dir,
                    lrc_encoding=args.lrc_encoding,
                    srt_encoding=args.srt_encoding)
            else:
                lrc2srt(
                    lrc_path=file,
                    srt_path=args.output_dir,
                    lrc_encoding=args.lrc_encoding,
                    srt_encoding=args.srt_encoding)
        except Exception as e:
            print(f'Error [{str(e)}] occured while processing "{file}".')
