# -*- coding: utf-8 -*-
#
# Copyright (c) 2022, Jose Antonio Maestre
# All rights reserved.
#
from connect.eaas.extension import (
    Extension,
    ProcessingResponse,
)

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class EmailServiceExtension(Extension):
    @staticmethod
    def get_param_by_id(request_params, id):
        for param in request_params:
            if param.get('id') == id:
                return param
                
    def process_asset_purchase_request(self, request):
        #Add an entry to the log
        self.logger.info(f"Obtained request with id {request['id']}")
        #Get the value for Email parameter
        # dest_email_param = self.get_param_by_id(request['asset']['params'], 'Email')
        #Check if the parameter was empty or not found
        # if dest_email_param:
        #     dest_email = dest_email_param['value']
        #     self.logger.info(f"The Email in the request is " + dest_email)
        # else:
        #     self.logger.error("I was not able to find the Email parameter, skipping process")
        #     return ProcessingResponse.done()
        #Test email config
        dest_email = "joseant.maestre@gmail.com"
        #Start mail processing
        mail_from = self.config['MAILFROM']
        mail_subject = self.config['MAILSUBJECT']
        mail_html = self.config['HTMLBODY']
        smtp_host = self.config['SMTPHOST']
        username = self.config['USERNAME']
        password = self.config['PASSWORD']
        mimemsg = MIMEMultipart()
        mimemsg['From']=mail_from
        mimemsg['To']=dest_email
        mimemsg['Subject']=mail_subject
        mimemsg.attach(MIMEText(mail_html, 'html'))
        connection = smtplib.SMTP(host=smtp_host, port=587)
        connection.starttls()
        connection.login(username,password)
        connection.send_message(mimemsg)
        connection.quit()

        return ProcessingResponse.done()
