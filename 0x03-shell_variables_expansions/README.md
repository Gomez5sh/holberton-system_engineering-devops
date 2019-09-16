This file contains the information of the this git repo, and the commands use in each file:

1. 0-alias: alias ls="rm *"
2. 1-hello_you: echo "Hello $USER"
3. 2-path: export PATH=$PAHT:/action
4. 3-paths: echo $PATH | tr -s ':' '\n' | wl -l
5. 4-global_variables: env
6. 5-local_variables: printenv | env | set
7. 6-create_local_variable: BETTY=Holberton
8. 7-create_global_variable: export HOLBERTON="Betty"
9. 8-true_knowledge: echo $(($TRUEKNOWLEDGE + 128))
10. 9-divide_and_rule: echo $(($POWER/$DIVIDE))
11. 10-love_exponent_breath: echo $(($BREATH**$LOVE))
12. 11-binary_to_decimal: echo $((2#$BINARY))
13 12-combinations: printf "%b\n" {a..z} {a..z} | grep -v | grep -v "oo"