from Page_login import Page_login
from Page_login import Page_garbage
import pytest
import common
import yaml


# @pytest.mark.skip
class Test_creat_del():
    @classmethod
    def setup_class(cls):
        cls.driver = common.open_driver(Page_login.url)
        common.login(cls.driver, yaml.safe_load(open('Test_data.yml', encoding='utf8'))['creat_garbage'])
        # 等待dialog页面弹出然后关闭他
        common.click(common.wait_until_show(cls.driver, Page_garbage.newxpaths['xpath_close_dialog']))

    @classmethod
    def teardown_class(cls):
        cls.driver.close()

    def setup(self):
        # 前往我的文件
        self.driver.get(Page_garbage.newxpaths['url_my'])

    def ready_test_del(self):
        # 前往回收站
        self.driver.get(Page_garbage.newxpaths['url_g'])
        # 在回收站查看文件数量
        try:
            # 出现异常意味着没找到元素,此时count为0
            self.count_of_g = len(
                common.s_wait_until_show(driver=self.driver, xpath=Page_garbage.newxpaths['xpath_file_listitems'],
                                         sec=2))
        except:
            self.count_of_g = 0
        # 在主页,查找并点击新建文件按钮
        common.click(common.wait_until_show(self.driver, Page_garbage.newxpaths['xpath_new_button']))
        # 在主页,获取所有新建文件的种类
        eles = common.s_wait_until_show(self.driver, Page_garbage.newxpaths['xpaths_new'])
        return eles

    # @pytest.mark.parametrize('str_',Page_garbage.newxpaths['text_to_des'])
    @pytest.mark.parametrize('str_', ['流程图', 'BPMN'])
    def test_del(self, str_):
        eles = self.ready_test_del()
        for i in range(0, len(eles)):
            # 如果新建菜单不可见,就点击一次新建按钮
            if common.is_show(self.driver, Page_garbage.newxpaths['xpath_menu_new']):
                ele = common.wait_until_show(self.driver, Page_garbage.newxpaths['xpath_new_button'])
                common.click(ele)
            if eles[i].text == str_:
                common.click(eles[i])
                common.wait_until(driver=self.driver,
                                  method=lambda a: True if (self.driver.title != 'ProcessOn - 我的文件') else False)
                # 为了系统有时间保存这一次作品
                common.sleep(2)
                # 返回我的文件
                self.driver.get(Page_garbage.newxpaths['url_my'])
                # 删除第一个文件
                common.context_click(driver=self.driver, ele=
                common.s_wait_until_show(driver=self.driver, xpath=Page_garbage.newxpaths['xpath_file_listitems'])[0])
                eles = common.s_wait_until_show(driver=self.driver,
                                                xpath=Page_garbage.newxpaths['xpath_menu_context_click'])
                for i in range(0, len(eles)):
                    if '删除' in eles[i].text:
                        common.click(eles[i])
                        common.click(common.wait_until_show(self.driver, Page_garbage.newxpaths['xpath_del_ok']))
                        break
                # 前往回收站
                self.driver.get(Page_garbage.newxpaths['url_g'])

                # 断言回收站里面的文件数量是不是上一个加1
                try:
                    # 出现异常意味着没找到元素,此时count为0
                    count_now = len(common.s_wait_until_show(driver=self.driver,
                                                             xpath=Page_garbage.newxpaths['xpath_file_listitems'],
                                                             sec=2))
                except:
                    count_now = 0
                assert count_now == self.count_of_g + 1
                break
