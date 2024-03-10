from .DTBaseDataIngress import DTBaseDataIngress
import configparser
import pkg_resources

class SendData:
    def __init__(self):
        self.ruta_archivo_config = pkg_resources.resource_filename(__name__, '../../ConfigFiles/DTBaseConfig.ini')
        self.USER_EMAIL = None
        self.USER_PASS = None
        self.getUserPass()
        self.ingresser = DTBaseDataIngress()

    def getUserPass(self):
        config = configparser.ConfigParser()
        config.read(self.ruta_archivo_config)
        self.USER_EMAIL = config.get('DTBase', 'USER_NAME')
        self.USER_PASS = config.get('DTBase', 'PASSWORD')

    def postData(self,data):
        self.ingresser(data=data, dt_user_email=self.USER_EMAIL, dt_user_password=self.USER_PASS)