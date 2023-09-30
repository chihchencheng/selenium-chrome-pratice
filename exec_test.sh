#!/bin/bash
pytest test_web.py
allure generate allure-results --clean -o allure-report
