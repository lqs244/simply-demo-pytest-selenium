from Page_login import Page_login
import pytest
import common
import yaml
import allure


# @pytest.mark.skip
@allure.feature('登录测试')
class Test_login():
    @classmethod
    def setup_class(cls):
        # 打开浏览器和访问网址
        cls.driver = common.open_driver(Page_login.url)

    @staticmethod
    @allure.step('步骤1 ：登录')
    def step_login(driver, dict1):
        common.login(driver, dict1)

    @staticmethod
    @allure.step('步骤2 ：断言')
    def step_assert(driver, dict1):
        if '用户名错误' in dict1['assert']:
            assert common.assert_text_in(driver, Page_login.text_usernameerror, Page_login.xpath_usernameerror)
        if '账号不能为空' in dict1['assert']:
            assert common.assert_text_in(driver, Page_login.text_usernamevoid, Page_login.xpath_usernameerror)
        if '密码错误' in dict1['assert']:
            assert common.assert_text_in(driver, Page_login.text_passwderror, Page_login.xpath_passwderror)
        if '密码不能为空' in dict1['assert']:
            assert common.assert_text_in(driver, Page_login.text_passwdvoid, Page_login.xpath_passwderror)
        if '账号不存在' in dict1['assert']:
            assert common.assert_text_in(driver, Page_login.text_usernamenone, Page_login.xpath_usernameerror)
        if '正确跳转' in dict1['assert']:
            assert common.wait_until_show(driver, Page_login.xpath_newfile)

    @pytest.mark.parametrize('dict1', yaml.safe_load(open('Test_data.yml', encoding='utf8'))['login_data'])
    def test_login(self, dict1):
        Test_login.step_login(self.driver, dict1)
        Test_login.step_assert(self.driver, dict1)

    def teardown(self):
        common.driver_get(self.driver, Page_login.url)

    @classmethod
    def teardown_class(cls):
        common.driver_close(cls.driver)
