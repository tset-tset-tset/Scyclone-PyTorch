from argparse import ArgumentParser, Namespace
from typing import List, Optional


def parseArgments(parser: ArgumentParser, input: Optional[List[str]]) -> Namespace:
    """
    Parse Scyclone-PyTorch arguments
    """

    # path for logging & checkpointing
    parser.add_argument("--dir_root", default="logs", type=str)
    parser.add_argument("--name_exp", default="default", type=str)
    parser.add_argument("--name_version", default="version_-1", type=str)
    # max: from Scyclone poster (check my Scyclone summary blog post)
    parser.add_argument("--max_epochs", default=400000, type=int)
    parser.add_argument("--noiseless_d", action="store_true")
    parser.add_argument("--no_amp", action="store_true")
    # DataLoaderPerformance
    parser.add_argument("--num_workers", default=2, type=int)
    parser.add_argument("--no_pin_memory", action="store_true")
    parser.add_argument("--profiler", action="store_true")

    return parser.parse_args() if input is None else parser.parse_args(input)