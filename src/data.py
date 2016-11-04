from time import sleep
from subprocess import Popen as P

from .utils import get_pts_name

# Defaults
DEFAULT_DB = "../data/obdgpslogger.db"

def generate_data( target=DEFAULT_DB, timeout=5*60 ):
    """ Generate random obd data. """

    # Start processes
    simulator = P(["obdsim", "-g", "Cycle"])

    sleep(1)  # Wait for simulator to start
    pts = get_pts_name()

    logger - P(["obdgpslogger", "-s", pts, "-d", target])

    # Wait until timeout
    sleep( timeout )
    simulator.wait()
