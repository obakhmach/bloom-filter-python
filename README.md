# Bloom Filter
Simple bloom filter implementation in Python.


## Install
To install a python library just execute one of the following command.

```bash
pip install git+https://github.com/alexanderbakhmach/bloom-filter-python.git@{branch_name}
```

```bash
pip install git+https://github.com/alexanderbakhmach/bloom-filter-python.git@{commit_hash}
```

```bash
pip install git+https://github.com/alexanderbakhmach/bloom-filter-python.git@{tag}
```

For example

```bash
pip install git+https://github.com/alexanderbakhmach/bloom-filter-python.git@0.1.0
```

## Usage

To initialize bloom filter use the example below.


```python
from bfilter.bloom import BloomFilter

bloom_filter: BloomFilter = BloomFilter(
    items_count, expected_false_positive_probability
)
```

In order to insert item into the bloom filter.


```python
bloom_filter.insert(test_item)
```

To check whether the item in bloom filter or not.


```python
bloom_filter(test_absent_item)
# Or
bloom_filter.is_probably_present(test_item)
```