#!/bin/bash

SUB='OK UPLOAD'
tail -F /var/log/vsftpd.log | while read line; do
  if [[ "$line" == *"$SUB"* ]]; then
    echo "found"
    filename=$(echo "$line" | cut -d, -f2)
    if [ -s "$filename" ]; then
      echo "$filename was received"
    fi
  fi
done
