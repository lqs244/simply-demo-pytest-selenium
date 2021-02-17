import yaml


class Page_login():
    __yaml_data = yaml.safe_load(open('Page_data.yml', encoding='utf-8'))
    # 字符串
    url = __yaml_data['Page_login']['url']
    # 一个字典
    __xpaths = __yaml_data['Page_login_xpaths']

    # xpath from here

    xpath_usernameinput = __xpaths['xpath_user_textbox']
    xpath_usernameerror = __xpaths['xpath_user_error']

    xpath_passwdinput = __xpaths['xpath_passwd_textbox']
    xpath_passwderror = __xpaths['xpath_passwd_error']

    xpath_loginbutton = __xpaths['xpath_login_button']

    xpath_newfile = __xpaths['xpath_newfile']

    __show_text = __yaml_data['show_text']
    text_usernameerror = __show_text['text_assert_usernameerror']
    text_passwderror = __show_text['text_assert_passwderror']
    text_usernamevoid = __show_text['text_assert_usernamevoid']
    text_passwdvoid = __show_text['text_assert_passwdvoid']
    text_usernamenone = __show_text['text_assert_usernamenone']


class Page_garbage():
    __yaml_data = yaml.safe_load(open('Page_data.yml', encoding='utf-8'))
    newxpaths = __yaml_data['Page_new_xpath']
