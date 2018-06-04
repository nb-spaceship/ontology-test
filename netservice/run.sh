sudo netstat -nlp|grep '0.0.0.0:10001'|awk '{print $7}'|awk -F / '{print $1}'|xargs kill >/dev/null 2>&1
python -u service.py
