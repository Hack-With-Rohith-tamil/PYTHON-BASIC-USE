""" AVOID USING THIRD PARTIES TO DOWNLOAD YOUTUBE VIDEO , BUILD YOUR OWN SCRIPT TO DO THAT
                      --> BY HACK WITH ROHIT TAMIL"""

from pytube import YouTube
import pyfiglet
 
text = pyfiglet.figlet_format("Hack With Rohith")
print(text)

link = input("Enter the url to download : ")
path = input("Enter the path to download the file : ")
ob = YouTube(link)

print("Title : ",ob.title)
print("Author : ",ob.author)
print("Channel URL : ",ob.channel_url)
print("Channel ID: ",ob.channel_id)
print("Video ID : ",ob.video_id)
print("Rating : ",ob.rating)
print("Views : ",ob.views)
print("len : ",ob.length)
print("Description :",ob.description)
print("Age_Restriction(T/F) : ",ob.age_restricted)
print("Thumbnail : ",ob.thumbnail_url)
print("Captions: ",ob.captions)

stream = ob.streams.filter(progressive=True).get_highest_resolution()
print("Downloading @@@@@@")
stream.download(output_path=path)
print("Downloaded Successfully !!!")
