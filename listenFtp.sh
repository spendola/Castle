#!/bin/bash

SUB='OK UPLOAD'
tail -F /var/log/vsftpd.log | while read line; do
  if [[ "$line" == *"$SUB"* ]]; then
    msg=${line//[ ]/_}
    python3 FtpCallback.py $msg
  fi
done
