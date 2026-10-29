"""Parser for OKOK scale BLE advertisements."""

import contextlib

from sensor_state_data import SensorDeviceClass, SensorUpdate, Units

from .parser import OKOKScaleBluetoothDeviceData

with contextlib.suppress(ModuleNotFoundError):
    from ._version import __version__ as __version__

__all__ = [
    "OKOKScaleBluetoothDeviceData",
    "SensorDeviceClass",
    "SensorUpdate",
    "Units",
]
