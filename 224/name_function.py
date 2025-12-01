# Adding New Tests

# Now that we know get_formatted_name() works for simple names again, let’s write a second test for people who include a middle name. We do this by adding another method to the class NamesTestCase:


def get_formatted_name(first, last, middle=''):
    """Generate a neatly formatted full name."""
    if middle:
        full_name = f"{first} {middle} {last}"
    else:
        full_name = f"{first} {last}"
    return full_name.title()

