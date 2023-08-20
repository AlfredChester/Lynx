#include <bits/stdc++.h>

#define AC    0
#define WA    1
#define ERROR -1

int spj(FILE *input, FILE *user_output);

void close_file(FILE *f) {
    if (f != NULL) {
        fclose(f);
    }
}

int main(int argc, const char *args[]) {
    FILE *input = NULL, *user_output = NULL;
    int result;
    if (argc != 3) {
        printf("Usage: spj x.in x.out\n");
        return ERROR;
    }
    input       = fopen(args[1], "r");
    user_output = fopen(args[2], "r");
    if (input == NULL || user_output == NULL) {
        printf("Failed to open output file\n");
        close_file(input);
        close_file(user_output);
        return ERROR;
    }

    result = spj(input, user_output);
    printf("result: %d\n", result);

    close_file(input);
    close_file(user_output);
    return result;
}

using namespace std;

int spj(FILE *input, FILE *user_output) {
    /*
      parameter:
        - input，The FILE pointer of input file
        - user_output，The FILE pointer of user's output
      return:
        - If the answer is correct, return AC
        - If the answer is wrong, return WA
        - If you actively capture your own errors,
          such as memory allocation failure, return ERROR
      Please complete the function on your own.
      demo:
      int a, b;
      while(fscanf(user_output, "%d %d", &a, &b) != EOF){
          if(a - b != 3){
              return WA;
          }
      }
      return AC;
    */
    return AC;
}