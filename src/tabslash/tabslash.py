r"""Test module for slash and no-slash autodoc."""

def foo(a, b, /):
    """Calculate a thing on two arguments, currently the sum."""
    return a + b

def bar(a, /, b, *, c=1):
    """Calculate c * (a ** b), with c defaulting to one.

    `a` is positional-only, `b` is general,
    `c` is keyword-only.

    """
    return c * (a ** b)
