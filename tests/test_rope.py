import pytest
import numpy as np

from rope import rope

def test_start_setter_bad():
    rope1 = rope()
    with pytest.raises(ValueError):
        rope1.start = [1]

def test_start_setter():
    rope1 = rope()
    rope1.start = [-1, -1]
    expected = np.array([1, 1])
    assert np.array_equal(rope1.start, expected)

def test_end_setter():
    rope1 = rope()
    with pytest.raises(ValueError):
        rope1.end = [1]

def test_theta_setter():
    pass

def test_length_setter():
    my_rope = rope()
    with pytest.raises(AttributeError):
        my_rope.length = 0

def test_swing():
    start1 = (250, 0)
    distance = 100
    theta1 = np.pi/4
    my_rope = rope(length=distance, theta=theta1, start=start1)
    new_theta = np.pi / 3
    my_rope.theta = new_theta
    x = 300
    y = 86.60254037844386
    expected = np.array([x, y])
    assert np.array_equal(my_rope.end, np.array([my_rope.start[0], distance]))
    my_rope.swing()
    new_distance = np.sqrt(np.power((my_rope.end[0] - my_rope.start[0]), 2) + np.power((my_rope.end[1] - my_rope.start[1]), 2))
    assert np.array_equal(my_rope.end, expected)
    assert new_distance == 100
