import argparse
import sys
import os

SOURCE_DIR = "/var/log/replacement"
CONF_FILE = sys.path.append(SOURCE_DIR, "replacer.conf")

def get_replace_dict(conf: str, source_dir: str):
    replace_dict = {}
    with open(conf, "r") as f:
        for line in f:
            source_object, dist_path = line.strip().split(":")
            source_object = os.path.join(source_dir, source_object.strip())
            replace_dict[source_object] = dist_path.strip()
    return replace_dict

def main():
    parser = argparse.ArgumentParser(description='Replace file and folders.')
    parser.add_argument('-s', 'source_dir', help='Source directory', default=SOURCE_DIR)
    parser.add_argument('-c', 'conf', help='Configuration file', default=CONF_FILE)
    args = parser.parse_args()
    conf = args.conf
    source_dir = args.source_dir

    # get dict of replacement
    replace_dict = get_replace_dict(conf, source_dir)

    for source_object, dist_path in replace_dict.items():
        # check if source_object exists
        if not os.path.exists(source_object):
            print("Source object {} does not exist.".format(source_object))
            continue

        # check if files exists in dist_path
        if os.path.exists(dist_path):
            # get permission of dist_path
            dist_permission = oct(os.stat(dist_path).st_mode)[-3:]
            # get owner of dist_path
            dist_owner = os.stat(dist_path).st_uid
        else:
            dist_permission = None
            dist_owner = None

        # copy source_object to dist_path
        os.system("cp -r {} {}".format(source_object, dist_path))

        # set permission of dist_path
        if dist_permission:
            os.system("chmod {} {}".format(dist_permission, dist_path))

        # set owner of dist_path
        if dist_owner:
            os.system("chown {} {}".format(dist_owner, dist_path))

if __name__ == '__main__':
    main()