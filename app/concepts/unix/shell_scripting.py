"""Shell Scripting - Writing bash scripts with variables, conditionals, and loops."""

from app.concepts.base import BaseConcept, TryItExample
from app.concepts import register_concept

concept = BaseConcept(
    slug="shell-scripting",
    title="Shell Scripting",
    category="unix",
    difficulty="advanced",
    order=11,
    short_description="Write bash scripts with variables, conditionals, loops, and functions",
    commands=["bash", "if", "for", "while", "case", "function"],
    try_it_examples=[
        TryItExample(
            title="Variables and arithmetic",
            command="x=5; y=3; echo \"Sum: $((x + y)), Product: $((x * y))\"",
            description="Variable assignment and arithmetic expansion"
        ),
        TryItExample(
            title="If statement",
            command="x=10; if [ $x -gt 5 ]; then echo 'x is greater than 5'; else echo 'x is 5 or less'; fi",
            description="Conditional statement with numeric comparison"
        ),
        TryItExample(
            title="For loop",
            command="for i in 1 2 3 4 5; do echo \"Number: $i\"; done",
            description="Iterate over a list of values"
        ),
        TryItExample(
            title="Loop over files",
            command="for f in /etc/*.conf; do echo \"Config: $(basename $f)\"; done 2>/dev/null | head -5",
            description="Iterate over files matching a pattern"
        ),
        TryItExample(
            title="While loop",
            command="i=1; while [ $i -le 3 ]; do echo \"Count: $i\"; i=$((i+1)); done",
            description="Loop while condition is true"
        ),
        TryItExample(
            title="Command substitution",
            command="today=$(date +%Y-%m-%d); echo \"Today is $today\"",
            description="Capture command output in a variable"
        ),
    ],
    gotchas=[
        "No spaces around = in variable assignment (x=5, not x = 5)",
        "Use [[ ]] for modern conditionals (better than [ ])",
        "Always quote variables: \"$var\" prevents word splitting",
        "Use $() for command substitution (backticks are deprecated)",
        "Exit codes: 0 = success, non-zero = failure",
    ],
    related=["environment", "pipes-redirection", "cron-scheduling"],
)

register_concept(concept)
