import errno
import os
from csv import writer


def dump_to_csv(filepath, data):
    """Dumps `data` to csv under `filepath`. Creates all necessary folders.

    :param filepath: Path to file, like 'data/1.csv'
    :param data: Data to dump
    :return:
    """
    try:
        os.makedirs(os.path.dirname(filepath))
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise
    with open(filepath, "w") as f:
        w = writer(f)
        w.writerow(["temperature", "value"])
        w.writerows(data)
