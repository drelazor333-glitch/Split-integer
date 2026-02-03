from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    """Test that sum of all parts equals the original value"""
    assert sum(split_integer(8, 1)) == 8
    assert sum(split_integer(6, 2)) == 6
    assert sum(split_integer(17, 4)) == 17
    assert sum(split_integer(32, 6)) == 32
    assert sum(split_integer(100, 13)) == 100
    assert sum(split_integer(50, 7)) == 50
    assert sum(split_integer(1, 10)) == 1
    assert sum(split_integer(3, 5)) == 3

    assert len(split_integer(17, 4)) == 4
    assert len(split_integer(32, 6)) == 6


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    """Test that value divisible by parts returns all equal elements"""
    result1 = split_integer(6, 2)
    assert result1 == [3, 3]
    assert all(x == 3 for x in result1)
    assert len(set(result1)) == 1

    result2 = split_integer(9, 3)
    assert result2 == [3, 3, 3]
    assert all(x == 3 for x in result2)

    result3 = split_integer(20, 4)
    assert result3 == [5, 5, 5, 5]
    assert min(result3) == max(result3)

    result4 = split_integer(100, 10)
    assert result4 == [10] * 10

    result5 = split_integer(12, 3)
    assert result5 == [4, 4, 4]
    assert result5[0] == 4
    assert result5[-1] == 4


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    """Test that splitting into 1 part returns the original value"""
    assert split_integer(8, 1) == [8]
    assert split_integer(100, 1) == [100]
    assert split_integer(1, 1) == [1]
    assert split_integer(42, 1) == [42]
    assert split_integer(999, 1) == [999]


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    """Test that result array is sorted ascending when parts are not equal"""
    result1 = split_integer(17, 4)
    assert result1 == [4, 4, 4, 5]
    # Проверяем строгую сортировку
    assert result1 == sorted(result1)

    result2 = split_integer(32, 6)
    assert result2 == [5, 5, 5, 5, 6, 6]
    assert result2.count(5) == 4
    assert result2.count(6) == 2

    result3 = split_integer(10, 3)
    assert result3 == [3, 3, 4]

    result4 = split_integer(7, 3)
    assert result4 == [2, 2, 3]
    assert sum(result4) == 7

    result5 = split_integer(11, 4)
    assert result5 == [2, 3, 3, 3]
    assert result5[0] == 2
    assert result5[1:] == [3, 3, 3]

    for value, parts in [(17, 4), (32, 6), (10, 3), (7, 3), (11, 4)]:
        result = split_integer(value, parts)
        assert max(result) - min(result) <= 1
        assert result == sorted(result)


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    """Test when value is less than number of parts, zeros should be added"""
    result1 = split_integer(3, 5)
    assert result1 == [0, 0, 1, 1, 1]
    assert result1[:2] == [0, 0]
    assert result1[2:] == [1, 1, 1]

    result2 = split_integer(2, 3)
    assert result2 == [0, 1, 1]
    assert result2[0] == 0

    result3 = split_integer(1, 2)
    assert result3 == [0, 1]

    result4 = split_integer(4, 7)
    assert result4 == [0, 0, 0, 1, 1, 1, 1]
    assert result4.count(0) == 3
    assert result4.count(1) == 4

    result5 = split_integer(2, 5)
    assert result5 == [0, 0, 0, 1, 1]

    result6 = split_integer(5, 5)
    assert result6 == [1, 1, 1, 1, 1]
    assert 0 not in result6

    result7 = split_integer(3, 3)
    assert result7 == [1, 1, 1]

    for value, parts in [(3, 5), (2, 3), (1, 2), (4, 7)]:
        result = split_integer(value, parts)
        assert result == sorted(result)
        assert sum(result) == value