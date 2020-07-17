from uuid import UUID, uuid4

_in_memory_storage = dict()


def save(data):
    data_uuid = uuid4()

    _in_memory_storage[data_uuid] = data

    return data_uuid


def get(uuid):
    return _in_memory_storage[UUID(uuid)]
