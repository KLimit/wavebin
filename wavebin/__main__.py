"""
wavebin
https://github.com/sam210723/wavebin

Waveform capture viewer for oscilloscopes.
"""

import appdirs
import argparse
from pathlib import Path
import sys

from wavebin.interface.window import QtApp
from wavebin.interface.plot import QtPlot
from wavebin.wave import WaveParser

__version__ = 2.2


def init():
    print( "                              __    _        ")
    print( "   _      ______ __   _____  / /_  (_)___    ")
    print( "  | | /| / / __ `/ | / / _ \\/ __ \\/ / __ \\")
    print( "  | |/ |/ / /_/ /| |/ /  __/ /_/ / / / / /   ")
    print(f"  |__/|__/\\__,_/ |___/\\___/_.___/_/_/ /_/  v{__version__}\n")
    print( "             vksdr.com/wavebin\n\n")

    # Parse CLI arguments
    args = parse_args()

    # Check for existing configuration file
    config_path = Path(appdirs.user_config_dir("wavebin", "")) / "wavebin.ini"
    if config_path.is_file():
        #TODO: Load config from file
        pass
    else:
        # Create default configuration object
        config = {
            "version": __version__,
            "verbose": args.v,
            "width":   1400,
            "height":  800

    # Create Qt application

    # Create Qt waveform plot
    plot = QtPlot({
        "verbose":     args.v,
        "opengl":      not args.no_opengl,
        "subsampling": limit,
        "filter_type": 0,
        "clipping":    False,
        "colours": [
            (242, 242, 0),
            (100, 149, 237),
            (255, 0, 0),
            (255, 165, 0)
        ]
    })

    # Set class instances
    #wave.instances(app, plot)

    # Add plot to main window

    # Parse file if path specified in argument

    # Run application
    app.run()

    # Gracefully exit application
    safe_exit()


def parse_args() -> argparse.Namespace:
    """
    Parse command-line arguments

    Returns:
        argparse.Namespace: List of arguments
    """

    argp = argparse.ArgumentParser(description="Waveform capture viewer for oscilloscopes")
    argp.prog = "wavebin"

    argp.add_argument("-i", action="store", help="Path to waveform capture file", default=None, dest="file")
    argp.add_argument("-v", action="store_true", help="Enable verbose logging mode")
    argp.add_argument("--no-opengl", action="store_true", help="disable hardware accelerated rendering with OpenGL")
    argp.add_argument("--no-limit", action="store_true", help="disable subsampling limit (may cause slow frame rates with large captures)")

    return argp.parse_args()


def safe_exit(msg=True, code=0) -> None:
    """
    Gracefully exit the application

    Args:
        msg (bool, optional): Print "Exiting..." to the console. Defaults to True.
        code (int, optional): Code to exit with. Defaults to 0.
    """

    if msg: print("Exiting...")
    sys.exit(code)


try:
    init()
except KeyboardInterrupt:
    safe_exit()
