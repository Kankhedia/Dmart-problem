import pytest
import os
from dmart1 import Dmart

@pytest.fixture()
def instance():
    dmart = Dmart()
    return dmart

#Test case to check if the file extension is .csv
def test_Extension(instance):
    if instance.data_file.lower().endswith('.csv'):
        print('Successful')

    else:
        assert False

#To Check the .CSV file is empty or not
def test_check(instance):
    file_path=instance.data_file
    if os.stat(file_path).st_size == 0:
        raise Exception("File is empty")
    else:
        print("Proceed")




