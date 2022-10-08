from modules.base_module import Module

class_name = "Trade"


class Trade(Module):
    prefix = "trd"

    def __init__(self, server):
        self.server = server
        self.commands = {"init": self.init, "of": self.of, "ac": self.accept, "cl": self.close}
        self.trades = {}

    async def init(self, msg, client):
        uid = msg[2]['trid']
        if uid not in self.server.online:
            return
        await client.send(["trd.init", {"trid": uid}])
        await self.server.online[uid].send(["trd.init", {"trid": client.uid}])

    async def of(self, msg, client):
        return

    async def accept(self, msg, client):
        return

    async def close(self, msg, client):
        uid = msg[2]['trid']
        await self.server.online[uid].send(["trd.cl", {"trid": client.uid, "trnm":
            await self.server.redis.lindex(f"uid:{client.uid}:appearance", 0)}])

