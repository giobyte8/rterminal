#
# Lightweight python image containing rterminal
#
# Note: Build context should be project's root.
# > See COPY commands below
#

FROM python:3.8.16-alpine3.16

WORKDIR /opt/rterminal
COPY rterminal/ /opt/rterminal/rterminal/
COPY requirements.txt /opt/rterminal/requirements.txt

RUN pip install -r requirements.txt
CMD [ "python", "rterminal/main.py" ]
