from hstest.stage_test import StageTest
from hstest.test_case import TestCase
from hstest.check_result import CheckResult

CheckResult.correct = lambda: CheckResult(True, '')
CheckResult.wrong = lambda feedback: CheckResult(False, feedback)


class Zookeeper(StageTest):
    def generate(self):
        return [TestCase(attach=
                         ["i love animals",
                          "let's check on the animals",
                          "the deer looks fine",
                          "the bat looks happy",
                          "the lion looks healthy"])]

    def check(self, reply, attach):
        reply = reply.replace('’', "'").strip().lower()
        reply = list(filter(None, reply.splitlines()))
        if len(reply) != 5:
            return CheckResult.wrong("Your program should print 5 lines")
        for j, (answer_line, reply_line) in enumerate(zip(attach, reply)):
            if answer_line not in reply_line:
                return CheckResult.wrong("Your output should be like in the example!\n"
                                         f"The '{answer_line.capitalize()}' string should be on the line {j+1}")
        return CheckResult.correct()


if __name__ == '__main__':
    Zookeeper('zookeeper.zookeeper').run_tests()
