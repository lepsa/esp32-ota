# Tagging versions
Use the following command to tag versions so that there is a simple
lexicographic ordering for versions in the python code, as it is using a simple
string comparison for determining which tag is newer.
`git tag $(date "+%Y-%m-%dT%H%M%S")`

# Pushing Code to the ESP
Commit, tag (as above), and push the code to Github.
Make a new release, using the new tag.
Reboot the ESP.
