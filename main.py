#!/$HOME/SSP_Automation/venv/bin/python3

import pytest
import os

if __name__ == "__main__":
    choice = "y"
    while choice == "y":
        # -s disables output capturing, allowing Pytest to read input properly.
        pytest.main(["-s", "tests/", "--html=reports/test_report.html"])
        
        os.system("wmctrl -a Terminal")
        choice = input("\nWould you like to run another test? (Y/n)").strip().lower()
        if not choice:
            choice = "y"
        
    

