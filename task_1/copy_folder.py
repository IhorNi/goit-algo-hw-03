import os
import shutil
import argparse


def copy_files(source_dir, dest_dir, current_dir=''):
    for item in os.listdir(os.path.join(source_dir, current_dir)):
        try:
            item_path = os.path.join(source_dir, current_dir, item)

            if os.path.isfile(item_path):
                ext = os.path.splitext(item)[1]
                ext_dest_dir = os.path.join(dest_dir, ext.strip('.'))
                os.makedirs(ext_dest_dir, exist_ok=True)
                shutil.copy2(item_path, ext_dest_dir)

            elif os.path.isdir(item_path):
                copy_files(source_dir, dest_dir, os.path.join(current_dir, item))

        except PermissionError:
            print(f"Permission denied: Unable to access '{item_path}'")
        except FileNotFoundError:
            print(f"File not found: '{item_path}'")
        except NotADirectoryError:
            print(f"Expected directory but found file: '{ext_dest_dir}'")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--source_dir', required=True, help='Source directory')
    parser.add_argument('--dest_dir', default='dist', help='Destination directory')
    args = parser.parse_args()

    if not os.path.isdir(args.source_dir):
        print(f"SourceDirectoryNotFoundError: Source directory '{args.source_dir}' does not exist.")
        return

    print(f"Copying files from {args.source_dir} to {args.dest_dir}")

    os.makedirs(args.dest_dir, exist_ok=True)

    copy_files(args.source_dir, args.dest_dir)


if __name__ == "__main__":
    main()
