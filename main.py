import config
import argparse
from src import Assembly


def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('--env', type=str, choices=['default', 'dev', 'prod'], help='environment')
    return parser.parse_args()


if __name__ == '__main__':
    args = get_arguments()
    conf = config.get_config(args.env)
    assembly = Assembly(conf)
    assembly.start()
