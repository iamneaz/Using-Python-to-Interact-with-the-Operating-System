# Test --> A command that evaluates the conditions received and exits with zero when they're true and with one when they're false

if test -n "$PATH"; then echo "Your path is not empty"; fi # Here -n checks if a string is empty or not
# alternative to the test command is using []. a space needs to be before and after the opening bracket and before the closing bracket
if [ -n "$PATH" ]; then echo "Your path is not empty"; fi