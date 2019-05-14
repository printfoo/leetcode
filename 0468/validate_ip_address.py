"""
Solution for Validate IP Address.

Idea:
Directly checking.
"""

# Solution.
class Solution:
    def validIPAddress(self, IP: str) -> str:
        if "." in IP:
            IP = IP.split(".")
            if len(IP) != 4: return "Neither"
            for ip in IP:
                if len(ip) == 0 or (ip[0] == "0" and ip != "0") or not ip.isnumeric() or int(ip) > 255: return "Neither"
            return "IPv4"
        if ":" in IP:
            IP = IP.split(":")
            if len(IP) != 8: return "Neither"
            for ip in IP:
                if len(ip) > 4 or len(ip) == 0 or any(c not in "0123456789abcdefABCDEF" for c in ip): return "Neither"
            return "IPv6"
        return "Neither"

# Main.
if __name__ == "__main__":
    IP = "192.0.0.1"
    print(Solution().validIPAddress(IP))
