"""List tests."""

from lists import (
    length,
    drop,
    reverse,
    take,
    Link
)

new_list = Link(4, Link(21, Link(43, None)))

def test_length() -> None:
    """Write tests if you want them."""
    assert length(new_list) == 3

def test_drop() -> None: 
    """Write tests if you want them."""
    assert drop(new_list, 2) ==  Link(43, None)

def test_reverse() -> None:
    """Write tests if you want them."""
    assert reverse(new_list) == Link(43, Link(21, Link(4, None)))

def test_take() -> None: 
    """Write tests if you want them."""
    assert take(new_list, 2) == Link(4, Link(21, None))
