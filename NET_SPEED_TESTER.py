""" DON'T USE THIRD PARTIES TO TEST NETWORK SPEED TEST , THE BELOW SCRIPT DOES FOR YOU
                      --> BY HACK WITH ROHIT TAMIL"""
import speedtest
import pyfiglet

msg = pyfiglet.figlet_format("Hack With Rohit")
print(msg)

test_net = speedtest.Speedtest() # creating an obj of testing wifi
print("Listing the Servers of our network........................")
lists = test_net.get_servers() # List the servers off nearby places
print(f"\n{lists}")
print("\nChoosing the best Server to To test Net Speed.........................")
best_server = test_net.get_best_server()# choosing the best server to test net speed
print(f"\n{best_server}")
ping = test_net.results.ping

download_result = test_net.download()
upload_result = test_net.upload()

print(f"\n Download Speed : {download_result / 1024 / 1024:.2f}mbps/")
print(f"\n Upload Speed : {upload_result / 1024 / 1024:.2f}mbps/")
print(f"\n Ping_Speed : {ping}")