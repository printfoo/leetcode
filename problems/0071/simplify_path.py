"""
Solution for Simplify Path, Time O(n).

Idea:
Stack.
"""

# solution
class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split("/")
        simplified_path = []
        for p in path:
            if not p or p == ".":
                continue
            elif p == "..":
                if simplified_path:
                    simplified_path.pop()
            else:
                simplified_path.append(p)
        return "/" + "/".join(simplified_path)

# Main.
if __name__ == "__main__":
    path = "/a//b////c/d//././/.."
    print(Solution().simplifyPath(path))
