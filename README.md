# Tagging versions
Use the following command to tag versions so that there is a simple
lexicographic ordering for versions in the python code, as it is using a simple
string comparison for determining which tag is newer.
`git tag $(date "+%Y-%m-%dT%H%M%S")`
