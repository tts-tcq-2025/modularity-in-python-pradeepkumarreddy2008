"""Color formatting functions for reference manual."""

from color_constants import MAJOR_COLORS, MINOR_COLORS
from color_converter import get_pair_number_from_color


def format_color_reference_manual():
    """Format color coding as reference manual for printing."""
    manual = "25-Pair Color Code Reference Manual\n"
    manual += "=" * 40 + "\n"
    manual += f"{'Pair Number':<12} | {'Major Color':<12} | " \
              f"{'Minor Color':<12}\n"
    manual += "-" * 40 + "\n"

    for major_color in MAJOR_COLORS:
        for minor_color in MINOR_COLORS:
            pair_number = get_pair_number_from_color(major_color, minor_color)
            manual += f"{pair_number:<12} | {major_color:<12} | " \
                      f"{minor_color:<12}\n"

    return manual


def print_color_reference_manual():
    """Print the color reference manual."""
    print(format_color_reference_manual())
