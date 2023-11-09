from selenium import webdriver

PROXY = "172.30.208.1:4780"

webdriver.Chrome()
webdriver.DesiredCapabilities.CHROME['proxy'] = {
"httpProxy": PROXY,
"ftpProxy": PROXY,
"sslProxy": PROXY,
"proxyType": "MANUAL",

}
cookies = [
        {
            "name":"CSSID",
            "value":"485669413",
            "domain":"connect.mobage.jp"
            },
        {
            "name":"_gcl_au",
            "value":"1.1.1176272094.1697304265",
            "domain":".mobage.jp"
            },
        {
            "name":"CTID_P",
            "value":"6cf10d4899bea11c39836efca85c57239187f364",
            "domain":".mobage.jp"
            },
        {
            "name":"CSID_P",
            "value":"eyJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE2OTczNDU1NzgsImp0aSI6IjQ4NTY2OTQxMyIsIl9leHQiOnsiciI6IjQ4NTY2OTQxMyIsImwiOjAsImlnIjowLCJwIjowLCJpIjo5LCJ1IjoxMDcxODY4OTI5fSwidHlwIjoic2Vzc2lvbiIsImlzcyI6Imh0dHBzOi8vY29ubmVjdC5tb2JhZ2UuanAiLCJleHAiOjE3Mjg4ODE1NzgsInN1YiI6IjE2MzY3MDg1MSJ9.bzIA7t3UHWCbwK6F-ZoCCNcytA90ZMlWmkDEpkdm7S0",
            "domain":".mobage.jp"
            }
        ]



with webdriver.Chrome() as driver:
# Open URL
    driver.get("https://game.granbluefantasy.jp/#raid_multi/33428956337")
    
    for c in cookies:
        driver.add_cookie(c)

    driver.refresh()





