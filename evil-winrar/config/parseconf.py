import configparser

conf = configparser.ConfigParser()

conf["smtp-conf"] = {
    "Personal-email":"",
    "Personal-smtp-passwd":"123",
    "smtp-host":"",
    "smtp-host-port":""
}

conf["http-server"] = {
    "localhost":"",
    "port":"",
    "url_download_path":"/download",
    "download_payload_name":"exp.rar",
    "certfile":"",
    "keyfile":""
}



with open("evil-winrar\config\config.ini","w+") as configfile:
    conf.write(configfile)


