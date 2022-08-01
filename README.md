# DexCom project installation guidance:

#### install packages listed in requirements.txt file
pip install -r requirements.txt

#### To generate simple report run following command:
pytest -v --html=./test.html

#### To run tests in parallel run following command:
pytest -n 2
