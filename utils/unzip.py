import argparse
import os
import zipfile


def __main__():
    parser = argparse.ArgumentParser(prog='unzip archive')
    parser.add_argument('archive', help='Path to file')
    parser.add_argument('dest_dir',
                        help='Destination folder',
                        nargs='?',
                        default='.')
    args = parser.parse_args()

    file_full_path = os.path.abspath(args.archive)
    folder_name = os.path.splitext(os.path.basename(file_full_path))[0]
    dest_dir = os.path.abspath(os.path.join(args.dest_dir, folder_name))

    with zipfile.ZipFile(file_full_path, 'r') as zf:
        zf.extractall(dest_dir)


if __name__ == '__main__':
    __main__()
