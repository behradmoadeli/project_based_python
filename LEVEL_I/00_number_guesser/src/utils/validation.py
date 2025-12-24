from numpy import round
from src.utils.ui import disp_out_of_range_input, disp_rounded_input, disp_invalid_input


def is_valid(input_str: str) -> bool:
    try:
        val_float = float(input_str)
        if val_float != int(val_float):
            disp_rounded_input()
        val = int(round(val_float, 0))
        if val < 1 or val > 100:
            disp_out_of_range_input()
            return None
        return val
    except (ValueError, OverflowError):
        disp_invalid_input()
        return None


if __name__ == "__main__":
    # Simple test cases
    test_inputs = ["50", "150.0", "25.7", "abc", "-10", "100.9", "100.3", "Inf", "NaN"]
    for inp in test_inputs:
        result = is_valid(inp)
        print(f"Input: {inp} => Validated Value: {result}")
