cd ./test_cases
pytest -s --alluredir ../outfiles/report --clean-alluredir
allure serve ../outfiles/report