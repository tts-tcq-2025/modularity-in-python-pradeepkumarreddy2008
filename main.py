
"""Main module for 25-pair color code application."""

from test_color_functions import run_all_tests
from color_formatter import print_color_reference_manual


if __name__ == '__main__':
    # Run all tests
    run_all_tests()

    # Print the color reference manual
    print("\n" + "=" * 50)
    print("GENERATING COLOR REFERENCE MANUAL")
    print("=" * 50)
    print_color_reference_manual()

    print('\nDone :)')
