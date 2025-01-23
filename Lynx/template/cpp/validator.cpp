/**
 * This validator will be compiled into an executive,
 * and the testcase-tools will provide it with the input
 * file in a way that testlib recognizes.
 *
 * So you can use the built-in io functions in testlib.h
 * to write your validator.
 */
#include "testlib.h"

int main(int argc, char *argv[]) {
    registerValidation(argc, argv);
    return 0;
}
