import pyshark


def load_pcap(file_path: str):
    """Load a pcap file into a pyshark capture object"""
    return pyshark.FileCapture(file_path)


def load_live_capture(interface: str = "eth0", timeout: int = 50):
    """Load a live capture into a pyshark capture object"""
    return pyshark.LiveCapture(interface=interface).sniff(timeout=timeout)
