/**
 * This checker will be compiled into an executive,
 * and the testcase-tools will provide it with the input
 * file and the output file in a way that testlib recognizes.
 *
 * So you can use the built-in io functions in testlib.h
 * to write your checker.
 */
#include "testlib.h"

int main(int argc, char *argv[]) {
    registerTestlibCmd(argc, argv);
    return 0;
}
