import speedtest
wifi3  = speedtest.Speedtest()
print("Wifi Download Speed is {:.2f} Mpbs".format(wifi3.download()/1000000))
print("Wifi Upload Speed is {:.2f} Mbps".format(wifi3.upload()/1000000))