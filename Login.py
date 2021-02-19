from operate_file import operate_file

class functions(object):

    def __init__(self):
        self.of = operate_file()

    def login_fun(self):#登录
        login_test_data=self.of.read_test_data("login_test_data.txt")
        login_test_step_data=self.of.read_test_step_data("login_test_step_data.txt")
        self.of.eval_commands(login_test_data,login_test_step_data)

    def create_contact(self):#创建联系人
        create_contact_test_data = self.of.read_test_data("create_contact_test_data.txt")
        create_contact_test_step_data = self.of.read_test_step_data("create_contact_test_step_data.txt")
        self.of.eval_commands(create_contact_test_data, create_contact_test_step_data)

    def send_email(self):#发送邮件
        send_email_test_data=self.of.read_test_data("send_email_test_data.txt")
        send_email_test_step_data=self.of.read_test_step_data("send_email_test_step_data.txt")
        self.of.eval_commands(send_email_test_data,send_email_test_step_data)

if __name__=="__main__":
    fun=functions()
    fun.login_fun()
    fun.create_contact()
    fun.send_email()

