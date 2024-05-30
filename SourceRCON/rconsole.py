import socket
import time

class RCONPacket:
    id = 0
    typ = 0
    body = ""
    def __init__(self, id:int, typ:int, body:str):
        self.id = id
        self.typ = typ
        self.body = body
    @classmethod
    def fromBytes(self, data:bytearray):
        size = int.frombytes(data[0:4])
        self.id = int.frombytes(data[4:8])
        self.typ = int.frombytes(data[8:12])
        self.body = data[12:size + 4].decode('utf-8').rstrip('\x00')
        return self
    @classmethod
    def toBytes(self):
        size = len(self.body) + 10
        data = bytearray()
        data.append(size.to_bytes(length=4, byteorder='little', signed=True))
        data.append(self.id.to_bytes(length=4, byteorder='little', signed=True))
        data.append(self.typ.to_bytes(length=4, byteorder='little', signed=True))
        data.append(self.body.encode('utf-8'))
        data.append(b'\x00\x00')
        return data

class RCONClient:
    _conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    _authenticated = False
    def __init__(self, host:str, port:int):
        self._conn.connect((host, port))
        self.authenticated = False
    @classmethod
    def auth(self, password:str):
        auth_pack = RCONPacket(1, 3, password)
        self._conn.sendall(auth_pack.toBytes())
        data = self._conn.recv(4096)
        while not data:
            time.sleep(1)
            data = self._conn.recv(4096)
        resp = RCONPacket.fromBytes(bytearray(data))
        self._authenticated = (resp.id == auth_pack.id)
    @classmethod
    def exec(self, cmd:str):
        if not self._authenticated:
            raise Exception("Connection Not Authenticated")
        exec_pack = RCONPacket(2, 2, cmd)
        self._conn.sendall(exec_pack.toBytes())
        data = self._conn.recv(4096)
        while not data:
            time.sleep(1)
            data = self._conn.recv(4096)
        resp = RCONPacket.fromBytes(bytearry(data))
        if (resp.id != exec_pack.id):
            raise Exception("Server Responded with Inconsistent ID")
        return resp.body
    @classmethod
    def isAuthenticated(self):
        return _authenticated
    @classmethod
    def __del__(self):
        self._conn.close()
        del authenticated

