def assert_element_present(element):
    if not element.is_displayed():
        raise AssertionError("Element not presented")

def assert_field_error(element):
    if not element.get_attribute('aria-invalid'):
        raise AssertionError("No attribute @aria-invalid")
