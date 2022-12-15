from pytest import raises

from bfilter.bloom import BloomFilter


def test_init_valid():
    expected_false_positive_probability: float = 0.04  # Expecting 4%
    items_count: int = 100000000

    bloom_filter: BloomFilter = BloomFilter(
        items_count, expected_false_positive_probability
    )

    assert type(bloom_filter) == BloomFilter


def test_get_bitarray_index():
    expected_false_positive_probability: float = 0.04  # Expecting 4%
    items_count: int = 100000000
    test_item: str = "Coke"

    bloom_filter: BloomFilter = BloomFilter(
        items_count, expected_false_positive_probability
    )

    for test_seed in range(1000):
        bit_array_index: int = bloom_filter._calc_random_bit_array_index(
            test_item, test_seed
        )

        assert bit_array_index >= 0
        assert bit_array_index < bloom_filter._number_of_bits


def test_invalid_bloom_filter_items_count_configuration():
    expected_false_positive_probability: float = 0.04  # Expecting 4%
    invalid_items_count: int = -100000000

    with raises(ValueError, match="Items count should be bigger then 0."):
        bloom_filter: BloomFilter = BloomFilter(
            invalid_items_count, expected_false_positive_probability
        )


def test_invalid_bloom_filter_false_positive_probability_configuration():
    expected_false_positive_probability: float = 1.02  # Expecting 4%
    invalid_items_count: int = 100000000

    with raises(
        ValueError,
        match="False positive probability should be higher than 0 and less than 1.",
    ):
        bloom_filter: BloomFilter = BloomFilter(
            invalid_items_count, expected_false_positive_probability
        )


def test_bloom_filter_insert():
    expected_false_positive_probability: float = 0.04  # Expecting 4%
    items_count: int = 100000000
    test_item: str = "Coke"

    bloom_filter: BloomFilter = BloomFilter(
        items_count, expected_false_positive_probability
    )

    assert bloom_filter.insert(test_item)


def test_bloom_filter_could_not_insert():
    expected_false_positive_probability: float = 0.04  # Expecting 4%
    items_count: int = 30
    test_item: str = "Coke"

    bloom_filter: BloomFilter = BloomFilter(
        items_count, expected_false_positive_probability
    )

    for _ in range(items_count):
        assert bloom_filter.insert(test_item)

    assert not bloom_filter.insert(test_item)
