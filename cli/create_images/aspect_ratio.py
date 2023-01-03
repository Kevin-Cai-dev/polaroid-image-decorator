from typing import Tuple


class AspectRatio:
    """Class wrapper representing available aspect ratios"""

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_portrait(self) -> Tuple[int, int]:
        """Get portrait orientation ratio

        Returns:
            Tuple[int, int]: Portrait orientation ratio
        """
        return (min(self.width, self.height), max(self.width, self.height))

    def get_landscape(self) -> Tuple[int, int]:
        """Get landscape orientation ratio

        Returns:
            Tuple[int, int]: Landscape orientation ratio
        """
        return (max(self.width, self.height), min(self.width, self.height))
