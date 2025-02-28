from PyQt5 import QtCore, QtGui, QtWidgets
import speech_recognition as sr
import pyttsx3
import wikipedia
import webbrowser
import os
from datetime import date
from datetime import datetime
import requests, json
import pydub
import io
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB


class Ui_Virtual_AI(object):
    def setupUi(self, Virtual_AI):
        Virtual_AI.setObjectName("Virtual_AI")
        Virtual_AI.resize(331, 473)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Virtual_AI.sizePolicy().hasHeightForWidth())
        Virtual_AI.setSizePolicy(sizePolicy)
        Virtual_AI.setMaximumSize(QtCore.QSize(331, 473))
        self.centralwidget = QtWidgets.QWidget(Virtual_AI)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 331, 451))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.background = QtWidgets.QFrame(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.background.sizePolicy().hasHeightForWidth())
        self.background.setSizePolicy(sizePolicy)
        self.background.setStyleSheet("background-color: #5F9EA0;")
        self.background.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.background.setFrameShadow(QtWidgets.QFrame.Raised)
        self.background.setObjectName("background")
        self.scrollArea = QtWidgets.QScrollArea(self.background)
        self.scrollArea.setGeometry(QtCore.QRect(-10, 40, 341, 361))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 339, 359))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.textEdit = QtWidgets.QTextEdit(self.scrollAreaWidgetContents)
        self.textEdit.setReadOnly(True)
        self.textEdit.setGeometry(QtCore.QRect(10, 10, 331, 351))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(14)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.background_label = QtWidgets.QWidget(self.background)
        self.background_label.setGeometry(QtCore.QRect(0, 0, 331, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.background_label.sizePolicy().hasHeightForWidth())
        self.background_label.setSizePolicy(sizePolicy)
        self.background_label.setStyleSheet("background-color: #FFFFFF;")
        self.background_label.setObjectName("background_label")
        self.NAME = QtWidgets.QLabel(self.background_label)
        self.NAME.setGeometry(QtCore.QRect(60, 0, 281, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.NAME.sizePolicy().hasHeightForWidth())
        self.NAME.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(28)
        font.setBold(False)
        font.setWeight(50)
        self.NAME.setFont(font)
        self.NAME.setAutoFillBackground(False)
        self.NAME.setObjectName("NAME")
        self.LOGO = QtWidgets.QLabel(self.background_label)
        self.LOGO.setGeometry(QtCore.QRect(0, 0, 51, 51))
        self.LOGO.setText("")
        self.LOGO.setPixmap(QtGui.QPixmap("../../../../Hình ảnh/Cuộn phim/d7de2ba4d7965d8c3293379a91f63414.jpg"))
        self.LOGO.setScaledContents(True)
        self.LOGO.setObjectName("LOGO")
        self.pushButton = QtWidgets.QPushButton(self.background)
        self.pushButton.clicked.connect(self.recognize_speech)
        self.pushButton.setGeometry(QtCore.QRect(140, 410, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: #fff;")
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.background, 0, 0, 1, 1)
        Virtual_AI.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Virtual_AI)
        self.statusbar.setObjectName("statusbar")
        Virtual_AI.setStatusBar(self.statusbar)

        self.retranslateUi(Virtual_AI)
        QtCore.QMetaObject.connectSlotsByName(Virtual_AI)

    def retranslateUi(self, Virtual_AI):
        _translate = QtCore.QCoreApplication.translate
        Virtual_AI.setWindowTitle(_translate("Virtual_AI", "MainWindow"))
        self.NAME.setText(_translate("Virtual_AI", "    VISON"))
        self.pushButton.setText(_translate("Virtual_AI", "START"))

    #virtual assistant
    def recognize_speech(self):
        self.robot_ear = sr.Recognizer()
        self.robot_mouth = pyttsx3.init()
        voices = self.robot_mouth.getProperty('voices')
        self.robot_mouth.setProperty('voice', voices[1].id)
        self.robot_mouth.setProperty('rate', 180)
        self.robot_mouth.setProperty('volume', 1.0)

        #ham loc tieng on
        def filter_noise(audio_segment):
            filtered = audio_segment.low_pass_filter(3000).high_pass_filter(300)
            return filtered

        # data huan luyen
        training_data = [
            ("what is the weather today", "weather"),
            ("open Chrome", "open_app"),
            ("open Google", "open_website"),
            ("open YouTube", "open_website"),
            ("open Facebook", "open_website"),
            ("can you help me", "help"),
            ("what time is it", "time"),
            ("find something", "wikipedia"),
            ("what day is today", "today"),
        ]

        # Tach cau lenh va nhan
        X_train = [x[0] for x in training_data]
        y_train = [x[1] for x in training_data]

        # Chuyen cau lenh thanh dac truc
        vectorizer = CountVectorizer()
        X_train_vec = vectorizer.fit_transform(X_train)

        # Huan luyen mo hinh Naive Bayes
        model = MultinomialNB()
        model.fit(X_train_vec, y_train)

        # Ham phan loai cau lenh
        def classify_command(command):
            X_test_vec = vectorizer.transform([command])
            return model.predict(X_test_vec)[0]

        # Ham xu ly cau lenh sau khi phan loai
        def process_command(command_type, you):
            self.robot_brain = ""
            if command_type == "help":
                return "Hello, how can I help you?"

            elif command_type == "open_website":
                if "Google" in you:
                    webbrowser.open('https://www.google.com/', new=1)
                    return "Ok, Google is opened"
                elif "Facebook" in you:
                    webbrowser.open('https://www.facebook.com/', new=1)
                    return "Ok, Facebook is opened"
                elif "YouTube" in you:
                    webbrowser.open('https://www.youtube.com/', new=1)
                    return "Ok, YouTube is opened"

            elif command_type == "weather":
                api_key = "34b04041f1e12e41d14a62c04d98cda7"
                base_url = "http://api.openweathermap.org/data/2.5/weather?"      
                self.update_conversation("VISON: Which city's weather would you like to check?")
                self.robot_mouth.say("Which city's weather would you like to check?")
                self.robot_mouth.runAndWait()

                with sr.Microphone() as mic:
                    self.update_conversation("VISON: I'm Listening")
                    audio = self.robot_ear.record(mic, duration = 5)                    
                    audio_segment = pydub.AudioSegment(
                        data=audio.get_raw_data(),
                        sample_width=audio.sample_width,
                        frame_rate=audio.sample_rate,
                        channels=1
                    )

                    filtered_audio = filter_noise(audio_segment)

                    raw_data = io.BytesIO()
                    filtered_audio.export(raw_data, format="wav")
                    raw_data.seek(0)

                    filtered_audio_for_recognition = sr.AudioData(
                        raw_data.read(),
                        filtered_audio.frame_rate,
                        filtered_audio.sample_width
                    )
                    try:
                        you = self.robot_ear.recognize_google(filtered_audio_for_recognition)
                        self.update_conversation("You: " + you)

                        complete_url = base_url + "appid=" + api_key + "&q=" + you
                        response = requests.get(complete_url)
                        x = response.json()
                        if x["cod"] != "404":
                            y = x["main"]
                            current_temperature = y["temp"] - 273.15
                            current_pressure = y["pressure"]
                            current_humidity = y["humidity"]
                            z = x["weather"]
                            weather_description = z[0]["description"]

                            return "Temperature (in Celsius unit): " + str(current_temperature) + ", atmospheric pressure (in hPa unit): " + str(current_pressure) + ", humidity (in percentage): " + str(current_humidity) + ", description: " + str(weather_description)

                        else:
                            return "City not found"
                    except:
                            return "Can't find"

            elif command_type == "wikipedia":
                self.update_conversation("This is Wikipedia")
                self.robot_mouth.say("This is Wikipedia")
                self.robot_mouth.runAndWait()

                while True:
                
                    with sr.Microphone() as mic:
                        self.update_conversation("VISON: I'm Listening")
                        audio = self.robot_ear.record(mic, duration = 3)                        
                        audio_segment = pydub.AudioSegment(
                            data=audio.get_raw_data(),
                            sample_width=audio.sample_width,
                            frame_rate=audio.sample_rate,
                            channels=1
                        )

                        filtered_audio = filter_noise(audio_segment)

                        raw_data = io.BytesIO()
                        filtered_audio.export(raw_data, format="wav")
                        raw_data.seek(0)

                        filtered_audio_for_recognition = sr.AudioData(
                            raw_data.read(),
                            filtered_audio.frame_rate,
                            filtered_audio.sample_width
                        )
                        try:
                            you = self.robot_ear.recognize_google(filtered_audio_for_recognition)
                            self.update_conversation("You: " + you)
                            self.update_conversation("VISON: ...")
                            if you == "thank" or you == "stop":
                                break
                            else:
                                try:
                                    searchresult = wikipedia.summary(you, sentences=2, auto_suggest=False, redirect=True)
                                except:
                                    searchresult = "Can't find"
                                
                                self.update_conversation("VISON: " + searchresult)
                                self.robot_mouth.say(searchresult)
                                self.robot_mouth.runAndWait()
                        except:
                            self.update_conversation("VISON: I can't get it")
                            self.robot_mouth.say("I can't get it")
                            self.robot_mouth.runAndWait()
                    
                return "End of Wikipedia search"
                            
            elif command_type == "time":
                now = datetime.now()
                return now.strftime("%H hours %M minutes %S seconds")

            elif command_type == "today":
                today = date.today()
                return today.strftime("%B %d, %Y")

            return "I don't understand, please try again"

        with sr.Microphone() as mic:
            self.update_conversation("VISON: I'm Listening")
            audio = self.robot_ear.record(mic, duration=3)            
            audio_segment = pydub.AudioSegment(
                data=audio.get_raw_data(),
                sample_width=audio.sample_width,
                frame_rate=audio.sample_rate,
                channels=1
            )

            filtered_audio = filter_noise(audio_segment)

            raw_data = io.BytesIO()
            filtered_audio.export(raw_data, format="wav")
            raw_data.seek(0)

            filtered_audio_for_recognition = sr.AudioData(
                raw_data.read(),
                filtered_audio.frame_rate,
                filtered_audio.sample_width
            )

            try:
                you = self.robot_ear.recognize_google(filtered_audio_for_recognition)
                self.update_conversation("You: " + you)
                self.update_conversation("VISON:...")
                # Phân loại câu lệnh
                command_type = classify_command(you)

                # Xử lý lệnh dựa trên loại câu lệnh
                self.robot_brain = process_command(command_type, you)
            
            except:
                self.update_conversation("You: ")
                self.robot_brain = "I can't not hear you, please try again"

        self.update_conversation(f"VISON: {self.robot_brain}")
        self.robot_mouth.say(self.robot_brain)
        self.robot_mouth.runAndWait()

    def update_conversation(self, message):
        self.textEdit.append(message)
        QtWidgets.QApplication.processEvents()        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Virtual_AI = QtWidgets.QMainWindow()
    ui = Ui_Virtual_AI()
    ui.setupUi(Virtual_AI)
    Virtual_AI.show()
    sys.exit(app.exec_())
