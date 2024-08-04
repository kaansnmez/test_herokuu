import os
def main():
  desired_order_list=["type","project_id","private_key_id","private_key","client_email","client_id","auth_uri","token_uri",
                        "auth_provider_x509_cert_url","client_x509_cert_url","universe_domain"]
  service_dict={}
  
  for key,value in os.environ.items():
      if (key!='api_key') & (key!='api_secret'):
          service_dict[key]=value
  
  SERVICE_ACCOUNT_FILE = {k: service_dict[k] for k in desired_order_list}
  print(SERVICE_ACCOUNT_FILE)
if __name__=='__main__':
    main()
