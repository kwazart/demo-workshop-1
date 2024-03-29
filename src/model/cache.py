import streamlit as st


# todo: хорошо бы добавить блокировки в LocalCacheLRU и использовать их в методах set и get (или хранить в базе)
class LocalCacheLRU(object):
    # создадим кэш с указанным размером
    def __init__(self, size):
        default_size = 128

        if not size:  # если размер не передали, установим дефолтное значение
            size = default_size

        self.size = size
        self.cache = dict()
        self.key_capacity = []

    def set(self, key, value):
        hash_key = hash(key)

        if hash_key not in self.cache:
            self.key_capacity.append(hash_key)

        self.cache[hash_key] = value

        if len(self.cache) > self.size:
            del_key = self.key_capacity.pop(0)
            del self.cache[del_key]

    def get(self, key):
        return self.cache.get(hash(key))


@st.cache_resource()
def new_lru_cache(size):
    return LocalCacheLRU(size)
