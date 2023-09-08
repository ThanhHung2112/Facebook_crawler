from get_user_from_fanpage import GET_USER_FFANPAGE
from login_fb import Login
import time

if __name__ == '__main__':

    g = GET_USER_FFANPAGE()
    g.login()
    g.get_user_links()
    # g.browser.close()
    
