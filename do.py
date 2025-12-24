class DoShit:
    def __init__(self,req):
        self.name = "DOSHIT() AND ANOTHER SHIT()"
    async def start(self,when):
        import config
        print(config.conf["URLS"]["clickfix_page"])
        print(f"Hello from do.py from DoShit() {self.name}")
        return "NONE"