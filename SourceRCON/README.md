# Source RCON Protocol Implementation

A single file implementation of the Source RCON protocol as a library.

## Classes

### RCONPacket

This implementation counts a class for RCON packets. It accepts an id (`id`), a numeric type (`typ`) and a body (`body`).
It can also be called with a bytes object.

```python
''' Default constructor '''
RCONPacket(id:int, typ:int, body:str)

''' Make an instance from a protocol compliant bytearray '''
RCONPacket.fromBytes(data:bytearray)
```

It possess the following methods :
```python
''' Sets the packet's body '''
RCONPacket.setBody(body:str)

''' Returns the class instance data in protocol compliant bytearray '''
RCONPacket.toBytes()
```

The different properties of the packet can be accessed like so :
```python
RCONPacket.id
RCONPacket.typ
RCONPacket.body
```

## RCONClient

For a simple client, the `RCONClient` class can be used.
```python
''' Default constructor '''
RCONClient(host:str, port:int)
```

### Usage

First, authenticate the connection.
```python
RCONClient.auth(password:str)
```

To validate the authentication, call the `isAuthenticated()` method :
```python
RCONClient.isAuthenticated()
```
Authentication does not validate if the server mismatches IDs.

To send a command to the RCON server, use the `exec` method :
```python
RCONClient.exec(cmd:str)
```
This method will raise an exception if the connection is not authenticated or if the server mismatches IDs.

To close the connection, simply delete the instance :
```python
del RCONClient
```

