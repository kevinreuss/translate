#!usr/bin/python

import os
import speech_recognition as sr
from textblob import TextBlob

# global #
translation_to = "en"
my_language = "de"

def listen():
	r = sr.Recognizer()
	with sr.Microphone() as source:
		audio = r.listen(source)
	try:
		command = r.recognize_google(audio, language = "de")
	except sr.UnknownValueError:
		command = ""
	os.system("cls")
	return command

def speak(text_to_speak, language = my_language):
	os.system('C:\eSpeak\command_line\espeak -p 70 -v ' + language +  ' "' + text_to_speak + '"')

def translate(message_detected):
	message_to_translate = TextBlob(message_detected)
	message_to_translate.correct()
	message = message_to_translate

	try:
		message = message_to_translate.translate(to = translation_to)
	except:
		pass

	message_to_write = ""
	for word in message.words:
		message_to_write = message_to_write + word + " "
	write_to_file(message_to_write)

def write_to_file(message_to_write):
	path = os.getcwd()
	path = path + "/../data/german"
	file_write = open(path, "r+")
	file_write.write(message_to_write)
	file_write.close()

def read_from_file():
	path = os.getcwd()
	path = path + "/../data/english"
	file_read = open(path, "r+")
	message_to_read = ""
	for line in file_read:
		message_to_read = line
	file_read.close()
	return message_to_read

def clean_files():
	path = os.getcwd()
	path = path + "/../data/english"
	file_to_clean = open(path, "r+")
	file_to_clean.truncate()
	file_to_clean.close()
	path = os.getcwd()
	path = path + "/../data/german"
	file_to_clean = open(path, "r+")
	file_to_clean.truncate()
	file_to_clean.close()

def __main__():
	first = True
	clean_files()
	while True:
		if first == False:
			os.system("cls")
			input(">>> ")
			# listening #
			os.system("cls")
			print("< listening >")
			message_detected = ""
			while message_detected == "":
				message_detected = listen()
			# translate #
			translate(message_detected)
		first = False
		# reading #
		os.system("cls")
		print("< reading >")
		message_read = ""
		while message_read == "":
			message_read = read_from_file()
		# speak #
		clean_files()
		speak(message_read)

if __name__ == "__main__":
	__main__()

