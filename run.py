import unittest
import time
# from testcase import test_01_baidu
from common import HTMLTestRunner
from config import report_paths


def run():
    test_dir = './testcase'
    suite = unittest.defaultTestLoader.discover(start_dir=test_dir, pattern='test*.py')
    now = time.strftime('%Y-%m-%d_%H_%M_%S')
    reportname = report_paths + 'TestResult-' + now + '.html'
    with open(reportname, 'wb') as f:
        runner = HTMLTestRunner.HTMLTestRunner(
            stream=f,
            title='测试报告',
            description='执行人： Jin'
        )
        runner.run(suite)
    f.close()


if __name__ == '__main__':
    run()
