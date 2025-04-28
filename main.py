import pytest 

if __name__ == "__main__":
    # -s disables output capturing, allowing Pytest to read input properly.
    pytest.main(["-s", "tests/", "--html=reports/test_report.html"])

