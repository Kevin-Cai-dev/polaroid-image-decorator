from typing import Tuple


class JPEGImageData:
    """
    Class wrapper storing JPEG image metadata. Currently stores 3 fields:
    - dpi
    - exif
    - icc_profile
    """

    def __init__(self, dpi: Tuple, exif: bytes, icc_profile):
        self.dpi = dpi
        self.exif = exif
        self.icc_profile = icc_profile

    def get_dpi(self) -> Tuple[int, int]:
        """Returns image dpi

        Returns:
            Tuple[int, int]: image dpi
        """
        return self.dpi

    def get_exif(self) -> bytes:
        """Returns image exif information

        Returns:
            bytes: image exif
        """
        return self.exif

    def get_icc_profile(self) -> bytes:
        """Returns image icc_profile

        Returns:
            bytes: image icc_profile
        """
        return self.icc_profile
