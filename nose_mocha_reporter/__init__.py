# -*- coding: utf-8 -*-
import re
import time

from nose.plugins import Plugin


class Colors:
    GREEN = '\033[92m'
    DARK = '\033[90m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'


def colored(text, color):
    return color + text + Colors.ENDC



class MochaReporterPlugin(Plugin):
    """Mocha reporter for nose"""

    name = "mocha-reporter"

    def __init__(self):
        super(MochaReporterPlugin, self).__init__()
        self._files = []
        self._suites = []
        self._current = None
        self._started = None

    def setOutputStream(self, stream):
        """Get handle on output stream.
        XXX: Should disable default output of Nose.
        """
        self.stream = stream

    def beforeTest(self, test):
        """Parse the test name and track elapsed time.
        """
        testname = test.test.id()
        parts = testname.split('.')
        test_suite, test_method = parts[-2:]
        test_file = ' '.join(parts[2:-2])

        if test_file not in self._files:
            self._files.append(test_file)
            test_file = self.beautify_file(test_file)
            self.stream.write("\b \n" + test_file + "\n")

        if test_suite not in self._suites:
            self._suites.append(test_suite)
            test_suite = self.beautify_suite(test_suite)
            self.stream.write("\b \n   " + test_suite + "\n")

        spec = test.test.shortDescription()
        if not spec:
            spec = self.beautify_method(test_method)

        self._current = spec
        self._started = time.time()

    def addSuccess(self, test):
        self.showTestResult(u"\u2713", Colors.GREEN)

    def addError(self, test, err):
        self.showTestResult(u"\u2717", Colors.YELLOW)

    def addFailure(self, test, err):
        self.showTestResult(u"\u2717", Colors.RED)

    def showTestResult(self, symbol, color):
        """Output the test result with its name.
        """
        spec = colored(self._current, Colors.DARK)
        duration = (time.time() - self._started) * 1000
        elapsed = ""
        if duration > 10:
            elapsed = "(%dms)" % duration

        if duration > 50:
            elapsed = colored(elapsed, Colors.RED)
        elif duration > 10:
            elapsed = colored(elapsed, Colors.YELLOW)

        msg = u"{mark} {spec} {elapsed}\n".format(mark=colored(symbol, color),
                                                  spec=spec,
                                                  elapsed=elapsed)
        self.stream.write("\b      " + msg)

    def beautify_file(self, test_file):
        groupname = test_file.replace('test_', '').replace('_', ' ')
        return colored(groupname.upper(), Colors.BOLD)

    def beautify_suite(self, test_suite):
        test_suite = test_suite.replace("Test", "")
        words = re.sub("([a-z])([A-Z])","\g<1> \g<2>", test_suite)
        return words.capitalize()

    def beautify_method(self, method):
        sentence = method.replace('test_', '').replace('_', ' ')
        return sentence.capitalize()
