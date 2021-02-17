import pytest
import os

if __name__ == '__main__':
    pytest.main(['--alluredir', './tmp'])
    os.system('allure generate ./tmp -o ./report --clean')
