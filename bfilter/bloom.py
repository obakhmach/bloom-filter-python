import logging
import math
from functools import cached_property
from typing import Optional, cast

from bitarray import bitarray
from mmh3 import hash as mhash
from cityhash import CityHash64 as chash


class BloomFilter:
    DEFAULT_FALSE_POSITIVE_PROBABILITY: float = 0.3

    def __init__(
        self, items_count: int, false_positive_probability: Optional[float] = None
    ) -> None:
        """Constructor to init the bloom filter in most simplest form.

        Args:
            items_count: The amount of items planned to store in the bloom filter.
            false_positive_probability: The probability of false positive responses from the
                                        bloom filter.
        """
        if items_count <= 0:
            raise ValueError("Items count should be bigger then 0.")

        self._items_added: int = 0
        self._items_count: int = items_count
        self._false_positive_probability: float
        self._buffer: bitarray

        if false_positive_probability is None:
            self._false_positive_probability = self.DEFAULT_FALSE_POSITIVE_PROBABILITY

        elif false_positive_probability >= 1 or false_positive_probability <= 0:
            raise ValueError(
                "False positive probability should be higher than 0 and less than 1."
            )

        else:
            self._false_positive_probability = false_positive_probability

        # Because _number_of_bits is getter and it's value could be calculated ones
        # the _false_positive_probability and _items_count where set.
        self._buffer = bitarray(self._number_of_bits)

    @cached_property
    def _number_of_bits(self) -> int:
        """A getter to calculate and receive the optimal
        number of bits in the bloom filter bit array based on
        desired _false_positive_probability and _items_count.

        Returns:
            The number of bits for bloom filter bit array.
        """
        return int(
            -(self._items_count * math.log(self._false_positive_probability, math.e))
            / math.log(2, math.e) ** 2
        )

    @cached_property
    def _number_of_hashes(self) -> int:
        """Calculates the best number of hash functions used
        to store the desired amount of items (_items_count).

        Returns:
            The best number of hash
        """
        return int(-math.log2(self._false_positive_probability))

    def _calc_random_bit_array_index(self, item: str, seed: int) -> int:
        """Calculates the bit to set in a bit array for a given item.
        This calculation per seed simulates the behavior
        of using unique hash function per a unique seed.

        Args:
            item: An item we want to remember in the bloom filter.
            seed: Any integer number.

        Returns:
            An index in bit array.
        """
        murmur_hash: int = mhash(item)
        city_hash: int = chash(item)

        aka_random_hash: int = murmur_hash + seed * city_hash

        return aka_random_hash % self._number_of_bits
