"""
71. Simplify Path

Given a string path, which is an absolute path (starting with a slash '/') to a file or directory in a Unix-style file system, convert it to the simplified canonical path.

In a Unix-style file system, a period '.' refers to the current directory, a double period '..' refers to the directory up a level, and any multiple consecutive slashes (i.e. '//') are treated as a single slash '/'. For this problem, any other format of periods such as '...' are treated as file/directory names.

The canonical path should have the following format:

The path starts with a single slash '/'.
Any two directories are separated by a single slash '/'.
The path does not end with a trailing '/'.
The path only contains the directories on the path from the root directory to the target file or directory
(i.e., no period '.' or double period '..')
Return the simplified canonical path.


Example 1:
Input: path = "/home/"
Output: "/home"
Explanation: Note that there is no trailing slash after the last directory name.

Example 2:
Input: path = "/../"
Output: "/"
Explanation: Going one level up from the root directory is a no-op, as the root level is the highest level you can go.

Example 3:
Input: path = "/home//foo/"
Output: "/home/foo"
Explanation: In the canonical path, multiple consecutive slashes are replaced by a single one.

Constraints:

- 1 <= path.length <= 3000
- path consists of English letters, digits, period '.', slash '/' or '_'.
- path is a valid absolute Unix path.
"""


def simplifyPath(path: str) -> str:
    """Runtime 52ms, Memory 13.9MB"""
    # Split path by / and remove all the empty string
    filtered_path = list(filter(None, path.split("/")))

    # We are going to use stack to trace
    stack = []
    absolute_path = "/"
    for path in filtered_path:
        # .. refers to its parent directory
        if path == "..":
            # Nothing will happen from root
            if len(stack) == 0:
                continue
            # If it is not root, we remove the recently added path as that will be the cur_directory after applying ..
            else:
                stack.pop()
        # . means current directory, so no action needed
        elif path == ".":
            continue
        # everything else is a valid directory (as constraint says its valid path)
        else:
            stack.append(path)

    # Now, we just need to add step by step from the beginning
    for path in stack:
        absolute_path += path + "/"

    return absolute_path[:-1] if len(absolute_path) > 1 else absolute_path


print(simplifyPath("/home/"))
print(simplifyPath("../"))
print(simplifyPath("/home//foo/"))
print(simplifyPath("/a/./b/../../c/"))
