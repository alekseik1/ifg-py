import os


def dump_to_csv(filepath, data):
    """
    Dumps `data` to csv under `filepath`. Creates all necessary folders
    :param filepath: Path to file, like 'data/1.csv'
    :param data: Data to dump
    :return:
    """
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    import pandas as pd
    df = pd.DataFrame(data)
    df.to_csv(filepath, index=False, sep=';')