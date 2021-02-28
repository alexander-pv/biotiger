import os
from biotiger.common.constants import OUTPUT_DIR, ROOT, OUTPUT_PATH


def make_output_dir():
    """
    Make the default output directory if it doesn't exist
    :return: None
    """
    if OUTPUT_DIR not in os.listdir(ROOT):
        os.mkdir(OUTPUT_PATH)
        print 'Created the default output folder on path: %s' % OUTPUT_PATH
    else:
        print 'The default output folder on path: %s' % OUTPUT_PATH


def write_msg(filename):
    print "File saved: %s" % filename
