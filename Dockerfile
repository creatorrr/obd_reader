FROM python:3.5-onbuild

# Build deps
RUN apt-get -y update && apt-get install -y gpsd libfltk1.1 software-properties-common cmake

# Make obdgpslogger
RUN mkdir obdgpslogger/build
WORKDIR obdgpslogger/build

RUN cmake ..
RUN make
RUN make install

WORKDIR ..

# Test run
ENTRYPOINT obdsim
CMD ["-g", "Cycle", "&"]

