# -*- coding:utf-8 -*-
class UrlPathMiddleware(object):
    # 记录用户登录前浏览的页面url
    def process_request(self, request):
        # print request.path
        if request.path not in [
            '/user/login/',
            '/user/register/',
            '/user/login_check/',
            '/user/register_check/',
            '/user/check_user_name/',
            '/user/logout/',
            '/user/islogin/',
        ]:
            request.session['url_path'] = request.get_full_path()
            # print request.session['url_path']


