from bluetooth_sensor_state_data import BluetoothServiceInfo
from sensor_state_data import DeviceKey

from okokscale.parser import OKOKScaleBluetoothDeviceData

UNSUPPORTED_SERVICE_INFO = BluetoothServiceInfo(
    name="Not it",
    address="00:00:00:00:00:01",
    rssi=-63,
    manufacturer_data={3234: b"\x00\x01"},
    service_data={},
    service_uuids=[],
    source="local",
)

OKOK_F0_ADDRESS = "50:FB:19:01:23:45"
OKOK_F0_TITLE = "OKOK Scale (2345)"
OKOK_F0_SERVICE_INFO = BluetoothServiceInfo(
    name=OKOK_F0_ADDRESS,
    address=OKOK_F0_ADDRESS,
    rssi=-60,
    manufacturer_data={61695: bytes.fromhex("02045403000000000000000050fb19012345")},
    service_data={},
    service_uuids=[],
    source="local",
)

OKOK_20_ADDRESS = "50:FB:19:67:89:AB"
OKOK_20_TITLE = "OKOK Scale (89AB)"
OKOK_20_SERVICE_INFO = BluetoothServiceInfo(
    name=OKOK_20_ADDRESS,
    address=OKOK_20_ADDRESS,
    rssi=-61,
    manufacturer_data={8394: bytes.fromhex("0b41af2f8101051b14be1770c9ed6737a1a873")},
    service_data={},
    service_uuids=[],
    source="local",
)

OKOK_C0_ADDRESS = "80:F4:16:AB:CD:EF"
OKOK_C0_TITLE = "OKOK Scale (CDEF)"
OKOK_C0_SERVICE_INFO = BluetoothServiceInfo(
    name=OKOK_C0_ADDRESS,
    address=OKOK_C0_ADDRESS,
    rssi=-62,
    manufacturer_data={
        11200: bytes.fromhex("064817700a013180f416abcdef"),
        39104: bytes.fromhex("000017700a013080f416abcdef"),
        42688: bytes.fromhex("000017700a013080f416abcdef"),
        53440: bytes.fromhex("000017700a013080f416abcdef"),
        54720: bytes.fromhex("000017700a013080f416abcdef"),
    },
    service_data={},
    service_uuids=[],
    source="local",
)


def test_can_create():
    OKOKScaleBluetoothDeviceData()


def test_unsupported_service_info() -> None:
    bt_device_data = OKOKScaleBluetoothDeviceData()
    result = bt_device_data.supported(UNSUPPORTED_SERVICE_INFO)
    assert result is False


def test_f0_service_info() -> None:
    bt_device_data = OKOKScaleBluetoothDeviceData()

    result = bt_device_data.supported(OKOK_F0_SERVICE_INFO)
    assert result is True

    sensor_update = bt_device_data.update(OKOK_F0_SERVICE_INFO)

    assert sensor_update.title == OKOK_F0_TITLE
    device = sensor_update.devices[None]
    assert device.name == OKOK_F0_TITLE
    assert device.model == "OKOK Scale"
    assert device.manufacturer == "OKOK"
    assert DeviceKey("mass") in sensor_update.entity_descriptions
    assert DeviceKey("signal_strength") in sensor_update.entity_descriptions

    entity_description = sensor_update.entity_descriptions[DeviceKey("mass")]
    assert entity_description.native_unit_of_measurement == "kg"
    entity_value = sensor_update.entity_values[DeviceKey("mass")]
    assert entity_value.native_value == 85.2

    entity_description = sensor_update.entity_descriptions[DeviceKey("signal_strength")]
    assert entity_description.native_unit_of_measurement == "dBm"
    entity_value = sensor_update.entity_values[DeviceKey("signal_strength")]
    assert entity_value.native_value == -60


def test_20_service_info() -> None:
    bt_device_data = OKOKScaleBluetoothDeviceData()

    result = bt_device_data.supported(OKOK_20_SERVICE_INFO)
    assert result is True

    sensor_update = bt_device_data.update(OKOK_20_SERVICE_INFO)

    assert sensor_update.title == OKOK_20_TITLE
    device = sensor_update.devices[None]
    assert device.name == OKOK_20_TITLE
    assert device.model == "OKOK Scale"
    assert device.manufacturer == "OKOK"
    assert DeviceKey("mass") in sensor_update.entity_descriptions
    assert DeviceKey("signal_strength") in sensor_update.entity_descriptions

    entity_description = sensor_update.entity_descriptions[DeviceKey("mass")]
    assert entity_description.native_unit_of_measurement == "kg"
    entity_value = sensor_update.entity_values[DeviceKey("mass")]
    assert entity_value.native_value == 53.1

    entity_description = sensor_update.entity_descriptions[DeviceKey("signal_strength")]
    assert entity_description.native_unit_of_measurement == "dBm"
    entity_value = sensor_update.entity_values[DeviceKey("signal_strength")]
    assert entity_value.native_value == -61


def test_c0_service_info() -> None:
    bt_device_data = OKOKScaleBluetoothDeviceData()

    result = bt_device_data.supported(OKOK_C0_SERVICE_INFO)
    assert result is True

    sensor_update = bt_device_data.update(OKOK_C0_SERVICE_INFO)

    assert sensor_update.title == OKOK_C0_TITLE
    device = sensor_update.devices[None]
    assert device.name == OKOK_C0_TITLE
    assert device.model == "OKOK Scale"
    assert device.manufacturer == "OKOK"
    assert DeviceKey("mass") in sensor_update.entity_descriptions
    assert DeviceKey("signal_strength") in sensor_update.entity_descriptions

    entity_description = sensor_update.entity_descriptions[DeviceKey("mass")]
    assert entity_description.native_unit_of_measurement == "lb"
    entity_value = sensor_update.entity_values[DeviceKey("mass")]
    assert entity_value.native_value == 160.8

    entity_description = sensor_update.entity_descriptions[DeviceKey("signal_strength")]
    assert entity_description.native_unit_of_measurement == "dBm"
    entity_value = sensor_update.entity_values[DeviceKey("signal_strength")]
    assert entity_value.native_value == -62
