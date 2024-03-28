import streamlit as st


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
        self.cache[key] = value
        self.key_capacity.append(key)

        if len(self.cache) > self.size:
            del_key = self.key_capacity.pop(0)
            del self.cache[del_key]

    def get(self, key):
        return self.cache.get(key)


@st.cache_resource()
def new_lru_cache(size):
    return LocalCacheLRU(size)
