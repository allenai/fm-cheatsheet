FROM python:3.8.18

# Uncomment the following lines to make PyTorch available to your application.
# See https://skiff.allenai.org/gpu.html for more details.
#
# ENV LD_LIBRARY_PATH /usr/local/nvidia/lib:/usr/local/nvidia/lib64
# ENV NVIDIA_VISIBLE_DEVICES all
# ENV NVIDIA_DRIVER_CAPABILITIES compute,utility
# RUN pip install torch==1.7.0+cu101 -f https://download.pytorch.org/whl/torch_stable.html

WORKDIR /app

# Install Python dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy over the source code
COPY . ./

ENV PYTHONPATH=$PYTHONPATH':app/'

# Kick things off
ENTRYPOINT [ "streamlit" ]
CMD [ "run", "./app.py" ]
