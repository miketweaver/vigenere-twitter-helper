#!/usr/bin/python
import sys
import subprocess
from vigenere import encryptMessage
import tweepy

consumer_key = 'your consumer_key'
consumer_secret = 'your consumer_secret'
access_token = 'your access_token'
access_token_secret = 'your access_token_secret'

def createMessage(keyhidden,key,message,attrib):
    return "Key: " + keyhidden + "\\n" + encryptMessage(key, message) + "\\n\\n     - " + attrib;

def easy(key,message,attrib):
	return createMessage(key,key,message,attrib)
	
def medium(key,message,attrib):
	hide = True;
	keyhidden = "";
	for letter in key:
		if hide:
			keyhidden = keyhidden + letter;
			hide = False;
		else:
			keyhidden = keyhidden + "_";
			hide = True;
	return createMessage(keyhidden,key,message,attrib);

def hard(key,message,attrib):
	keyhidden = "";
	for letter in key:
		keyhidden = keyhidden + "_ ";
	return createMessage(keyhidden,key,message,attrib);
	
def variables():
	global message
	global attrib
	global key
	message = raw_input('Enter message: ')
	attrib = raw_input('Enter attribution: ')
	key = raw_input('Enter key [alphanumeric]: ')
	return

def main():

	if len(sys.argv) == 1:
		variables();

		print("Easy Key");
		print("--------");
		print(easy(key,message,attrib));


		print("\nMedium Key");
		print("--------");
		print(medium(key,message,attrib));


		print("\nHard Key");
		print("--------");
		print(hard(key,message,attrib));

	elif sys.argv[1] == "easy":
		variables();
		print(easy(key,message,attrib));
	elif sys.argv[1] == "medium":
		variables();
		print(medium(key,message,attrib));
	elif sys.argv[1] == "hard":
		variables();
		print(hard(key,message,attrib));
	elif sys.argv[1] == "generate":


		auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
		auth.set_access_token(access_token, access_token_secret)
		api = tweepy.API(auth)

		picture = raw_input('Enter background picture name: ')

		print("\nEasy Key");
		print("--------");
		variables();
		subprocess.call(['./imagecreation.sh',easy(key,message,attrib), picture, 'easy.png'])
		api.update_with_media('easy.png', status="Difficulty: Easy");

		print("\nMedium Key");
		print("--------");
		variables();
		subprocess.call(['./imagecreation.sh',medium(key,message,attrib), picture, 'medium.png'])
		api.update_with_media('medium.png', status="Difficulty: Medium");

		print("\nHard Key");
		print("--------");
		variables();
		subprocess.call(['./imagecreation.sh',hard(key,message,attrib), picture, 'hard.png'])
		api.update_with_media('hard.png', status="Difficulty: Hard");


if __name__ == '__main__':
	main()
