def click_Xpath(driver, num, add_accs):
    """Clicks on the element at the given index in the list of elements found by the given XPath.

    Args:
        driver: The WebDriver instance.
        num: The index of the element to click.
        add_accs: The XPath expression to use to find the elements.
    """

    elements = driver.find_elements_by_xpath(add_accs)
    elements[num].click()
