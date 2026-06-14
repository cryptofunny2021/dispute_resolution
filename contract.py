# v0.2.16
# { "Depends": "py-genlayer:1jb45aa8ynh2a9c9xn3b7qqh8sm5q93hwfp7jqmwsfhh8jpz09h6" }

from genlayer import *

class DisputeResolution(gl.Contract):

    disputes: TreeMap[Address, str]

    def __init__(self):
        pass

    @gl.public.write
    def submit_dispute(self, dispute: str) -> None:
        user = gl.message.sender_address
        self.disputes[user] = dispute

    @gl.public.view
    def my_dispute(self) -> str:
        user = gl.message.sender_address
        return self.disputes.get(user, "")
