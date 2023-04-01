from main import *

def test_1():
    #expected log in is True with valid user:
    expected = True
    driver = get_driver()
    log_in(driver,"standard_user","secret_sauce")
    actual = check_if_logged_in(driver)
    assert expected == actual
    driver.close()

def test_2():
    #expected log in is True with non valid user:
    expected = False
    driver = get_driver()
    log_in(driver,"locked_out_user","secret_sauce")
    actual = check_if_logged_in(driver)
    assert expected == actual
    driver.close()

def test_3():
    expected = True
    driver = get_driver()
    log_in(driver,"standard_user","secret_sauce")
    add_to_cart(driver)
    go_to_cart(driver)
    check_out(driver)
    fill_details_in_check_out(driver,"standard_user","standard_user",'0000000')
    continue_after_check_out(driver)
    finish_check_out(driver)
    actual = check_if_check_out_successfully_completed(driver)
    assert expected == actual
    driver.close()

def test_4():
    expected = True
    driver = get_driver()
    log_in(driver,"problem_user","secret_sauce")
    add_to_cart(driver)
    go_to_cart(driver)
    check_out(driver)
    fill_details_in_check_out(driver,"problem_user","problem_user",'0000000')#fail here
    continue_after_check_out(driver)
    finish_check_out(driver)
    actual = check_if_check_out_successfully_completed(driver)
    assert expected == actual
    driver.close()