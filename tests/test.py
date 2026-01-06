from .. import *


html = Html()


main_page = html.getTemplateFixedHtml()
second_page = html.getTemplateFixedHtml(fileOrder=2)

ps = PowerShell()

dropper = ps.getPowershellCode()


server_start_command = getUvicornRunCommand()

ServerStartUp()

