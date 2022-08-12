#!/home/pi/homeberryApi/bin/python
from flask import Flask
from apscheduler.schedulers.background import BackgroundScheduler
import subprocess


app = Flask(__name__)


@app.route("/")
def helloWorld():
	return "Hello World\n"

@app.route("/bt_speaker/stop")
def stopBtSpeaker():
	subprocess.run("sudo systemctl stop bt_speaker".split())
	return "Stopping bt_speaker service"

@app.route("/bt_speaker/start")
def startBtSpeaker():
	subprocess.run("sudo systemctl start bt_speaker".split())
	return "Starting bt_speaker service"

@app.route("/kodi/kill")
def killKodi():
	#subprocess.run("sudo systemctl stop kodi".split())
	subprocess.run("pkill -15 kodi".split())
	return "Killing Kodi service"

@app.route("/kodi/start")
def startKodi():
	subprocess.Popen("kodi".split(), start_new_session=True)
	#subprocess.run("sudo systemctl start kodi".split())
	return "Starting Kodi service"

@app.route("/mousepad/kill")
def killMP():
	subprocess.run("pkill -15 mousepad".split())
	return "Killing mousepad"

@app.route("/mousepad/start")
def startMP():
	subprocess.Popen("mousepad".split(), start_new_session=True)
	return "Starting mousepad"

@app.route("/tv/on")
def onTV():
	subprocess.run("./tv_on.sh".split())
	return "TV einschalten"

@app.route("/tv/standby")
def standbyTV():
	subprocess.run("./tv_off.sh".split())
	return "TV standby"

@app.route("/tv/input_pi")
def inPiTV():
	subprocess.run("./tv_hdmi3.sh".split())
	return "Quelle PI"

@app.route("/tv/input_sat")
def inSatTV():
	subprocess.run("./tv_hdmi2.sh".split())
	return "Quelle SAT"

@app.route("/shutdown")
def shutdown():
	subprocess.run("sudo shutdown -h now".split())
	return "Shutting down Raspberry"

@app.route("/reboot")
def reboot():
	subprocess.run("sudo shutdown -r now".split())
	return "Restarting Raspberry"

def test_job():
    print('switching off tv...')
    standbyTV()


if __name__ == '__main__':
	scheduler = BackgroundScheduler()
	job = scheduler.add_job(test_job, 'cron', day_of_week ='mon-sun', hour=2, minute=30)
	scheduler.start()
	app.run(host='0.0.0.0', port=5000)
